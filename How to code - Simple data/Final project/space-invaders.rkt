;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-abbr-reader.ss" "lang")((modname space-invaders) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
(require 2htdp/universe)
(require 2htdp/image)

;; Space Invaders

;; Constants:

(define WIDTH  300)
(define HEIGHT 500)

(define INVADER-X-SPEED 1.5)  ;speeds (not velocities) in pixels per tick
(define INVADER-Y-SPEED 1.5)
(define TANK-SPEED 3)
(define MISSILE-SPEED 10)

(define HIT-RANGE 10)

(define INVADE-RATE 100)

(define BACKGROUND (empty-scene WIDTH HEIGHT))

(define INVADER
  (overlay/xy (ellipse 10 15 "outline" "blue")              ;cockpit cover
              -5 6
              (ellipse 20 10 "solid"   "blue")))            ;saucer

(define TANK
  (overlay/xy (overlay (ellipse 28 8 "solid" "black")       ;tread center
                       (ellipse 30 10 "solid" "green"))     ;tread outline
              5 -14
              (above (rectangle 5 10 "solid" "black")       ;gun
                     (rectangle 20 10 "solid" "black"))))   ;main body

(define TANK-HEIGHT/2 (/ (image-height TANK) 2))
(define TANK-Y (- HEIGHT TANK-HEIGHT/2))
(define TANK-TURNR (- WIDTH (/ (image-width TANK) 2)))
(define TANK-TURNL (/ (image-width TANK) 2))
(define INVADER-TURNR (- WIDTH (/ (image-width INVADER) 2)))
(define INVADER-TURNL (/ (image-width INVADER) 2))
(define MISSILE (ellipse 5 15 "solid" "red"))


;; =======================================================================================
;; Data Definitions:

(define-struct game (invaders missiles t))
;; Game is (make-game  (listof Invader) (listof Missile) Tank)
;; interp. the current state of a space invaders game
;;         with the current invaders, missiles and tank position

;; Game constants defined below Missile data definition

#;
(define (fn-for-game s)
  (... (fn-for-loinvader (game-invaders s))
       (fn-for-lom (game-missiles s))
       (fn-for-tank (game-t s))))



(define-struct tank (x dir))
;; Tank is (make-tank Number Integer[-1, 1])
;; interp. the tank location is x, HEIGHT - TANK-HEIGHT in screen coordinates
;;         the tank moves TANK-SPEED pixels per clock tick left if dir -1, right if dir 1

(define T0 (make-tank (/ WIDTH 2) 1))   ;center going right
(define T1 (make-tank 50 1))            ;going right
(define T2 (make-tank 50 -1))           ;going left

#;
(define (fn-for-tank t)
  (... (tank-x t) (tank-dir t)))



(define-struct invader (x y dx))
;; Invader is (make-invader Number Number Number)
;; interp. the invader is at (x, y) in screen coordinates
;;         the invader along x by dx pixels per clock tick

(define I1 (make-invader 150 100 12))           ;not landed, moving right
(define I2 (make-invader 150 HEIGHT -10))       ;exactly landed, moving left
(define I3 (make-invader 150 (+ HEIGHT 10) 10)) ;> landed, moving right


#;
(define (fn-for-invader invader)
  (... (invader-x invader) (invader-y invader) (invader-dx invader)))

;; ListOfInvader is one of:
;; - empty
;; (cons Invader ListOfInvader)
(define LOI1 empty)
(define LOI2 (cons I1 empty))
(define LOI3 (cons I1 (cons I2 empty)))

#;
(define (fn-for-loi loi)
  (cond [(empty? loi) (...)]
        [else (... (fn-for-invader (first loi))
                   (fn-for-loi (rest loi)))]))


(define-struct missile (x y))
;; Missile is (make-missile Number Number)
;; interp. the missile's location is x y in screen coordinates

(define M1 (make-missile 150 300))                       ;not hit U1
(define M2 (make-missile (invader-x I1) (+ (invader-y I1) 10)))  ;exactly hit U1
(define M3 (make-missile (invader-x I1) (+ (invader-y I1)  5)))  ;> hit U1

#;
(define (fn-for-missile m)
  (... (missile-x m) (missile-y m)))

;; ListOfMissile is one of:
;; - empty
;; - (cons Missile ListOfMissile)

(define LOM1 empty)
(define LOM2 (cons M1 empty))
(define LOM3 (cons M2 (cons M3 empty)))
(define LOM4 (list M1 M3))

#;
(define (fn-for-lom lom)
  (cond [(empty? lom) (...)]
        [else (... (fn-for-missile (first lom))
                   (fn-for-lom (rest lom)))]))


(define G0 (make-game empty empty T0))
(define G1 (make-game empty empty T1))
(define G2 (make-game (list I1) (list M1) T1))
(define G3 (make-game (list I1 I2) (list M1 M2) T1))

;; =============================================================================

;; Functions

;; Game -> Game
;; start the world with (main G0)

(define (main g)
  (big-bang g                         ; G
            (on-tick   tock)          ; G -> G
            (to-draw   render)        ; G -> Image
            (stop-when over?)         ; G -> Boolean
            (on-key    handle-key)))  ; G KeyEvent -> G

;; Game -> Game
;; produce the next game state

(define (tock g)
  (make-game (add-invader (update-invaders (filter-invaders (game-invaders g) (game-missiles g))))
             (update-missiles (filter-missiles (game-missiles g) (game-invaders g)))
             (move-tank (game-t g))))


;;ListOfInvaders -> ListOfInvaders
;; randomly add 1 invader at random X coordinate

(define (add-invader loi)
  (cond [(> INVADE-RATE (random 5000)) (cons (make-invader (random WIDTH) 10 1) loi)]
        [else loi]))


;; ListOfInvaders -> ListOfInvaders
;; updates list of invaders by moving them downward
(define (update-invaders loi)
  (cond [(empty? loi) loi]
        [else (cons (update-invader (first loi))
                    (update-invaders (rest loi)))]))



;; Invader -> Invader
(define (update-invader i)
  (cond [(> INVADER-TURNL (+ (invader-x i) (* (invader-dx i) INVADER-X-SPEED)))
         (make-invader INVADER-TURNL
                       (+ (* INVADER-Y-SPEED (abs (invader-dx i)))
                          (invader-y i))
                       (-(invader-dx i)))]
        [(< INVADER-TURNR (+ (invader-x i) (* (invader-dx i) INVADER-X-SPEED)))
         (make-invader INVADER-TURNR
                       (+ (* INVADER-Y-SPEED (abs (invader-dx i)))
                          (invader-y i))
                       (-(invader-dx i)))]
        [else (make-invader (+ (invader-x i) (* INVADER-X-SPEED (invader-dx i)))
                            (+ (invader-y i) (* INVADER-Y-SPEED (abs (invader-dx i))))
                            (invader-dx i))]))


;; ListOfInvaders ListOfMissiles -> ListOfInvaders
;; produces a list of invaders which are not hit by missiles
(define (filter-invaders loi lom)
  (cond [(empty? loi) empty]
        [else (if (is-invader-hit? (first loi) lom)
                  (filter-invaders (rest loi) lom)
                  (cons (first loi) (filter-invaders (rest loi) lom)))]))


;; Invader ListOfMissile -> Boolean
;; Check if invader is hit
(define (is-invader-hit? i lom)
  (cond [(empty? lom) false]
        [else (or (is-hit? i (first lom))
                  (is-invader-hit? i (rest lom)))]))


;; Invader Missile -> Boolean
(define (is-hit? i m)
  (and (<= (abs (- (invader-x i)  (missile-x m))) HIT-RANGE)
       (<= (abs (- (invader-y i) (missile-y m))) HIT-RANGE)))



;; ListOfMissile -> ListOfMissile
;; produce new list of missiles
(define (update-missiles lom)
  (cond [(empty? lom) empty]
        [else (if (off? (first lom))
                  (update-missiles (rest lom))
                  (cons (update-missile (first lom))
                        (update-missiles (rest lom))))]))


;; Missile -> Missile
;; update position of one missile
(define (update-missile m)
  (make-missile (missile-x m) (- (missile-y m) MISSILE-SPEED)))



;; Missile -> Boolean
;; produce false if missile is off screen
(define (off? m)
  (<= (missile-y m) (- (/ (image-height MISSILE) 2))))




;; ListOfMissile ListOfInvader -> ListOfMissile
;; produce listofmissiles by filtering list of missiles
(define (filter-missiles lom loi)
  (cond [(empty? lom) empty]
        [else (if (is-missile-hit? (first lom) loi)
                  (filter-missiles (rest lom) loi)
                  (cons (first lom) (filter-missiles (rest lom) loi)))]))


;; Missile ListOfInvader -> Boolean
;; produce true if missile has hit any single invader
(define (is-missile-hit? m loi)
  (cond [(empty? loi) false]
        [else (or (is-hit? (first loi) m)
                  (is-missile-hit? m (rest loi)))]))


;;Tank -> Tank
;; Move the tank along screen
(define (move-tank t)
  (cond [(> (+ (tank-x t) (* TANK-SPEED (tank-dir t))) TANK-TURNR)
         (make-tank TANK-TURNR (tank-dir t))]
        [(< (+ (tank-x t) (* TANK-SPEED (tank-dir t))) TANK-TURNL)
         (make-tank TANK-TURNL (tank-dir t))]
        [else (make-tank (+ (tank-x t) (* TANK-SPEED (tank-dir t))) (tank-dir t))]))


;; ===================================================================================
;; Rendering


;; Game -> Image
;; render all invaders, missiles and the tank on screen
(define (render g)
  (render-tank-on (game-t g)
                  (render-missiles-on (game-missiles g)
                                      (render-invaders (game-invaders g)))))

;; Tank Image -> Image
;; produce and image with tank on
(define (render-tank-on t img)
  (place-image TANK (tank-x t) TANK-Y img))

;; ListOfMissiles Image -> Image
;; produce image with ListOfMissiles
(define (render-missiles-on lom img)
  (cond [(empty? lom) img]
        [else (add-missile-on (first lom)
                              (render-missiles-on (rest lom) img))]))

;; Missile Image -> Image
;; produce image with missile on top
(define (add-missile-on m img)
  (place-image MISSILE (missile-x m) (missile-y m) img))

;; ListOfInvaders -> Image
;; render all invaders
(define (render-invaders loi)
  (cond [(empty? loi) BACKGROUND]
        [else (add-invader-on (first loi)
                              (render-invaders (rest loi)))]))

;; Invader -> Image
;; add invader to the background
(define (add-invader-on i img)
  (place-image INVADER (invader-x i) (invader-y i) img))


;; ===================================================================================
;; Stop-When Functions

;; Game -> Boolean
;; Produce true if the game is over
(define (over? g)
  (touchdown? (game-invaders g)))
      

;; LOI -> Boolean
;; Produce true if any of the list of invaders has touched bottom
(define (touchdown? loi)
  (cond [(empty? loi) false ]
        [else (or (is-touching? (first loi))
                  (touchdown? (rest loi)))]))

;; Invader-> Boolean
;; produce true if invader is touching bottom of screen
(define (is-touching? invader)
  (>=  (invader-y invader) HEIGHT))


;; ===================================================================================
;; On-Key Function
;; Game KeyEvent -> Game
;; 'left' changes tank direction to left
;; 'right' changes tank direction to right
;; 'space' fires a missile
(define (handle-key g ke)
  (cond [(key=? ke " ")
         (make-game (game-invaders g) (cons (make-missile (tank-x (game-t g)) HEIGHT) (game-missiles g)) (game-t g))]
        [(and (= 1 (tank-dir (game-t g)))(key=? ke "left"))
         (make-game (game-invaders g) (game-missiles g) (make-tank (tank-x (game-t g)) -1))]
        [(and (= -1 (tank-dir (game-t g))) (key=? ke "right"))
         (make-game (game-invaders g) (game-missiles g) (make-tank (tank-x (game-t g)) 1))]
        [else g]))
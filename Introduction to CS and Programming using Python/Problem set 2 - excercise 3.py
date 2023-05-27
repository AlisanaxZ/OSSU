# Tinh so tien phai tra it nhat hang thang de co the tra het no trong 1 nam
# balance: Tien no
# annualInterestRate: Rate lai xuat hang nam
def calculate_balance(balance, annualInterestRate):
    # Cac gia tri can su dung
    monthlyInterestRate = annualInterestRate / 12.0
    lowerBound = balance / 12
    upperBound = (balance * (1+ monthlyInterestRate)**12)/12
    minimumMonthlyPayment = (upperBound + lowerBound)/2.0
    #Tim so tien can tra
    while True:
        remainingBalance = balance
        # Tinh so tien con no sau 1 nam
        for month in range(0,12):
            monthlyUpaidBalance = remainingBalance - minimumMonthlyPayment
            remainingBalance = round(monthlyUpaidBalance + (monthlyInterestRate * monthlyUpaidBalance),2)
        # Kiem tra xem so tien doan luc dau da dung chua
        if remainingBalance <= 0 and remainingBalance >= -0.01:
            break
        else:
            # Neu lon hon 0 thi so tien minh can tim lon hon so tien da doan
            if remainingBalance > 0:
                lowerBound = minimumMonthlyPayment
            else:
                # so tien can tim be hon so tien da doan
                upperBound = minimumMonthlyPayment
        # Doan gia tri moi
        minimumMonthlyPayment = (upperBound + lowerBound)/2.0
    #in kq
    print("Lowest Payment:", round(minimumMonthlyPayment,2))

balance = 320000
annualInterestRate = 0.2
calculate_balance(balance, annualInterestRate)
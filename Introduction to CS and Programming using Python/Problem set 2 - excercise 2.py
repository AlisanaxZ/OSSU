# Tinh so tien no con lai sau 1 nam
# balance: Khoan no ban dau
# anualInterestRate: Rate lai xuat cua nam
# minPayment: So minh doan la so tien tra hang thang
# remainingBalance: So no con lai
# month: thang bat dau
def caculate_Remaining_Balance(balance, annualInterestRate, minPayment, remainingBalance, month):
    if month < 12:
        month = month + 1
        rate = annualInterestRate/12.0
        remainingBalance = balance - minPayment
        nextBalance = remainingBalance + (rate * remainingBalance)
        return caculate_Remaining_Balance(nextBalance, annualInterestRate, minPayment,remainingBalance, month)
    else:
        return remainingBalance

#Tinh so tien it nhat phai tra trong 1 nam
# balance: so no ban dau
# anualInterestRate: Rate lai xuat hang nam
def caculate_Min_Payment(balance, annualInterestRate):
    #default khoan tra nho nhat = 10
    minPayment = 10
    # Doan gia tri cua khoan tien phai tra
    while minPayment <= balance:
        # Tinh so tien no con lai sau 1 nam
        Balance = caculate_Remaining_Balance(balance, annualInterestRate, minPayment, 0, 0)
        # Kiem tra neu so no be hon hoac bang 0 thi so tien it nhat phai tra la so tien da doan
        if round(Balance) <= 0:
            print("Lowest Payment:", minPayment)
            break
        # Neu chua bang khong thi them 10 vao so tien tra
        else:
            minPayment += 10

caculate_Min_Payment(320000, 0.2)
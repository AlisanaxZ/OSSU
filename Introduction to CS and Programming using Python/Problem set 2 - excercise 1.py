# Tinh so tien con no sau moi thang trong 1 nam
# Balance: So no ban dau
# annualInterestRate: Phan tram lai hang nam
# monthlyPaymentRate: Rate tra tien hang thang
# month: def 0
def caculate_Remaining_Balance(balance, annualInterestRate, monthlyPaymentRate , month):
    #dk de chuong trinh khong vuot qua 1 nam
    if month < 12:
        #Cac phep tinh de tinh tien no trong thang nay
        month = month + 1
        rate = annualInterestRate/12.0
        minPayment = monthlyPaymentRate * balance
        remainingBalance = balance - minPayment
        # In so tien no
        print("Month", month, "Remaining balance:", round(remainingBalance,2))
        #Tinh so tien no trong thang tiep theo
        nextBalance = remainingBalance + (rate * remainingBalance)
        caculate_Remaining_Balance(nextBalance, annualInterestRate, monthlyPaymentRate, month)

caculate_Remaining_Balance(4773, 0.2, 0.04, 1)
    
    
class bankAccount:
    def __init__(self,name,accountNo):
        self.name = name
        self.accountNO = accountNo

    def withdraworDeposit(self):
         choice = str(input("Withdraw or Deposit?"))
         try:
            if choice == 'withdraw':
                withdraw = input("Enter the amount you want to withdraw")
            elif choice == 'Deposit':
                deposit = input("Enter the amount you want to deposit: ")
         except Exception as ex:
            print(ex)
            return withdraw,deposit
         
    def withdraw(self,withdraw):
        print(f"your amount {withdraw} is succesfully withdrawn")

    def deposit(self,deposit):
        print(f"your amount {deposit} has deposited succesfully")

account1 = bankAccount("varun","7827787")
account1.withdraworDeposit()
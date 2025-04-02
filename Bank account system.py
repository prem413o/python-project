#create Account class with 2 attributes-balance,accountno 
#create method for debit , credit,printing balnce

class Account:

    def __init__(self,acc_no,balance):
        self.acc_no=acc_no
        self.balance=balance

    def credit(self,amount):
        self.balance+=amount
        print("your amount ",amount,"credited in your account no",self.acc_no)
        print("your total balance is",self.current_balance())


    def Debit(self,amount):
        self.balance-=amount
        print("Rupees",amount,"Debited from your account")
        print("total balance in your account is",self.current_balance())

    def current_balance(self):
        return self.balance
    

s1=Account(123,2000)
s1.Debit(500)
s1.credit(25000)
s1.credit(17000)
        
#create account class with 2 attributes
# - ballacne and account nuber
# create methods for debit, vredit and printing the balance
class Account:
    def __init__(self,bal,acc):
        self.balance = bal
        self.account_no= acc
    
    # debit method
    def debit(self, amount):
        self.balance -= amount
        print("your", amount," was debited")
        print("total balnace.",self.get_balance())
    
    def credited(self,amount):
        self.balance += amount
        print('rs', amount,"was credited")
        print("total balance =", self.balance)
    



         


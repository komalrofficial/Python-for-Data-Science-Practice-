#polymorphism

class  SavingAccount:
    __account_balance=100000;
    def display_balance(self):
        print(f"Your balance is{self.__account__balance}")
 
    def set_balance(self,amount):
        self.__account_balance=amount

class PFAccount(SavingAccount):
    __pf_acc_balance=30000;
    def display_balance(self):
        print(f"Your balance is{self. __pf_acc_balance}")

    def set_balance(self,amount):
        self.__pf_acc_balance=amount

class FDAccount(SavingAccount):
    __fd_acc_balance=500000;
    def display_balance(self):
        print(f"Your balance is{self.__fd_acc_balance}")

    def set_balance(self,amount):
        self.__fd_acc_balance=amount

class RDAccount(FDAccount):
    __rd_acc_balance=80000;
    def display_balance(self):
        print(f"Your balance is{self.__rd_acc_balance}")

    def set_balance(self,amount):
        self.__rd_acc_balance=amount    

rd=RDAccount()
rd.display_balance()
fd=FDAccount()
fd.display_balance()
#METHOD ABSTRACTION

class Account:
    __account_balance = 100000;
    __daily_limit = 100000;
    def display_balance(self):
        print(f"Your balance is{self.__account__balance}")
    
    def __amount_validate(self,amount):
        if amount>0 and  amount<1000000:
          return True;
        else:
          return False;


    def set_balance(self, amount):
        if self.__amount_validate(amount):
           print(f"Your current balance is{self.__account_balance}")
        else:
           print("Invalid Amount")

    def __check_pending_limit(self, amount):
        if self.__daily_limit > amount:
           self.__account_balance += amount
           self.__daily_limit -= amount
        else:
           print("your Daily limit reached,Please try after 24hrs")

acc = Account()
acc.set_balance(40000)


    


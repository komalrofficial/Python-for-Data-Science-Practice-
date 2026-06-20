#METHOD ABSTRACTION
#ABSTRACTION IS THAT IN WHICH WE HIDING THE  INTERNAL IMPLEMANTATION AND SHOWING ONLY ESSENTIAL INFORMATION OR THE REQUIRED FUNCTIONALITY TO THE USER.
class Account:
    __account_balance = 1000000;
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

# CLASS ABSTRACTION

class Payment_Gateway(ABC):
   @abstarctmethod
   def __amount_process(self):
      pass
   
class UPI(Payment_Gateway):
   def __amount_paid(self,amount):
      print(f"your amount is (amount)")

def amount_paid(self,amount):
      if amount>0 and amount<50000:
        if self.__isUPIID("upi123456"):
           print("UPI valided", amount)
           self.__amount_paid(amount)
    
       else:
           print("invalidUPI ID")


    def __isUPIID(self,id):
        if id:
           return True;
        else:
           return False;

class Credit_card(Payament_Gateway):
   
   __card_credit_status=True
  
   def amount_paid(self,amount):
      if amount>0 and amount<50000:
        if self.__iscreditNo(12345678) and self.__iscreditActive:
            self.__amount_paid(amount)
        else:
           print("unable to read card")

    def __isCreditNo(self.id):
        if id:
            return True;
        else:
             return False
      
online = UPI()
online.payment_process(2000)
cerdit= Creadit__card()
cerdit.payment_process(2000)

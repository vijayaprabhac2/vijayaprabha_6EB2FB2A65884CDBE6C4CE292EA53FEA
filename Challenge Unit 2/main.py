#
class BankAccount:
  def_init_(self,account_number,
account_hloder_name,
initial_balance=0):
      self.__account_number=
account_number 
     self._account holder_name
=account_holder_name
   self.__account_balance=
initial_balance 

   def deposit(self,amount):
     if amount>0:
       self.__account_balance+=
amount 
     return f"Deposited₹
  {amount}.New balance:₹
  {self.__account_balance}"
else :
return "Invalid deposit 
amount please enter a positive
amoun."
  def withdraw(self,amount):
    if 0 < amount <=
    self.__account_balance:
      return"Insufficient funds."
      else:
      return "Invalidwithdrawal
      amount please enter a positive 
    amount."
def display_balance(self):
  return f"Account balance for 
  {self._account_holdee_name}:₹
  {self._account_balance}"
#Testing the BankAccount class
if _=="__main__":
  account1 =
BankAccount("123456789",
"Ganeshkumar",1000)
print(account1.didplay__balance())
  print(account1.deposit(500))
  print(account1.withdraw(200))
  print(account1.withdraw(1500))

print(account1.display_balance())
# ============================================================================
# STUDENT TEST: ENCAPSULATION (Information Hiding)
# ============================================================================
# 
# INSTRUCTIONS: Follow each step below and write your code in the spaces provided.
# Each step builds on the previous one. DO NOT skip steps.
#
# ============================================================================

# ----------------------------------------------------------------------------
# STEP 1: Create a class called BankAccount
# ----------------------------------------------------------------------------
# 
# TASK: Create a class called BankAccount with:
# - A private attribute __balance initialized to 0
# - A private attribute __account_number initialized to "123456789"
#
# WRITE YOUR CODE BELOW:

class BankAccount:
    def __init__(self):
        self.__balance = 0
        self.__account_number = 123456789

# ----------------------------------------------------------------------------
# STEP 2: Add a method to display account information
# ----------------------------------------------------------------------------
# 
# TASK: Add a method called show_account_info() that prints:
# "Account Number: [account_number]"
# "Current Balance: $[balance]"
#
# HINT: Use the private attributes inside the method
#
# WRITE YOUR CODE BELOW (UPDATE YOUR CLASS FROM STEP 1):

    def show_account_info(self):
        print('Account Number is {} :'.format(self.__account_number))
        print('Current Balance is ${}:'.format(self.__balance))

# ----------------------------------------------------------------------------
# STEP 3: Create an object and test it
# ----------------------------------------------------------------------------
# 
# TASK: 
# 1. Create a BankAccount object called my_account
# 2. Call the show_account_info() method
# 3. Try to access __balance directly and see what happens (write your prediction)
#
# WRITE YOUR CODE BELOW:

my_account = BankAccount()
my_account.show_account_info()

# The Show Account info showed the account number and balance 

# ----------------------------------------------------------------------------
# STEP 4: Add Getter and Setter methods
# ----------------------------------------------------------------------------
# 
# TASK: Add these methods to your class:
# 
# 1. get_balance() - returns the current balance
# 2. set_balance(new_balance) - sets the balance BUT only if new_balance >= 0
#    If new_balance is negative, print "Error: Balance cannot be negative!"
#
# WRITE YOUR CODE BELOW (UPDATE YOUR CLASS FROM STEPS 1-2):
class BankAccount:
    def __init__(self):
        self.__balance = 0
        self.__account_number = 123456789

    def show_account_info(self):
            print('Account Number is {} :'.format(self.__account_number))
            print('Current Balance is ${}:'.format(self.__balance))

    def get_balance(self):
        return self.__balance

    def set_balance(self, new_balance):
         if new_balance >= 0:
              self.__balance = new_balance
         else:
            print('Errror: Balance cannot be neagative')
         
         
my_account = BankAccount()
my_account.show_account_info()




# ----------------------------------------------------------------------------
# STEP 5: Test the Getter and Setter
# ----------------------------------------------------------------------------
# 
# TASK: 
# 1. Create a BankAccount object called savings
# 2. Try to set the balance to 500 using set_balance()
# 3. Get and print the balance using get_balance()
# 4. Try to set the balance to -100
# 5. Show the account info using show_account_info()
#
# WRITE YOUR CODE BELOW:
class BankAccount:
    def __init__(self):
        self.__balance = 0
        self.__account_number = 123456789

    def show_account_info(self):
            print('Account Number is {} :'.format(self.__account_number))
            print('Current Balance is ${}:'.format(self.__balance))

    def get_balance(self):
        return self.__balance

    def set_balance(self, new_balance):
         if new_balance >= 0:
              self.__balance = new_balance
         else:
            print('Errror: Balance cannot be neagative')
         
savings = BankAccount()
savings.set_balance(500)
print('The Account balance is:', savings.get_balance())
print(savings.set_balance(-100))
savings.show_account_info()






# ----------------------------------------------------------------------------
# STEP 6: Add a deposit method
# ----------------------------------------------------------------------------
# 
# TASK: Add a method called deposit(amount) that:
# - Only deposits if amount > 0
# - If amount <= 0, print "Error: Deposit amount must be positive!"
# - If valid, adds the amount to __balance
# - Prints: "Deposited: $[amount]. New balance: $[new_balance]"
#
# WRITE YOUR CODE BELOW (UPDATE YOUR CLASS):

class BankAccount:
    def __init__(self):
        self.__balance = 0
        self.__account_number = 123456789

    def show_account_info(self):
            print('Account Number is {} :'.format(self.__account_number))
            print('Current Balance is ${}:'.format(self.__balance))

    def get_balance(self):
        return self.__balance

    def set_balance(self, new_balance):
         if new_balance >= 0:
              self.__balance = new_balance
         else:
            print('Errror: Balance cannot be neagative')
    
    def deposit(self, amount):
         if amount >0:
              self.__balance += amount
              print(f'Depostied: ${amount}. New Balance ${self.__balance}.')
         else:
              print('Error: The DEposit amount must be greater than 0')

        
         
         
# savings = BankAccount()
# savings.set_balance(500)
# print('The Account balance is:', savings.get_balance())
# print(savings.set_balance(-100))
# savings.show_account_info()





# ----------------------------------------------------------------------------
# STEP 7: Test the deposit method
# ----------------------------------------------------------------------------
# 
# TASK: 
# 1. Create a BankAccount object called checking
# 2. Set initial balance to 1000
# 3. Deposit 250
# 4. Deposit -50 (should show error)
# 5. Show account info
#
# WRITE YOUR CODE BELOW:

# checking = BankAccount()
# checking.set_balance(1000)
# checking.deposit(250)
# checking.deposit(-50)
# checking.show_account_info()





# ----------------------------------------------------------------------------
# STEP 8: Add a withdraw method
# ----------------------------------------------------------------------------
# 
# TASK: Add a method called withdraw(amount) that:
# - Checks if amount > 0, if not print "Error: Withdrawal amount must be positive!"
# - Checks if amount <= __balance, if not print "Error: Insufficient funds!"
# - If valid, subtracts amount from __balance
# - Prints: "Withdrew: $[amount]. New balance: $[new_balance]"
#
# WRITE YOUR CODE BELOW (UPDATE YOUR CLASS):

class BankAccount:
    def __init__(self):
        self.__balance = 0
        self.__account_number = 123456789

    def show_account_info(self):
            print('Account Number is {} :'.format(self.__account_number))
            print('Current Balance is ${}:'.format(self.__balance))

    def get_balance(self):
        return self.__balance

    def set_balance(self, new_balance):
         if new_balance >= 0:
              self.__balance = new_balance
         else:
            print('Errror: Balance cannot be neagative')
    
    def deposit(self, amount):
         if amount >0:
              self.__balance += amount
              print(f'Depostied: ${amount}. New Balance ${self.__balance}.')
         else:
              print('Error: The Deposit amount must be greater than 0')
    def withdraw(self, amount):
         if amount  < 0 :
              print('Error: Withdrawal amount must be positive!')
         elif amount > self.__balance:
              print('Error: Insufficient funds!')
              
         else:
              self.__balance -= amount
              print(f'Withdrew: ${amount}. New balance: ${self.__balance}')

# ----------------------------------------------------------------------------
# STEP 9: Test the withdraw method
# ----------------------------------------------------------------------------
# 
# TASK: 
# 1. Create a BankAccount object called personal
# 2. Set initial balance to 500
# 3. Withdraw 200
# 4. Withdraw 400 (should show insufficient funds error)
# 5. Show account info
#
# WRITE YOUR CODE BELOW:

personal = BankAccount()
personal.set_balance(500)
personal.withdraw(200)
personal.withdraw(400)
personal.show_account_info()






# ----------------------------------------------------------------------------
# STEP 10: Add a transfer method (Bonus Challenge)
# ----------------------------------------------------------------------------
# 
# TASK: Add a method called transfer(to_account, amount) that:
# - Checks if amount > 0, if not print "Error: Transfer amount must be positive!"
# - Checks if amount <= __balance, if not print "Error: Insufficient funds for transfer!"
# - If valid:
#   a. Withdraw amount from current account (use the withdraw method)
#   b. Deposit amount to to_account (use the deposit method)
#   c. Print: "Transferred: $[amount] to account [to_account_number]"
#
# HINT: You'll need to use the getter/setter or methods you already created
#
# WRITE YOUR CODE BELOW (UPDATE YOUR CLASS):

class BankAccount:
    def __init__(self):
        self.__balance = 0
        self.__account_number = 123456789

    def show_account_info(self):
            print('Account Number is {} :'.format(self.__account_number))
            print('Current Balance is ${}:'.format(self.__balance))

    def get_balance(self):
        return self.__balance

    def set_balance(self, new_balance):
         if new_balance >= 0:
              self.__balance = new_balance
         else:
            print('Errror: Balance cannot be neagative')
    
    def deposit(self, amount):
         if amount >0:
              self.__balance += amount
              print(f'Depostied: ${amount}. New Balance ${self.__balance}.')
         else:
              print('Error: The Deposit amount must be greater than 0')
    def withdraw(self, amount):
         if amount  < 0 :
              print('Error: Withdrawal amount must be positive!')
         elif amount > self.__balance:
              print('Error: Insufficient funds!')
              
         else:
              self.__balance -= amount
              print(f'Withdrew: ${amount}. New balance: ${self.__balance}')

    def transfer(self, to_account, amount):
          if amount < 0:
               print('Error: Transfer amount must be positive!')
          elif amount > self.__balance:
               print('Error: Insufficient funds for transfer!') 
          else:
               self.withdraw(amount)
               to_account.deposit(amount)
               print("Transferred: $", amount, " to account", to_account.__account_number)
               
# ----------------------------------------------------------------------------
# STEP 11: Test the transfer method
# ----------------------------------------------------------------------------
# 
# TASK: 
# 1. Create two BankAccount objects: account1 and account2
# 2. Set account1 balance to 1000
# 3. Set account2 balance to 0
# 4. Transfer 300 from account1 to account2
# 5. Show info for both accounts
# 6. Try to transfer 1000 from account1 to account2 (should show error)
#
# WRITE YOUR CODE BELOW:

account1 = BankAccount()
account2 = BankAccount()
account1.set_balance(1000)
account2.set_balance(0)
account1.transfer(account2, 300)
account1.show_account_info()
account2.show_account_info()
account1.transfer(account2, 1000)





# ----------------------------------------------------------------------------
# STEP 12: Reflection Questions
# ----------------------------------------------------------------------------
# 
# Answer the following questions in comments below:
# 
# 1. Why do we make attributes private (using '__')?
# so that it wont be used in other parts of the class unless
# you want it to.

     # so that they dont get overwritten or accessed by directly from out side the class
#
# 2. What is the purpose of getter and setter methods?
# the puropse of the getter and setter methods are to get a specific value(getter)
#and to set the specific value(setter)

     # The getter method retrives and returns an attributes value
     # The setter method checks, validates and updates an attributes value.
#
# 3. What happens if you try to access a private attribute directly?
# it wont let you because it needs you to use the self. before you can access
# the private attribute

     #it wont work because __ is hidden so when python tries to find it it cant because it is private.

#
# 4. Why is encapsulation useful in programming?
# so that you can use a name 2 times

     # encapsulation is useful in programing because it allowes you to all of your attributes and methods
     # into a single class with out it getting corroupted.
#
#

# ============================================================================
# END OF TEST
# ============================================================================
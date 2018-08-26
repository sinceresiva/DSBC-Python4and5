#**********Class defintions**************
class PiggyBankOperations:
    def __init__(self):
        self.piggyBank=PiggyBank()
        self.optionsInput=OptionsInput()
    def startOperations(self): 
        while(True):
            parentInput=self.optionsInput.getParentOperation() #parent operation is Start (s) or End (e)
            if parentInput=='e': #e means end
                break       
            operation = self.optionsInput.getOperation() #operation is Add (a), Withdraw (w) Or Check (c)
            if operation == 'a':
                amount=self.optionsInput.getAmount(operation)
                self.piggyBank.addAmount(amount)
                print("After adding the a/c balance is {}".format(self.piggyBank.getBalance()))
            elif operation == 'w':
                amount=self.optionsInput.getAmount(operation)
                self.piggyBank.withdrawAmount(amount)
                print("After withdrawing the a/c balance is {}".format(self.piggyBank.getBalance()))
            else:
                print("The balance of the account is {}: ".format(self.piggyBank.getBalance()))

class PiggyBank:
    def __init__(self):
        self.accountBalance = 0
    def addAmount(self,amount):
        self.accountBalance+=amount
    def withdrawAmount(self,amount):
        self.accountBalance-=amount
    def getBalance(self):
        return self.accountBalance

class OptionsInput:
    def getParentOperation(self):
        while(True):
            parentOperation = input("Start (s) or End (e): ").lower()
            if parentOperation!="start" and parentOperation!="s" and parentOperation!="end" and parentOperation!="e":
                print("Please enter a valid input (Start (s) or End (e))")
                continue
            else:
                break
        return parentOperation[0:1]

    def getOperation(self):
        while(True):
            operation = (input("Add (a), Withdraw (w) Or Check (c): ")).lower()
            if operation!="add" and operation!="a" and operation!="withdraw" and operation!="w" \
            and operation!="check" and operation!="c":
                print("Please enter a valid input (Add (a), Withdraw (w) Or Check (c))")                
            else:
                break
        return operation[0:1]

    def getAmount(self, code):
        amount=0
        while(True):
            if code=='a':
                msg="Add amount: "         
            else:
                msg="Withdraw amount: "
            amount=input(msg)
            if(not amount.isnumeric()):
                print("Please enter a valid (numeric) amount.")
                continue
            else:
                break
        return float(amount)

#***********Start Operations*************
bankOperations=PiggyBankOperations()
bankOperations.startOperations()

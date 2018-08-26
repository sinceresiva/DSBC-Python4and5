'''
Define a class MathOperation which implements pow(x,n) without using
python's in-built pow() method
'''
class MathOperation:
    def pow(self,x,n):
        return x**n
mathOper=MathOperation()
num=input("Enter the number:")
pw=input("The Power: ")
print("{} to the Power of {} is {}".format(num,pw,mathOper.pow(float(num),int(pw))))
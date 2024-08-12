x = int(input("Enter first number :"))
y = int(input("Enter second number :"))
def hcf(x,y):
     if x>y :
          smaller = y
     else:
         smaller = x
     for i in range(1,smaller+1):
         if x%i == 0 and y%i ==0 :
            HCF = i
     return HCF
HCF = hcf(x,y)
LCM = (x*y)/HCF
print("The HCF of x and y are = ",HCF)

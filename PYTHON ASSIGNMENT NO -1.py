# QUESTION NO.1

print("This Python program is used to find average of three numbers entered by the user")
print("Enter your first number:")
var1=int(input())
print("Enter your second number:")
var2=int(input())
print("Enter your third number:")
var3=int(input())
print("The average of these numbers is equal to ")
print((var1+var2+var3)/3)
print("")
print("")

# QUESTION NO.2

print("This python program is used to compute a person's income tax.")
print("Enter your Gross Income")
var1 = int(input())
print("Enter the number of dependents")
var2 = int(input())
print("Taxable income is equal to")
print(var1 - 10000 - (var2* 3000),"Rupees")
print(" ")
print("And The Income Tax is equal to")
print((var1 - 10000 - (var2* 3000))* 20,"Rupees")
print("")
print("")

# QUESTION NO.3

print("This program ask's the user for the number of seconds and prints out how many minutes and seconds that is equal to")
print("Enter the number of seconds you want to convert:")
var1=int(input())
print("This is equal to :")
print(var1//60,"Minutes",var1%60,"Seconds")
print("")
print("")

# QUESTION NO.4
print("This python program is used to add three numbers integer+’string’+float and produce result of this sum as string.")
print("Enter your first number:")
var1=int(input())
print("Enter your second number:")
var2=input()
print("Enter your third number:")
var3=float(input())
V=(var1+int(var2)+int(var3))
print("The sum as string is equal to :")
print(str(V))
print("")
print("")

# QUESTION NO.5

print("This program prints out the sine and cosine of the angles ranging from 0 to 345◦ in 15◦ increments")
print(" ")
print("So just enter the appropriate value of theta as mentioned by program ")
print(" ")
print("Enter the value of theta")
theta=int(input())
if theta==0:
    print("sin(theta)=0","And","cosine(theta)=1")
if theta==15:
    print("sin(theta)=0.2588","And","cosine(theta)=0.9659")
if theta==30:
    print("sin(theta)=0.5","And","cosine(theta)=0.8660")
if theta==45:
    print("sin(theta)=0.7071","And","cosine(theta)=0.7071")
if theta==60:
    print("sin(theta)=0.8660","And","cosine(theta)=0.5")
if theta==75:
    print("sin(theta)=0.9659","And","cosine(theta)=0.2588")
if theta==90:
    print("sin(theta)=1","And","cosine(theta)=0")
if theta==105:
    print("sin(theta)=0.9659","And","cosine(theta)=-0.2588")
if theta==120:
    print("sin(theta)=0.8660","And","cosine(theta)=-0.5")
if theta==135:
    print("sin(theta)=0.7071","And","cosine(theta)=-0.7071")
if theta==150:
    print("sin(theta)=0.5","And","cosine(theta)=-0.8660")
if theta==165:
    print("sin(theta)=0.2588","And","cosine(theta)=-0.9659")
if theta==180:
    print("sin(theta)=0","And","cosine(theta)=-1")
if theta==195:
    print("sin(theta)=-0.2588","And","cosine(theta)=-0.9659")
if theta==210:
    print("sin(theta)=-0.5","And","cosine(theta)=-0.8660")
if theta==225:
    print("sin(theta)=-0.7071","And","cosine(theta)=-0.7071")
if theta==240:
    print("sin(theta)=-0.8660","And","cosine(theta)=-0.5")
if theta==255:
    print("sin(theta)=-0.9659","And","cosine(theta)=-0.2588")
if theta==270:
    print("sin(theta)=-1","And","cosine(theta)=0")
if theta==285:
    print("sin(theta)=-0.9659","And","cosine(theta)=0.2588")
if theta==300:
    print("sin(theta)=-0.8660","And","cosine(theta)=-0.5")
if theta==315:
    print("sin(theta)=-0.7071","And","cosine(theta)=0.7071")
if theta==330:
    print("sin(theta)=-0.5","And","cosine(theta)=0.8660")
if theta==345:
    print("sin(theta)=-0.2588","And","cosine(theta)=0.9659")
if theta==360:
    print("sin(theta)=0","And","cosine(theta)=1")
List=[15,30,45,60,75,90,105,120,135,150,165,180,195,210,225,240,255,270,285,300,315,330,345,360]
if theta in List:
    print("your answer ")
else:
    print("The value of theta is not inserted in  program.so,enter the values as mentioned obove")

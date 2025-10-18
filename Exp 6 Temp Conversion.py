print("WELCOME TO PYTHON PROGRAMMING LANGUAGE")
print()
print("PROGRAM TO CONVERT CELSIUS SCALE TO FAHRENHEIT SCALE ACCORDING TO USER'S CHOICE")#Title
print()
print("OPTIONS OF CONVERSION")
print("1. To convert Celcius To Fahreheit")
print("2. To convert Fahrenheit To Celcius")
print()
choice=int(input("Enter the Choice(1/2):"))

if choice==1:
    cel=float(input("Enter the Temperature in Celcius:"))
    fah=(cel*9/5)+32
    print(f"{cel}°C in Fahrenheit is {fah}°F")
elif choice==2:
    fah=float(input("Enter the Temperature in Fahrenheit:"))
    cel=(fah-32)*5/9
    print(f"{fah}°F in Celcius is {cel}°C")
else:
    print("Enter a Vaalid Choice")

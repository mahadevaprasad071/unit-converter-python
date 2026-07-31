# Unit Converter

print("===== UNIT CONVERTER =====")
print("1. Kilometers to Miles")
print("2. Miles to Kilometers")
print("3. Celsius to Fahrenheit")
print("4. Fahrenheit to Celsius")

choice = int(input("Enter your choice (1-4): "))

if choice == 1:
    km = float(input("Enter kilometers: "))
    print("Miles =", km * 0.621371)

elif choice == 2:
    miles = float(input("Enter miles: "))
    print("Kilometers =", miles / 0.621371)

elif choice == 3:
    c = float(input("Enter Celsius: "))
    print("Fahrenheit =", (c * 9/5) + 32)

elif choice == 4:
    f = float(input("Enter Fahrenheit: "))
    print("Celsius =", (f - 32) * 5/9)

else:
    print("Invalid choice!")

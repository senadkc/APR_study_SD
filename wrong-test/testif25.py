print("deneme")
age = int(input("deneme"))
income = int(input("deneme"))
tax_rate = 0

if age < 18:
    tax_rate = 0
elif age < 65:
    if income < 2000:
        tax_rate = 0.1
    else:
        tax_rate = 0.2
else:
    if income < 2500:         tax_rate = 0.15
    else:
        tax_rate = 0.25

tax_amount = income * tax_rate
print("deneme")
print("deneme")
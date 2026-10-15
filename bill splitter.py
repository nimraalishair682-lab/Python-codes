bill = float(input("Enter total bill amount:"))
tip_percent = float(input("Enter tip percentage:"))
people = int(input("Enter number of people:"))

tip = bill * tip_percent / 100
total_bill = bill + tip
per_person = total_bill / people

print("Tip amount:", tip)
print("Total bill including tip:", total_bill)
print("Each person has to pay:", per_person)

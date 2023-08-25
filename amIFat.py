height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

bmi = round(weight / height ** 2)

statement = f"Your bmi is {bmi}, "
diagnosis = ""

if bmi < 18.5:
    diagnosis = "underweight"
elif bmi < 25:
    diagnosis = "okay"
elif bmi < 30:
    diagnosis = "little chunk"
elif bmi < 35:
    diagnosis = "fat"
elif bmi > 35:
    diagnosis = "damn"

print(statement + diagnosis)

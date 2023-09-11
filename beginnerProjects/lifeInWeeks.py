age = int(input("What is your current age? "))

years_remaining = 90 - age
weeks_remaining = years_remaining * 52
days_remaining = years_remaining * 365
months_remaining = years_remaining * 12

print(f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left")

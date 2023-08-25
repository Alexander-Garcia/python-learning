print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? ")[1:])
percent_tip = round(int(input("What percentage tip would you like to give? ")) / 100, 2)
number_of_people = int(input("How many people to split the bill? "))

bill_plus_tip = bill * (1 + percent_tip)
amount_for_each_person = round(bill_plus_tip / number_of_people, 2)
final_amount = "{:.2f}".format(amount_for_each_person)
print(f"Each person should pay: ${final_amount}")

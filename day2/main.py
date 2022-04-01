#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))

percentage_of_tip = int(input("How much tip would you like to give? 10, 12, or 15? "))

number_of_people_to_split = int(input("How many people to split the bill? "))

split_payment = (total_bill / number_of_people_to_split) * (percentage_of_tip / 100 + 1)

final = round(split_payment, 2)
final = "{:.2f}".format(split_payment)
message = (f"Each person should pay ${final}")

print(message)

print('Welcome to the tip calculator')
bill=input("What was the total bill? ")
tip=input("What percentage tip would you like to give? 10,12 or 15? ")
people=input("How many people to split the bill? ")
bills=float(bill)
tips=int(tip)
peoples=int(people)
pay=bills*(tips/100)+bills
pays=pay/peoples
final_amount=round(pays,2)
final_amount="{:2f}".format(pays)
print(f"Each person should pay: ${final_amount}")

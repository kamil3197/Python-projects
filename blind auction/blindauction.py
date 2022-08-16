'''from replit import clear - it'll work on website repl.it where i have done this project, this module clearing
screen beacuse after input a new user we don't want to see others bid'''
from art import logo
print(logo)
dictionary = {}
his_name = input("enter the name of a bidder\n")
his_bid = input("enter the bid\n$")
end_code = False
while end_code == False:

    def bidder(name, bid):
        dictionary[name] = bid

    bidder(name=his_name, bid=his_bid)
    clear()
    decision = input("Is there are other people who want to bid?\n").lower()
    if decision == "no":
        clear()
        all_values = dictionary.values()
        max_value = max(all_values)
        max_key = max(dictionary, key=dictionary.get)
        print(f"auction winner is {max_key} with bid ${max_value}")
        end_code = True
    else:
        clear()
        his_name = input("enter the name of a bidder\n")
        his_bid = input("enter the bid\n$")
        bidder(name=his_name, bid=his_bid)

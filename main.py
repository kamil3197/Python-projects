MENU = {
 "espresso": {
 "ingredients": {
 "water": 50,
 "coffee": 18,
 },
 "cost": 1.5,
 },
 "latte": {
 "ingredients": {
 "water": 200,
 "milk": 150,
 "coffee": 24,
 },
 "cost": 2.5,
 },
 "cappuccino": {
 "ingredients": {
 "water": 250,
 "milk": 100,
 "coffee": 24,
 },
 "cost": 3.0,
 }
}

resources = {
 "water": 300,
 "milk": 200,
 "coffee": 100,
}
print("welcome at coffee machine")
end_game = False


def user_wish(ask):
    return ask


def ingredients(MENU, ask, ingredient):
    if ask == 'espresso':
        ingredient['water'] = (MENU["espresso"]["ingredients"]["water"])
        ingredient['coffee'] = (MENU["espresso"]["ingredients"]["coffee"])
        ingredient['cost'] = (MENU["espresso"]["cost"])
        return ingredient
    elif ask == 'latte':
        ingredient['water'] = (MENU["latte"]["ingredients"]["water"])
        ingredient['milk'] = (MENU["latte"]["ingredients"]["milk"])
        ingredient['coffee'] = (MENU["latte"]["ingredients"]["coffee"])
        ingredient['cost'] = (MENU["latte"]["cost"])
        return ingredient
    elif ask == 'cappuccino':
        ingredient['water'] = (MENU["cappuccino"]["ingredients"]["water"])
        ingredient['milk'] = (MENU["cappuccino"]["ingredients"]["milk"])
        ingredient['coffee'] = (MENU["cappuccino"]["ingredients"]["coffee"])
        ingredient['cost'] = (MENU["cappuccino"]["cost"])
        return ingredient



def check_resources(resources, ingredient, ask):
    if ask == 'espresso':
        if resources['water'] >= ingredient['water']:
            if resources['coffee'] >= ingredient['coffee']:
                print('loading... there is enough resources to make a product')
            else:
                print('There is not enough coffee')
                global end_game
                end_game = True
                return end_game
        else:
            print('there is not enough water')
            end_game = True
            return end_game
    if ask == 'latte':
        if resources['water'] >= ingredient['water']:
            if resources['milk'] >= ingredient['milk']:
                if resources['coffee'] >= ingredient['coffee']:
                    print('loading... there is enough resources to make a product')
                else:
                 print('There is not enough coffee')
                 end_game = True
                 return end_game
            else:
                print('there is not enough milk')
                end_game = True
                return end_game
        else:
            print('there is not enough water')
            end_game = True
            return end_game
    if ask == 'cappuccino':
        if resources['water'] >= ingredient['water']:
            if resources['milk'] >= ingredient['milk']:
                if resources['coffee'] >= ingredient['coffee']:
                    print('loading... there is enough resources to make a product')
                else:
                    print('There is not enough coffee')
                    end_game = True
                    return end_game
            else:
                print('there is not enough milk')
                end_game = True
                return end_game
        else:
            print('there is not enough water')
            end_game = True
            return end_game


while not end_game:
    ask = input("what would you like? (espresso,latte,cappuccino)").lower()
    turn_off = False
    money = 0
    ingredient = {}
    ingredient_after = {}
    if ask == 'off':
        turn_off = True
        print(user_wish(ask))
        end_game = True
    elif ask == 'report':
        print("current resources:")
        print(f"water: {resources['water']}\nmilk: {resources['milk']}\ncoffee: {resources['coffee']}\nmoney: {money}")
        end_game = True
    else:
        ingredients(MENU, ask, ingredient)
        check_resources(resources, ingredient, ask)
        if check_resources(resources, ingredient, ask) is True:
            break
        else:
            print("you have to insert coins")
            quarters = float(input("how many quarters?")) * 0.25
            dimes = float(input("how many dimes?")) * 0.10
            nickles = float(input("how many nickles?")) * 0.05
            pennies = float(input("how many pennies?")) * 0.01
            total = quarters + dimes + nickles + pennies
            exchange = round(total - ingredient['cost'],2)
            print(f"here is ${exchange} in change")

            if total >= ingredient['cost']:
                if ask == 'espresso':
                    resources["money"] = ingredient["cost"]
                    ingredient_after['water'] = resources['water'] - ingredient['water']
                    ingredient_after['coffee'] = resources['coffee'] - ingredient['coffee']
                    ingredient_after['money'] = ingredient['cost']
                    resources = ingredient_after
                else:
                    resources["money"] = ingredient["cost"]
                    ingredient_after['water'] = resources['water'] - ingredient['water']
                    ingredient_after['coffee'] = resources['coffee'] - ingredient['coffee']
                    ingredient_after['milk'] = resources['milk'] - ingredient['milk']
                    ingredient_after['money'] = ingredient['cost']
                    resources = ingredient_after

            else:
                print("Sorry, that's not enough money, {money returned}")

            print(f"Resources left {resources}")
            print(f"Here is your {ask}, enjoy!")
            play_again = input("do you want something else? (yes or no)").lower()
            if play_again == 'yes':
                end_game = False
            else:
                end_game = True
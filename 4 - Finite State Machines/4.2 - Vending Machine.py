
drinks = [{"id": "water", "name": "Water", "price": 1}]
drinkStock = {"water": "infinite"}
acceptedMoney = [0.10, 0.20, 0.50, 1, 2]
# States
# * waitsForUserInput
#? * inputNotValid
# * waitsForMoney
#? * notEnoughMoney
#? * moreMoneyGiven
# * givesItem

state = "waitsForUserInput"

money = 10

chosenDrink = ""
moneyGiven = 0

while True:
    if state == "waitsForUserInput":
        drinksOption= ", ".join([drink["name"]+" $"+str(drink["price"]) for drink in drinks])
        chosenDrink = input(f"Choose drink ({drinksOption}): ")
        if chosenDrink.lower() not in [drink["id"] for drink in drinks]:
            print("Not a valid drink")
            state = "waitsForUserInput"
            continue
        else: 
            chosenDrink = next(drink for drink in drinks if drink["id"]== chosenDrink.lower()) 
            if drinkStock[chosenDrink["id"]] == "infinite" or drinkStock[chosenDrink["id"]] > 0:
                print(f"You chose {chosenDrink['name']}")
                state = "waitsForMoney"
            else:
                print("Out of stock")
                state = "waitsForUserInput"
            continue
    elif (state == "waitsForMoney"):
        if moneyGiven > 0:
            print("You gave me $" + str(moneyGiven))
        print("You have $" + str(money))
        moneyGivenInput = input("How much money to spend: ")
        try:
            moneyGivenInput = (float(moneyGivenInput))
        except:
            moneyGivenInput = 0
        if moneyGivenInput not in acceptedMoney:
            print("Not a valid money")
            state = "waitsForMoney"
            continue
        elif moneyGiven > money:
            print("You don't have that money")
            # money -= moneyGiven
            continue
        elif moneyGiven+moneyGivenInput == chosenDrink['price']:
            money -= moneyGiven
            state = "givesItem"
            continue
        elif moneyGiven+moneyGivenInput > chosenDrink['price']:
            moneyGiven += moneyGivenInput
            refundAmount = chosenDrink['price'] - moneyGiven
            money -= moneyGivenInput
            print(f"Too much money - refunding {refundAmount}")
            money += refundAmount
            state = "givesItem"
            continue
        elif moneyGiven+moneyGivenInput < chosenDrink['price']:
            print("Not enough money given")
            money -= moneyGiven
            moneyGiven += moneyGivenInput
            continue
    elif state == "givesItem":
        print(f"Here is your {str(chosenDrink['name'])}")
        print("Enjoy...\n")
        state = "waitsForUserInput"

        if drinkStock[chosenDrink["id"]] != "infinite" :
            drinkStock[chosenDrink["id"]] -= 1
        
        moneyGiven = 0
        chosenDrink = ""

        continue




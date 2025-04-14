restaurant = []

details = {
        "number": "001",
        "name":"JAVAS RESTAURANT",
        "address":"KAWEMPE, Bombo rd.",
        "contact person":"TWAHA",
        "contact":"0758102369",
        "opening hour":"06:00 am",
        "closing hour":"10:00 pm"
    }
restaurant.append(details)
meals = []
while True:
    meal_no = input("Enter meal number or 'Q' to quit: ")
    if meal_no.upper()=='Q':
        break

    meal_details = []

    for i in range(4):
        dish = input("Enter Food: ")
        meal_details.append(dish)
    drink = input("Enter Drink: ")
    meal_details.append(drink)
    price = int(input("PRICE = "))
    status = input("STATUS: ")

    mealdict = {
        "meal number": meal_no,
        "meal details":meal_details,
        "price":price,
        "status":status
    }
    meals.append(mealdict)

def display_restaurant_details():
    for detail in restaurant:
        print(f"\n=====JAVA RESTAURANT DETAILS=====\n")
        print(f'No. :\t\t\t{details.get("number")}\nName :\t\t\t{details.get("name")}\nAddress :\t\t{details.get("address")}\nContact person : \t{details.get("contact person")}\nContact :\t\t{details.get("contact")}\nOpening Hours :\t\t{details.get("opening hour")}\nClosing Hour :\t\t{details.get("closing hour")}')
        
    

print(display_restaurant_details())       


   
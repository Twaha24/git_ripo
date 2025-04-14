restaurant = []

details = {
        "number": "580",
        "name":"JAVAS",
        "address":"KAWEMPE",
        "contact person":"TWAHA",
        "contact":"0758102369",
        "opening hour":"06:00",
        "closing hour":"05:00"
    }
restaurant.append(details)

while True:
    meal_no = input("Enter meal number or 'Q' to quit: ")
    if meal_no.upper()=='Q':
        break

    meal_details = []

    for i in range(5):
        dish = input("Enter Food: ")
        meal_details.append(dish)
    
    price = int(input("PRICE = "))
    status = input("STATUS: ")

    mealdict = {
        "meal number": meal_no,
        "meal details":meal_details,
        "price":price,
        "status":status
    }
    restaurant.append(mealdict)

print(restaurant)

   
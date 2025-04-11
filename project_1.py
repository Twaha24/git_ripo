
restaurants = [
    [
    {
        "name":"JAVA",
        "location":"kawempe",
        "contact_person":"SHAFIK KIDOMOLA",
        "contact":"0758102363",
        "opening Hour":"08:00am",
        "closing Hour":"05:30pm",
        "restaurant no":"01"
    },
    {
        "name":"HEAVEN STONE",
        "location":"NAGURU",
        "contact_person":"LULE HUZAIPHA",
        "contact":"0700188669",
        "opening Hour":"08:00am",
        "closing Hour":"10:30pm",
        "restaurant no":"02"
    },
    {
        "name":"MIDDLE EAST",
        "location":"MAKINDYE",
        "contact_person":"KAKANDE SHARIF",
        "contact":"0758102365",
        "opening Hour":"08:00am",
        "closing Hour":"10:50pm",
        "restaurant no":"03"
    },
    {
        "name":"CHICKEN TONIGHT",
        "location":"WANDEGEYA",
        "contact_person":"GUMA RODNEY",
        "contact":"0758102364",
        "opening Hour":"09:00am",
        "closing Hour":"06:00pm",
        "restaurant no":"04"
    },
    {
        "name":"DA VEGAS",
        "location":"GAYAAZA",
        "contact_person":"TWAHA MAGALA",
        "contact":"0758102369",
        "opening Hour":"08:00am",
        "closing Hour":"06:00pm",
        "restaurant no":"05"
    }
    ],
    [
        {
            "restaurant no": "01",
            "meal no":" 01",
            "meal details":["CHICKEN PILAO: 20000","PLAIN PIALO: 10000","BEEF PILAO:25000",]
        }
    ]
]

'''meals = [
    {
        "meal no":"1",
        ""
    }
]'''
print(f"\n\t*****RESTAURANTS AVAILABLE*****\n")
counter = 0
for restaurant in restaurants:
    counter += 1
    print(f"\t0{counter}.) {restaurant["name"]}\n")
restaurant_choice = input('ENTER RESTAURANT NUMBER OR "Q" TO QUIT: ')
for restaurant in restaurants:
    if restaurant_choice == "01":
        name = "JAVA"
    elif restaurant_choice == "02":
        name = "HEAVEN STONE"
    elif restaurant_choice == "03":
        name = "MIDDLE EAST"
    elif restaurant_choice == "04":
        name = "CHICKEN TONIGHT"
    elif restaurant_choice == "05":
        name = "DA VEGAS"
    elif restaurant_choice.upper() == "Q":
        break

print(f"\nWELCOME TO {name} RESTAURANT")
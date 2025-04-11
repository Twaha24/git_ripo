restaurants = [
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
        "contact":"0758102362",
        "opening Hour":"08:00am",
        "closing Hour":"10:50pm",
        "restaurant no":"03"
    },
    {
        "name":"CHICKEN TONIGHT",
        "location":"WANDEGEYA",
        "contact_person":"GUMA RODNEY",
        "contact":"0758102361",
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
]
print(f"\n\t\tRESTAURANTS AVAILABLE")
counter = 0
for restaurant in restaurants:
    counter += 1
    print(f"\t0{counter}.) {restaurant["name"]}\n")

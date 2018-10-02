

def city_country(ci, co):
    """A function that lists city, country combinations using while Loop"""


    travel_destination = city + " " + country

while True:
    print("City and country of travel")
    print("Press q to quit anytime")

    city = input("city: ")
    if city == "q":
        break
    country = input("country: ")
    if country == "q":
        break



travel_destination = city_country(city, country)
print(travel_destination)

import inquirer
from inquirer import errors
from InquirerPy import prompt
from InquirerPy.validator import EmptyInputValidator
from colorama import Fore, init
import re
import time
init(autoreset=True)

print(Fore.YELLOW + '''
      
      
██╗  ██╗ ██████╗ ██╗     ██╗██████╗  █████╗ ██╗   ██╗    ██████╗  ██████╗  ██████╗ ██╗  ██╗██╗███╗   ██╗ ██████╗ 
██║  ██║██╔═══██╗██║     ██║██╔══██╗██╔══██╗╚██╗ ██╔╝    ██╔══██╗██╔═══██╗██╔═══██╗██║ ██╔╝██║████╗  ██║██╔════╝ 
███████║██║   ██║██║     ██║██║  ██║███████║ ╚████╔╝     ██████╔╝██║   ██║██║   ██║█████╔╝ ██║██╔██╗ ██║██║  ███╗
██╔══██║██║   ██║██║     ██║██║  ██║██╔══██║  ╚██╔╝      ██╔══██╗██║   ██║██║   ██║██╔═██╗ ██║██║╚██╗██║██║   ██║
██║  ██║╚██████╔╝███████╗██║██████╔╝██║  ██║   ██║       ██████╔╝╚██████╔╝╚██████╔╝██║  ██╗██║██║ ╚████║╚██████╔╝
╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝╚═════╝ ╚═╝  ╚═╝   ╚═╝       ╚═════╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝ 
                                                                                                                 
''')

# Price dictionaries
destination_prices = {
    "Spain": 300,
    "France": 350,
    "Germany": 400,
    "Japan": 800,
    "Iceland": 600,
    "Greece": 450,
    "Cyprus": 400
}

city_prices = {
    "Barcelona": 100,
    "Madrid": 120,
    "Valencia": 110,
    "Seville": 90,
    "Granada": 80,
    "Paris": 150,
    "Nice": 140,
    "Lyon": 130,
    "Marseille": 120,
    "Bordeux": 110,
    "Berlin": 160,
    "Munich": 150,
    "Hamburg": 140,
    "Frankfurt": 130,
    "Cologne": 120,
    "Tokyo": 200,
    "Kyoto": 180,
    "Osaka": 170,
    "Hiroshima": 160,
    "Sapporo": 150,
    "Reykjavik": 250,
    "Akureyri": 220,
    "Húsavík": 210,
    "Selfoss": 200,
    "Egilsstaðir": 190,
    "Athens": 140,
    "Thessaloniki": 130,
    "Santorini": 160,
    "Heraklion": 150,
    "Rhodes": 140,
    "Nicosia": 130,
    "Limassol": 120,
    "Larnaca": 110,
    "Paphos": 100,
    "Ayia Napa": 90
}

# Extras dictionary
extras_prices = {
    "Airport Transfer": 50,
    "Travel Insurance": 100,
    "City Tour": 70,
    "Room Upgrade": 150,
    "Car Rental": 80,
    "Special Meals": 40,
    "Spa Package": 120,
    "Sports Equipment Rental": 60,
    "Event Tickets": 90,
    "Kids Activities": 50
}

print("Hello, welcome to the Johnson's Bookings. Where will you be off to?\n")

total_price = 0  

while True: 
            email = input(Fore.YELLOW + "Enter email: " + Fore.RESET)
            if re.match(r'.+@.+\.(com|co\.uk)$', email):
                break 
            else:
                print(Fore.RED + "\nEmail not valid. Please try again.\n")

print("\n")
    
holiday_destinations_list = list(destination_prices.keys())

holiday_destination = [
    inquirer.List(
        "holiday_destinations",
        message=Fore.YELLOW + "Where will you be flying off to?",
        choices=holiday_destinations_list,
    ),
]

answers = inquirer.prompt(holiday_destination)
selected_country = answers['holiday_destinations']
print(Fore.YELLOW + f"You chose {selected_country} as your holiday destination.\n")

total_price += destination_prices[selected_country]


spain_list = ["Barcelona", "Madrid", "Valencia", "Seville", "Granada"]
france_list = ["Paris", "Nice", "Lyon", "Marseille", "Bordeux"]
germany_list = ["Berlin", "Munich", "Hamburg", "Frankfurt", "Cologne"]
japan_list = ["Tokyo", "Kyoto", "Osaka", "Hiroshima", "Sapporo"]
iceland_list = ["Reykjavik", "Akureyri", "Húsavík", "Selfoss", "Egilsstaðir"]
greece_list = ["Athens", "Thessaloniki", "Santorini", "Heraklion", "Rhodes"]
cyprus_list = ["Nicosia", "Limassol", "Larnaca", "Paphos", "Ayia Napa"]

city_lists = {
    "Spain": spain_list,
    "France": france_list,
    "Germany": germany_list,
    "Japan": japan_list,
    "Iceland": iceland_list,
    "Greece": greece_list,
    "Cyprus": cyprus_list
}

city_destination = [
    inquirer.List(
        "city_destinations",
        message=Fore.YELLOW + f"Where would you like to go in {selected_country}?",
        choices=city_lists[selected_country],
    ),
]

city_answers = inquirer.prompt(city_destination)
selected_city = city_answers['city_destinations']
print(Fore.YELLOW + f"You've chosen {selected_city}, {selected_country}.\n")

total_price += city_prices[selected_city]

print(Fore.YELLOW + "Loading extras...")

for seconds in range(3, -1, -1): #! countdown will be shown when the user hits enter
        time.sleep(1)


extras = [
    inquirer.Checkbox(
        "holiday_extras",
        message=Fore.YELLOW + "Select any additional extras for your holiday",
        choices=list(extras_prices.keys()),
    ),
]

extras_answers = inquirer.prompt(extras)
selected_extras = extras_answers['holiday_extras']

for extra in selected_extras:
    print(Fore.YELLOW + f"Adding price for {extra}: £{extras_prices[extra]}\n") 
    total_price += extras_prices[extra]

print("\n")

def validate_passengers(answer, current):
    if not current.isdigit():
        raise errors.ValidationError('', reason="Please enter a valid number.")
    num = int(current)
    if num < 1 or num > 10:
        raise errors.ValidationError('', reason="Please select between 1 and 10 passengers.")
    return True

passengers = [
    inquirer.Text(
        'passengers',
        message="Select how many passengers",
        validate=validate_passengers
    ),
]

passenger_result = inquirer.prompt(passengers)
num_passengers = int(passenger_result['passengers'])
print(Fore.YELLOW + f"Number of passengers: {num_passengers}")
print("\n")
total_price *= num_passengers

print(Fore.YELLOW + f"\nThe total price for your holiday is: £{total_price:.2f} or £{total_price/num_passengers:.2f}pp")

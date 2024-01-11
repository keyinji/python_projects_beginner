import requests

try:
    money = int(input("How much money do you want to convert? "))

    if money <= 0:
        print('You must enter a positive value')
        exit()
except ValueError:
    print("Invalid input. Please enter a whole number.")
    exit()

import requests

# Input for base and target currencies
base = input('What is the base currency? ').upper()
convert = input('What is the currency you want to convert to? ').upper()


# Constructing the API URL
url = f'https://v6.exchangerate-api.com/v6/API_KEY/latest/{base}'

# Making our request
try:
    response = requests.get(url)
    response.raise_for_status()  # Check if the request was successful
    data = response.json()

    # Check if the currencies are valid
    if base not in data['conversion_rates'] or convert not in data['conversion_rates']:
        print('Invalid currency')
        exit()

    # Get the conversion rate
    symbol = data['conversion_rates'][convert]
    print(f'{money} {base} is equal to {money * symbol} {convert}')

except requests.RequestException as e:
    print(f"Error while fetching data: {e}")

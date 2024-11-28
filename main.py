catalog = {
    "Bubble Sus": 1200,
    "AmongUs": 42,
    "Capybara Clicker": 234,
    "CS:GO": 400
}

print("Hello! This is the catalog of our games: ")

for game, price in catalog.items():
    print(f'{game} costs {price} UAH')

budget = int(input("What is your budget?\n"))
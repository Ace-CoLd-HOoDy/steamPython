catalog = {
    "Bubble Sus": 1200,
    "AmongUs": 42,
    "Capybara Clicker": 234,
    "CS:GO": 400
}

print("Hello! This is the catalog of our games: ")

for game, price in catalog.items():
    print(f'{game} costs: {price} UAH')

budget = int(input("What is your budget?\n"))
cart = []
total_cost = 0
print("Enter your game, or type 'стоп' to finish")

for i in range(len(catalog)):
    choice = input('Game: ')
    if choice.lower() == 'стоп':
        break
    elif choice in catalog:
        if total_cost + catalog[choice] > budget:
            print("You have no money, ahaha")
        else:
            cart.append(choice)
            total_cost += catalog[choice]
            print(f"{choice} added to your cart. Total cost {total_cost}")
    else:
        print("No game with that name")

print("Your cart")
for game in cart:
    print(f"{game} {catalog[game]} UAH")

print("Total cost", total_cost)
dwarfs = ["Doc", "Dopey", "Bashful", "Grumpy"]

def roll_call_dwarves(dwarfs):
    for i, dwarf in enumerate(dwarfs, start=1):
        print(f'{i}. {dwarf}')

planeteer_calls = ["earth", "wind", "fire", "water", "heart"]

def summon_captain_planet(planeteer_calls):
    return [call.capitalize() + '!' for call in planeteer_calls]

def long_planeteer_calls(calls):
    for call in calls:
        if len(call) > 4:
            return True
    return False

def find_the_cheese(snacks):
    cheeses = ['cheddar', 'gouda', 'camembert']
    for snack in snacks:
        if snack in cheeses:
            return snack
    return None

ingredients = ["garlic", "beer", "bread"]
print(find_the_cheese(ingredients))  # Output: "gouda"
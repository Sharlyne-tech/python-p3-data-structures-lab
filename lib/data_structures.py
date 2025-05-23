spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    names = [spicy_foods[i]["name"] for i in range(len(spicy_foods))]
    return names

def get_spiciest_foods(spicy_foods):
    spiciest = [spicy_foods[i] for i in range(len(spicy_foods)) if spicy_foods[i]["heat_level"] > 5]
    return spiciest

def print_spicy_foods(spicy_foods):
    [print(f"{spicy_foods[i]["name"]} ({spicy_foods[i]["cuisine"]}) | Heat Level: {'🌶' * spicy_foods[i]["heat_level"]}") for i in range(len(spicy_foods))]
    for i in range(len(spicy_foods)):
        print(f"{spicy_foods[i]['name']} ({spicy_foods[i]['cuisine']}) | Heat Level: {'🌶' * spicy_foods[i]['heat_level']}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for i in range(len(spicy_foods)): 
        if spicy_foods[i]["cuisine"] == cuisine:
            return spicy_foods[i]

def print_spiciest_foods(spicy_foods):
    [print(f"{spicy_foods[i]["name"]} ({spicy_foods[i]["cuisine"]}) | Heat Level: {'🌶' * spicy_foods[i]["heat_level"]}") for i in range(len(spicy_foods)) if spicy_foods[i]["heat_level"] > 5]
    [print(f"{spicy_foods[i]['name']} ({spicy_foods[i]['cuisine']}) | Heat Level: {'🌶' * spicy_foods[i]['heat_level']}") for i in range(len(spicy_foods)) if spicy_foods[i]['heat_level'] > 5]

def get_average_heat_level(spicy_foods):
    average = 0
@@ -43,4 +44,6 @@

def create_spicy_food(spicy_foods, spicy_food):
    newlist = spicy_foods + [spicy_food]
    return newlist
    return newlist

print_spicy_foods(spicy_foods=spicy_foods)

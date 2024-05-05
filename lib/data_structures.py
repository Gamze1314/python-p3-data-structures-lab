# with given list of dictionaries representing different spicy foods.
# use loops and list comprehensions alongside list and dict methods to solve these deliverables.

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

# this function takes a list of spicy_foods and returns a list of strings with the names.


def get_names(spicy_foods):
    # using get() method and list comprehension
    names = [food.get("name") for food in spicy_foods]
    return names


get_names(spicy_foods)


# takes a list , and returns a list of dictionaries for the food that has the heat_level greater than 5.
def get_spiciest_foods(spicy_foods):
    # iterate over the list to check heat_level properties
    # return if heat_level > 5
    # food.get("heat_level", 0) will return 0 if the "heat_level" key is not found in a dictionary, preventing a KeyError
    spiciest_foods = [
        food for food in spicy_foods if food.get("heat_level", 0) > 5]
    return spiciest_foods


get_spiciest_foods(spicy_foods)


# print(): Buffalo Wings (American) | Heat Level: 🌶🌶🌶
# f string formatting to concatenate strings
# * operator to multiply string emoji.
# avoid conflicts with string literals and single quotes.
def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        print(f"{food.get('name')} ({food.get('cuisine')}) | Heat Level: {food.get('heat_level', 0) * '🌶'}")


print_spicy_foods(spicy_foods)


# returns a single dictionary for the spicy food whose cuisine matches the cuisine being passed to the method.
def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    # take list and cuisine string
    matching_food = [
        food for food in spicy_foods if food.get("cuisine") == cuisine]
    return matching_food[0]


get_spicy_food_by_cuisine(spicy_foods, "American")


def print_spiciest_foods(spicy_foods):
    # prints the spiciest foods heat_level > 5
    # call get_spiciest_foods
    # if heat leave > 5
    spiciest_foods = get_spiciest_foods(spicy_foods)
    for food in spiciest_foods:
        print(f"{food.get('name')} ({food.get('cuisine')}) | Heat Level: {food.get('heat_level', 0) * '🌶'}")


print_spiciest_foods(spicy_foods)

# takes a list, and returns an integer =>average heat level


def get_average_heat_level(spicy_foods):
    total_heat_level = 0
    for food in spicy_foods:
        total_heat_level += food.get("heat_level", 0)
    average_heat_level = total_heat_level / len(spicy_foods)
    return average_heat_level

print(get_average_heat_level(spicy_foods))

def create_spicy_food(spicy_foods, spicy_food):
    # spicy food is a dict
    #returns the original list with new food added. 
    spicy_foods.append(spicy_food)
    return spicy_foods

print(create_spicy_food(spicy_foods, {
    'name': 'Griot',
    'cuisine': 'Haitian',
    'heat_level': 10,
}))


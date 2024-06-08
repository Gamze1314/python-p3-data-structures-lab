# with given list of dictionaries representing different spicy foods.
# use loops and list comprehensions alongside list and dict methods to solve these deliverables.
import ipdb


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
    # using get() method and list comprehension
    return [food.get("name") for food in spicy_foods]


get_names(spicy_foods)

# takes a list , and returns a list of dictionaries for the food that has the heat_level greater than 5.
def get_spiciest_foods(spicy_foods):
    # return if heat_level > 5  => filter spicy foods.
    return [food for food in spicy_foods if food["heat_level"] > 5]

get_spiciest_foods(spicy_foods)
# ipdb.set_trace()


# print(): Buffalo Wings (American) | Heat Level: 🌶🌶🌶
# f string formatting to concatenate strings
# * operator to multiply string emoji.
# avoid conflicts with string literals and single quotes.
# def print_spicy_foods(spicy_foods):


# print_spicy_foods(spicy_foods)


# # returns a single dictionary for the spicy food whose cuisine matches the cuisine being passed to the method.
# def get_spicy_food_by_cuisine(spicy_foods, cuisine):
#     # take list and cuisine string


# get_spicy_food_by_cuisine(spicy_foods, "American")


# def print_spiciest_foods(spicy_foods):
#     # prints the spiciest foods heat_level > 5
#     # call get_spiciest_foods
#     # if heat leave > 5


# print_spiciest_foods(spicy_foods)

# # takes a list, and returns an integer =>average heat level


# def get_average_heat_level(spicy_foods):


# print(get_average_heat_level(spicy_foods))

# def create_spicy_food(spicy_foods, spicy_food):
#     # spicy food is a dict
#     #returns the original list with new food added. 


# print(create_spicy_food(spicy_foods, {
#     'name': 'Griot',
#     'cuisine': 'Haitian',
#     'heat_level': 10,
# }))


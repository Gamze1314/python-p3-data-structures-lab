import statistics
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
def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        print(
            f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")


print_spicy_foods(spicy_foods)


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    # Filter out the list with matching cuisine.
    x = [food for food in spicy_foods if food["cuisine"] == cuisine]
    for food in x:
        return food


print(get_spicy_food_by_cuisine(spicy_foods, "American"))


def print_spiciest_foods(spicy_foods):
    # get spiciest foods.
    spicy_foods = get_spiciest_foods(spicy_foods)
    for food in spicy_foods:
        print(
            f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")


print_spiciest_foods(spicy_foods)


def get_average_heat_level(spicy_foods):
    # Extract all heat levels from spicy_foods
    heat_levels = [food.get("heat_level", 0) for food in spicy_foods]
    # Calculate the average heat level using mean
    average_heat_level = statistics.mean(heat_levels)

    return average_heat_level


print(get_average_heat_level(spicy_foods))


def create_spicy_food(spicy_foods, spicy_food):
    # Add the spicy_food to spicy_foods
    spicy_foods.append(spicy_food)
    return spicy_foods


print(create_spicy_food(spicy_foods, {
    'name': 'Griot',
    'cuisine': 'Haitian',
    'heat_level': 10,
}))

import numpy

from cocktail_data import CocktailData
from constants import DATA_FILE

user_cocktail = CocktailData.load_data(DATA_FILE)

# General recommendation


def general_recommendation():
    # Sort the list by highest rating.
    user_cocktail.sort(key=lambda c: c.rating, reverse=True)

    sample_cocktail = user_cocktail[:10]

    ing_list = []
    for i in sample_cocktail:
        ing_list += i.ingredients

    ing_set = set(ing_list)

    rating_ingredient_list = []
    for i in sample_cocktail:
        contains_ingredient = [0 for _ in range(len(ing_set))]
        for j in enumerate(ing_set):
            if j[1] in i.ingredients:
                contains_ingredient[j[0]] = 1*i.rating
        rating_ingredient_list.append(contains_ingredient)

    sum_arr = numpy.sum(rating_ingredient_list, axis=0)

    sum_rating = numpy.sum(sum_arr)

    weighted_ingredient_dict = dict()
    for ingredient, init_rating in zip(ing_set, sum_arr):
        weighted_ingredient_dict[ingredient] = init_rating/sum_rating

    print(weighted_ingredient_dict)

general_recommendation()

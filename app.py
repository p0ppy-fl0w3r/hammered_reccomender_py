import numpy

from cocktail_data import CocktailData
from constants import USER_DATA_FILE, SAMPLE_DATA_FILE


user_cocktail = CocktailData.load_data(USER_DATA_FILE)


def general_recommendation():
    # Sort the list by highest rating.
    user_cocktail.sort(key=lambda c: c.rating, reverse=True)

    sample_cocktail = user_cocktail[:10]

    ing_list = []
    for i in sample_cocktail:
        ing_list += i.ingredients

    # Converting list to sets will not enforce order.
    # To prevent variance in final value, convert the set to list and sort it.
    ing_set = list(set(ing_list))
    ing_set.sort()

    rating_ingredient_matrix = get_rating_list(sample_cocktail, ing_set, True)

    sum_arr = numpy.sum(rating_ingredient_matrix, axis=0)

    sum_rating = numpy.sum(sum_arr)

    weighted_ingredient_dict = dict()
    for ingredient, init_rating in zip(ing_set, sum_arr):
        weighted_ingredient_dict[ingredient] = init_rating/sum_rating

    sample_data = CocktailData.load_data(SAMPLE_DATA_FILE)
    sample_ingredient_matrix = get_rating_list(sample_data, ing_set, False)

    weighted_sample_matrix = dict()
    for ingredient_matrix, cocktail in zip(sample_ingredient_matrix, sample_data):
        weighted_sample_matrix[cocktail.cocktail] = get_weighted_rating(
            ingredient_matrix, weighted_ingredient_dict)

    recommendation = sorted(weighted_sample_matrix.items(), key=lambda c: c[1], reverse=True)[:4]
    
    print("Based on your previous interactions, you'll probably like the following:\n")
    for i in enumerate(recommendation, start=1):
        print(f"\t{i[0]}. {i[1][0]}")


def get_weighted_rating(ingredient_matrix, weighted_ingredient_matrix):
    total_weighted_rating = 0

    for ingredient_value, weighted_value in zip(ingredient_matrix,
                                                weighted_ingredient_matrix.values()):
        if ingredient_value > 0:
            total_weighted_rating += weighted_value

    return total_weighted_rating


def get_rating_list(sample, ing_set, is_weighted):
    """
    Creates a matrix of ingredients' availability in the given sample.

    Args:
        sample (List<CocktailData>): List of sample data.
        ing_set (List<str>): List of all ingredients.
        is_weighted (bool): Is the result weighted?

    Returns:
        List<int>: Matrix of ingredients' availability represented by 
        the rating if weighted else 1.
    """
    rating_ingredient_list = []
    for i in sample:
        contains_ingredient = [0 for _ in range(len(ing_set))]
        for j in enumerate(ing_set):
            if j[1] in i.ingredients:
                contains_ingredient[j[0]] = i.rating if is_weighted else 1
        rating_ingredient_list.append(contains_ingredient)

    return rating_ingredient_list


general_recommendation()

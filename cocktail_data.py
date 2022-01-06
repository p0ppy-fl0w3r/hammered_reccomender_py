import json

from constants import COCKTAIL, INGREDIENT, RATING


class CocktailData:
    """
    A representation of Cocktail with ingredients and rating.
    """

    def __init__(self, cocktail, ingredients, rating):
        self.cocktail = cocktail
        self.ingredients = ingredients
        self.rating = rating

    @staticmethod
    def from_json(json_data):
        """
        Creates a CocktailData using the given argument.

        Args:
            json_data (dict): A dictionary of raw cocktail data.

        Returns:
            CocktailData
        """

        return CocktailData(
            json_data[COCKTAIL], json_data[INGREDIENT], json_data[RATING]
        )

    @staticmethod
    def load_data(data_file):
        """
        Creates a list of CocktailData using the raw json data of the
        given file.

        Args:
            data_file (str): Filename of the file containing the raw json

        Returns:
            List<CocktailData>
        """

        with open(data_file, "r") as input_file:
            j_data = json.load(input_file)

        cocktail_list = []
        for j_cocktail in j_data:
            cocktail_list.append(CocktailData.from_json(j_cocktail))

        return cocktail_list

    def __str__(self):
        return f"Cocktail: {self.cocktail}\nIngredients: \
        {self.ingredients}\nRating: {self.rating}\n"

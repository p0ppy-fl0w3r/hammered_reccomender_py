import json

import constants

from cocktail_data import CocktailData

cocktail_list = CocktailData.load_data(constants.DATA_FILE)

for i in cocktail_list:
    print(i)
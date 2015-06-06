# -*- coding: utf-8 -*-

recipe_data_txt_file = open('recipe-data.txt', 'r')
recipe_data_txt_data = recipe_data_txt_file.read()
recipe_data_txt_file.close()

print(recipe_data_txt_data)
# -*- coding: utf-8 -*-

# file open
recipe_data_txt_file = open('recipe-data2.txt', 'r')

# insert txt data
recipe_data_txt_data = recipe_data_txt_file.read()

# file close
recipe_data_txt_file.close()

# show on console
print(recipe_data_txt_data)
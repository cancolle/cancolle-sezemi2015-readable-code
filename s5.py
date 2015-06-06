import random

# get the line's numbers of txt file
recipe_data_txt_file = open('recipe-data2.txt', 'r')

recipe_readline = recipe_data_txt_file.readline()

# list for recipe data & id
i = 0

recipe = []*100
recipe_id = []*100

while recipe_readline:
    recipe[i] = recipe_readline
    recipe_id[i] = random.randrange(1, 10000)
    i += 1
    print(recipe[i])
    recipe_readline = recipe_data_txt_file.readline()

recipe_data_txt_file.close()
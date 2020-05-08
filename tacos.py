import requests, docx



# Fetching data from url

url = 'https://taco-1150.herokuapp.com/random/?full_taco=true'

# Making request to the API server converting the JSON into a Python object

#requesting from API server and coverting it into a python object

response = requests.get(url).json()

#print(response)





#A word document

document = docx.Document()

# Adding a paragraph and a title

document.add_paragraph('Random Taco Cookbook', 'Title')

#Resizing a saved picture

document.add_picture('halfsize.jpg', width=docx.shared.Inches(5),

                   height=docx.shared.Cm(16))



# A paragraph  title

document.add_paragraph('Credits', 'Title')

# Citation

document.add_paragraph('The author of this picture is Natasha-bhogal on n Unsplash')

# Giving  Url for reference

document.add_paragraph('Tacos from https://taco-1150.herokuapp.com/random/?full_taco=true')

# Adding author paragraph

document.add_paragraph('Coded by Mohamud')





# looping to get data

for index in range(3):

    taco = requests.get(url).json()

    print(taco)

    mixin = taco['mixin']

    mixin_name = mixin['name']

    mixin_recipe = mixin['recipe']



    seasoning = taco['seasoning']

    seasoning_name = seasoning['name']

    seasoning_recipe = seasoning['recipe']



    condiment = taco['condiment']

    condiment_name = condiment['name']

    condiment_recipe = condiment['recipe']

    base_layer = taco['base_layer']

    base_layer_name = base_layer['name']



    shell = taco['shell']

    shell_name = shell['name']

    shell_recipe = shell['recipe']



    #Adding paragraphs

    document.add_paragraph(f'This is Mixin { mixin_name }', 'Heading 1')

    document.add_paragraph(mixin_recipe)

    # adding a paragraph for seasoning and seasoning recipe

    document.add_paragraph(f'This is Seasoning { seasoning_name}', 'Heading 1')

    document.add_paragraph(seasoning_recipe)

    # adding a paragraph for condiment  and condiment recipe

    document.add_paragraph(f'This is condiment { condiment_name} ', 'Heading 1')

    document.add_paragraph(condiment_recipe)



    document.add_paragraph(f'This is base layer {base_layer_name }', 'Heading 1')



    document.add_paragraph(f'This is shell  {shell_name}', 'Heading 1')

    document.add_paragraph(shell_recipe)

    #Breaking the document

    document.add_page_break()

    # saving document

    document.save('Tacos_recipe.docx')

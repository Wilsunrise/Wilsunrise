import random

# Lire les citations depuis le fichier
with open('quotes.txt', 'r') as file:
    quotes = file.readlines()

# Choisir une citation aléatoire
quote = random.choice(quotes).strip()

# Lire le contenu actuel du README
with open('README.md', 'r') as file:
    readme_contents = file.read()

# Construire le nouveau contenu du README
# Supposons que vous avez un placeholder dans votre README où vous voulez la citation aléatoire
# Par exemple: <!-- QUOTE_GOES_HERE -->
new_readme_contents = readme_contents.replace('<!-- QUOTE_GOES_HERE -->', quote)

# Écrire le nouveau contenu dans le README
with open('README.md', 'w') as file:
    file.write(new_readme_contents)

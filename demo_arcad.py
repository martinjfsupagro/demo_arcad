import requests
from bs4 import BeautifulSoup

def get_pokemon_evolution(pokemon_name):
    # Make a request to the pokepedia website
    url = f"https://pokepedia.fr/{pokemon_name}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the evolution information in the HTML
    evolution_section = soup.find('div', {'id': 'Évolution'})
    if not evolution_section:
        print(f"No evolution information found for {pokemon_name}.")
        return

    # Extract the evolution names from the HTML
    evolution_names = [link.text for link in evolution_section.find_all('a')]

    # Print the evolution names
    print(f"{pokemon_name} evolves into:")
    for name in evolution_names:
        print(name)

# Example usage
pokemon_name = input("Enter the name of a Pokemon: ")
get_pokemon_evolution(pokemon_name)

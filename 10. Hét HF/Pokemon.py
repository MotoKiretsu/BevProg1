import json

def main():
    KP = input("Adja meg a Kedvenc Pokemonját: \n") #KP = Kedvnec Pokemon
    PokemonLink=f"https://pokeapi.co/api/v2/pokemon/{KP}"
    Pokemon=open(f"{PokemonLink}","r")
    d = json.load(Pokemon)
    #HP
    print(d["stats"][0]["stats"]["name"]+": "+d["stats"][0]["base_stats"])
    #attack
    print(d["stats"][1]["stats"]["name"]+": "+d["stats"][1]["base_stats"])
    #defense
    print(d["stats"][2]["stats"]["name"]+": "+d["stats"][2]["base_stats"])
    #special-attack
    print(d["stats"][3]["stats"]["name"]+": "+d["stats"][3]["base_stats"])
    #special-defense
    print(d["stats"][4]["stats"]["name"]+": "+d["stats"][4]["base_stats"])
    #speed
    print(d["stats"][5]["stats"]["name"]+": "+d["stats"][5]["base_stats"])
    try:
        print("Types: "+d["types"][0]["type"]["name"]+", "+d["types"][1]["type"]["name"])
    except IndexError:
        print("Type: "+d["types"][0]["type"]["name"])
    Pokemon.close()

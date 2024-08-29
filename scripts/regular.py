import os
import json
from unidecode import unidecode

files = os.scandir("assets/regular")
dex = json.load(open("scripts/pokedex.json", "r"))

for i in files:
    name = i.name.lower().replace("'", "").replace(". ", "-").replace(" ", "-").replace("gigantamax", "gmax")
    stripped_name = unidecode(name.removesuffix(".png").removesuffix("percent"))
    for e in dex:
        entry_name = str(e["pokedex_number"]).zfill(3)+"-"+e["name"].removesuffix("-m").removesuffix("-f")
        form_name = "-".join(stripped_name.split("-")[1:])
        if stripped_name == entry_name:
            print("put ", stripped_name.replace("-"+e["name"], ""))
            pk_name = e["name"]
            os.rename(i.path, f"assets/regular/{stripped_name.replace('-'+pk_name, '')}.png")
            continue
        else:
            for form in e["forms"]:
                if form_name == form.replace("-cap", "").replace("-striped", ""):
                    print("put ", stripped_name.replace("-"+e["name"], ""))
                    pk_name = e["name"]
                    os.rename(i.path, f"assets/regular/{stripped_name.replace('-'+pk_name, '')}.png")
            continue
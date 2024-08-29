import os
import json
import shutil

files = os.scandir("assets/shiny")
dex = json.load(open("scripts/pokedex.json"))
total = 0

names = []
successes = []

for i in files:
    name = i.name.lower().split(" ")[0]
    stripped_name = "-".join(name.split("-")[1:])
    names.append(stripped_name)
    for e in dex:
        if stripped_name == e["name"]:
            print("yay ", stripped_name)
            file_name = str(e["pokedex_number"]).zfill(3)+stripped_name.replace(e["name"], "")+".png"
            shutil.copy(i.path, f"assets/shiny/{file_name}")
            successes.append(stripped_name)
            total += 1
        else:
            for form in e["forms"]:
                fixed_name = stripped_name.replace("-drive", "").replace("-flower", "").replace("-memory", "").replace("-breed", "").replace("-shield", "").replace("-cloak", "").replace("-form", "")
                if fixed_name == form:
                    print("yay ", stripped_name)
                    file_name = str(e["pokedex_number"]).zfill(3)+fixed_name.replace(e["name"], "")+".png"
                    shutil.copy(i.path, f"assets/shiny/{file_name}")
                    successes.append(stripped_name)
                    total += 1
print(total)

final = list(set(names)-set(successes))
print(len(names))
print(final)
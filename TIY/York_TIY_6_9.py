my_favorite_places = {"McKinstry" : ["The Baseball Field (Wrigley Field in Chicago)", "The Beach (Fernandina Beach Fl", "FWCS Career Academy"], "Caleb" : ["Colorado (Mountains)", "Great American Ballpark"], "Luke" : ["Kreager", "Indie", "US Open (Where ever the stadium is)"]}

for key, value in my_favorite_places.items():
    print(f"\nThese are {key} favorite places: ", end="")
    print(*value, sep=", ", end="")
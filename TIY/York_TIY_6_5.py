Rivers = {"Maumee" : "United States", "Nile" : "Egypt", "Congo" : "Africa"}

for river, country in Rivers.items():
    if river == "Maumee":
        print(f"\nThe {river} runs through Indiana.")
    else:
        print(f"\nThe {river} runs through {country}.")

for river in Rivers.keys():
    print(river)

for country in Rivers.values():
    print(country)
cities = {
          "Chicago" : {"country": "US", "population" : "2.665 million", "fact" : "Chicago is comprised of 77 community areas."},
          "Indianapolis" : {"country": "US", "population" : "880,621", "fact" : "It's the state capitol with the second-biggest population."},
          "Riverdale" : {"country": "US", "population" : "10,266", "fact" : "Settled in 1850."}
          }

for city, dict in cities.items():
    print(f"\n{city}")
    for key, value in dict.items():
        print(f"\t{key}: {value}")
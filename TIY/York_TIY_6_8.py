Charles = {"Name" : "Charoles", "Breed" : "Poodle", "Owner" : "Paul"}
Jimmy = {"Name" : "Jimmy", "Breed" : "Shih Tzu", "Owner" : "Martha"}
Ivan = {"Name" : "Ivan", "Breed" : "Boston Terrier", "Owner" : "Dral"}
Train = {"Name" : "Train", "Breed" : "Golden Lab", "Owner" : "William"}
Bolt = {"Name" : "Bolt", "Breed" : "Cavalier", "Owner" : "Braxon"}
Bridget = {"Name" : "Bridget", "Breed" : "Rottweiler", "Owner" : "Truman"}
Bracks = {"Name" : "Bracks", "Breed" : "Bulldog", "Owner" : "Kinley"}

Pets = [Charles, Jimmy, Ivan, Train, Bolt, Bridget, Bracks]

for pet in Pets:
    for key, value in pet.items():
        print(f"\n{key}: {value}")


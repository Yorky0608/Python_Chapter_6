people = {"John" : [6,9], "Paul" : [7,0], "Joshua" : [77,71], "Tim" : [25,17], "Polk" : [99,90]}

for person, num in people.items():
    print(f"\nThis is {person} favorite numbers: ", end="")
    print(*num, sep=", ", end="")
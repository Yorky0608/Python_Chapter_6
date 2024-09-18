import csv
# Pull in the CSV file
filename = 'candy_type.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # Loop through the csv file and create two lists
    candy_type = []
    candy_price = []

    for row in reader:
        candy = row[1]
        price = float(row[2])
        candy_type.append(candy)
        candy_price.append(price)
    print(candy_type)
    print(candy_price)

candy_dict = {candy_type[i]: candy_price[i] for i in range(len(candy_type))}

print(candy_dict)

list= []

for i in range(len(candy_type)):
    for b in range(len(candy_type)-1):

        if candy_type[i].replace("'", "").title() == candy_type[b].replace("'", "").title() and i != b:
            if b not in list and i not in list:
                print(f"{candy_type[b]} is a duplicate")
                list.append(b)

temp_dict = {candy_type[i]: candy_price[i] for i in range(len(candy_type))}

for type, price in candy_dict.items():
    if price > 3:
        del temp_dict[type]

print(temp_dict)

for type, price in temp_dict.items():
    if type == 'Skittles' or type == 'mints' or type == 'Gummy Bears' or type == 'Candy Corn ':
        temp_dict[type] = [price, "not chocolate"]
    else:
        temp_dict[type] = [price, "chocolate"]

print(temp_dict)

for type, values in temp_dict.items():
    if values[1] == 'chocolate':
        print(f"{type} needs to be kept refrigerated since it is chocolate.")
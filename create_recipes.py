cook_book = {}
with (open('recipes.txt', 'r', encoding = "UTF-8") as f):
    cook_name = f.readline().strip()
    count = f.readline().strip()
    cook_book[cook_name] = []
    for i in range(int(count)):
        line = f.readline().strip()
        list = []
        for item in line.replace(' | ', ' ').split():
            list.append(item)
            cook_values = {}
        cook_values['ingredient_name'] = list[0]
        cook_values['quantity'] = list[1]
        cook_values['measure'] = list[2]
        cook_book[cook_name] += [cook_values]
    while True:
        cook_name = f.readline().strip()
        if(cook_name == ''):
            cook_name = f.readline().strip()
            if (cook_name == ''):
                print(cook_book)
                break
            count = f.readline().strip()
            cook_book[cook_name] = []
            for i in range(int(count)):
                line = f.readline().strip()
                list = []
                for item in line.replace(' | ', ' ').split():
                    list.append(item)
                    cook_values = {}
                cook_values['ingredient_name'] = list[0]
                cook_values['quantity'] = list[1]
                cook_values['measure'] = list[2]
                cook_book[cook_name] += [cook_values]



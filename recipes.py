cook_book = {
    'Овсяная каша': [
        {'ingredient_name': 'Овсянка', 'quantity': 70, 'measure': 'гр.'},
        {'ingredient_name': 'Молоко', 'quantity': 50, 'measure': 'мл'},
        {'ingredient_name': 'Вода', 'quantity': 50, 'measure': 'мл'}
        ],
    'Стейк из говядины': [
        {'ingredient_name': 'Кусок говядины', 'quantity': 1, 'measure': 'шт'},
        {'ingredient_name': 'Масло', 'quantity': 10, 'measure': 'мл'},
        {'ingredient_name': 'Приправы', 'quantity': 5, 'measure': 'гр'},
        ],
    'Лапша с морепродуктами': [
        {'ingredient_name': 'Морепродукты', 'quantity': 300, 'measure': 'гр'},
        {'ingredient_name': 'Лапша', 'quantity': 70, 'measure': 'гр'},
        {'ingredient_name': 'Вода', 'quantity': 1000, 'measure': 'мл'},
        ],
    'Топор': [
        {'ingredient_name': 'Деревянная рукоять', 'quantity': 1, 'measure': 'шт'},
        {'ingredient_name': 'Железное окончание', 'quantity': 1, 'measure': 'шт'},
        {'ingredient_name': 'Клей', 'quantity': 1, 'measure': 'гр'},
        ]
    }

def get_shop_list_by_dishes(dishes, person_count):
    dishes_for_people = {}
    for dish in dishes:
        for cook in cook_book:
            if cook == dish:
                for ingredient in cook_book.get(cook):
                    ingredient_parameters_list = {}
                    ingredient_list = list(ingredient.values())
                    ingredient_parameters_list['measure'] = ingredient_list[2]
                    if ingredient_list[0] in dishes_for_people:
                        ingredient_parameters_list['quantity'] = ingredient_list[1] * person_count + list(dishes_for_people[ingredient_list[0]].values())[1]
                    else:
                        ingredient_parameters_list['quantity'] = ingredient_list[1] * person_count
                    dishes_for_people[ingredient_list[0]] = ingredient_parameters_list
    print(dishes_for_people)

get_shop_list_by_dishes(['Овсяная каша', 'Топор'], 2)
get_shop_list_by_dishes(['Стейк из говядины', 'Стейк из говядины'], 2)
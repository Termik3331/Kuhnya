# Задание 1
with open('recipes.txt', encoding='utf-8') as file:
    cook_book = {}
    for i in file:
        recipes_name = i.strip()
        ingredients_count = file.readline()
        ingredients = []
        for p in range(int(ingredients_count)):
            recipes = file.readline().strip().split(' | ')
            product, quantity, word = recipes
            ingredients.append({'product': product, 'quantity': quantity, 'measure': word})
        file.readline()
        cook_book[recipes_name] = ingredients
    print(cook_book)
# Задание 2
def get_shop_list_by_dishes(person_count: int, dishes: list):
    result = {}
    for dish in dishes:
        if dish in cook_book:
            for consist in cook_book[dish]:
                if consist['product'] in result:
                    result[consist['product']]['quantity'] += consist['quantity'] * person_count
                else:
                    result[consist['product']] = {'measure': consist['measure'],'quantity': (consist['quantity'] * person_count)}
        else:
            print('Такого блюда нет в книге')
    print(result)
get_shop_list_by_dishes(2, ['Запеченный картофель', 'Омлет'])

# Задание 3

path = './text/'

d = {}
for i in range(1, 3):
    name = f'{path}{i}.txt'
    with open(name, 'r', encoding='utf-8') as f:
        d[name] = [x for x in f.read().splitlines() if x]

with open('final_file.txt', 'w', encoding='utf-8') as file:
    for k, v in sorted(d.items(), key=lambda x: len([x[-1]])):
        file.write(k + '\n')
        file.write('Количество строк: ' +str(len(v)) + '\n')
        file.write('\n'.join(v))
        file.write('\n')
print('Выполнено')
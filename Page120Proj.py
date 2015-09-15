import pprint

inv = {'sword': 2, 'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'ruby', 'pin', 'pin', 'pin']

def display_inventory(stuff):
    print('Inventory:')
    total_num_items = 0
    for k, v in stuff.items():
        print(str(k) + ': ' + str(v))
        total_num_items += v
    print('Total number of items: ' + str(total_num_items))

def addToInventory(stuff, addedItems):
    for item in addedItems:
        stuff.setdefault(item, 0)
        stuff[item] += 1


#displayInventory(inv)
addToInventory(inv, dragonLoot)
pprint.pprint(inv)

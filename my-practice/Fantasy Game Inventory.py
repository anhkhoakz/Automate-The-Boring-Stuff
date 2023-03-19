inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def displayInventory(inventory):
    print('Inventory: ')
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' +k)
        item_total += v
    print('Total number of items: '+str(item_total))
displayInventory(inventory)

def addToInventory(inventory, addedItems):
    for item in addedItems:
        if item in inventory.keys():
            inventory[item] += 1 #Increment quantity if item already exist in inv
        else: 
            inventory.setdefault(item, 1) #Create item in inv if doesnt already exist

inventory = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inventory = addToInventory(inventory, dragonLoot)
displayInventory(inventory)
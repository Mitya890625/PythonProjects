
resulted_inv = {}
while True:
    try:
        data = input()
    except KeyboardInterrupt:
        print()
        break
    if data in resulted_inv:
        resulted_inv[data] += 1
    else:
        resulted_inv[data] = 1
for item, quantity in resulted_inv.items():
    print(quantity, item.upper())








'''
inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
for i in range(len(dragonLoot)):
    if  dragonLoot[i] in inv:
        inv[dragonLoot[i]] += 1
    else:
        inv[dragonLoot[i]] = 1
print(inv)
'''

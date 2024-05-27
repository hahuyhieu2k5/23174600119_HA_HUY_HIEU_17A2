inventory = {
    'gold':800,
    'pouch': ['flint', 'twine', 'gemstone'],
    'backpack': ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}
inventory['pocket'] = ['seashell', 'strange berry', 'lint']
inventory['backpack'].sort()
if 'dagger' in inventory['backpack']:
    inventory['backpack'].remove('dagger')
inventory['gold'] += 70
print("Từ điển inventory sau khi thực hiện các thay đổi:")
print(inventory)
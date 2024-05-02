inventory = {
 'gold' : 500,
 'pouch' : ['flint', 'twine', 'gemstone'],
 'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}
inventory["key"]= " ['seashell', 'strange berry', 'lint']" # Thêm phần tử


inventory['backpack'].sort()  # Sắp xếp các phần tử


inventory['backpack'].remove('dagger')  # Loại bỏ biến


inventory['gold'] += 50  # Thêm giá trị
print(inventory)










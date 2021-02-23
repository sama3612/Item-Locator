item_dict = {}

def add_item(item_string):
    item_name = item_string[:item_string.find(' -')]
    item_loc = item_string[item_string.find('- ')+2:]
    item_dict[item_name] = item_loc

def find_item(item_name):
    if item_name in item_dict:
        return item_dict[item_name]
    else:
        return None

# Test 1 - Add items to the dict
add_item("banana - fridge")
if "banana" in item_dict and item_dict["banana"] == 'fridge': print("(adding banana to fridge) Test 1 passed!")

# Test 2 - Add item with the same value into the dict
add_item("apple - fridge")
if "apple" in item_dict and item_dict["apple"] == 'fridge': print("(adding apple to fridge) Test 2 passed!")

# Test 3 - find item in dict
if item_dict["apple"] == 'fridge' and item_dict["apple"] == find_item("apple"): print("(locating apple) Test 3 passed!")

# Test 4 - override previous location of item
add_item("apple - trash")
if "apple" in item_dict and item_dict["apple"] == 'trash': print("(changing location of apple) Test 4 passed!")

# Test 5 - find item that has been placed in a new location
if item_dict["apple"] == 'trash' and item_dict["apple"] == find_item("apple"): print("(locating apple) Test 5 passed!")
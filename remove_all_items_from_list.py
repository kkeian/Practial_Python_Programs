# print('which list do you want to remove a word from?:')
# list_with_duplicated_items = input()
# print('enter the word you want to remove from your list:')
# item_to_remove = input()

# erase list literal 'list_with_duplicated_items'
#  and the string literal 'item_to_remove' below,
#  if you want to use the modular version of this program
#  that has been listed above.
#  Note: don't forget to uncomment the 'input version' above

list_with_duplicated_items = ['this', 'this', 'and', 'that', 'and', 'this', 'and', 'that']

item_to_remove = 'this'
for item in list_with_duplicated_items:
    try:
        list_with_duplicated_items.remove(item_to_remove)
        print(list_with_duplicated_items)
    except ValueError:
        break

# this is optional and reminds you what you removed
print('all occurrances of \'' + item_to_remove + '\' have been removed from the'
      ' list.')

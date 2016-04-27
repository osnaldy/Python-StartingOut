def main():

    food = ['pizza', 'burger', 'cake']
    print "Here are the items of your list"
    print food

    item = raw_input("Enter the item in the list to be changed: ")

    try:
        item_index = food.index(item)
        new_item = raw_input("Enter the new item to add to the list: ")
        food[item_index] = new_item

        print "Here is the new list including the changed item"
        print food
    except Exception as err:
        print err
main()
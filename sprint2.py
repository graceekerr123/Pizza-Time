def get_integer(m):
    my_integer = int(input(m))
    return my_integer


def get_string(m):
    my_string = input(m)
    return my_string


def print_list(plist):
    print("Pizza Menu")
    for i in range(0, len(plist)):
        output = "${}0 : {}".format(plist[i][0], plist[i][1])
        print(output)


def print_menu(pmenu):
    print("." * 60)
    for i in range(0, len(pmenu)):
        output = "{}: {}".format(pmenu[i][0], pmenu[i][1])
        print(output)


def print_indexlist(plist):
    print("Pizza Menu")
    print("Index    Cost     Pizza")
    for i in range(0, len(plist)):
        output = "{: <7}: ${}0 - {}".format(i, plist[i][0], plist[i][1])
        print(output)


def ordering(olist, plist):
    print_indexlist(plist)
    run = True
    while run == True:
        type_pizza = get_integer("Please chose the index number for the pizza you would like to order: -> ")
        chosen_type_pizza = plist[type_pizza][1]
        quantity_pizza = get_integer("How many of the {} pizza would you like to order: ->".format(chosen_type_pizza))
        temp_list = [chosen_type_pizza, quantity_pizza]
        olist.append(temp_list)
        output = "You have ordered {} of the {} pizza".format(quantity_pizza, chosen_type_pizza)
        print(output)
        another_pizza = get_string("Would you like to order another pizza? (y/n)-> ")
        if another_pizza == "n":
            return None
        elif another_pizza != "y":
            print("Invalid Entry")


def review_order(olist):
    if len(olist) == 0:
        print("There's nothing in the order yet. Please order something using the 'Order' option in the menu.")
    else:
        print("Here is your order so far:")
        print("Pizza          Amount")
        for i in range(0, len(olist)):
            output = "{: <12} - {}".format(olist[i][0], olist[i][1])
            print(output)


def menu():
    pizza_list = [
        ("18.5", "Cheese"),
        ("18.5", "Pepperoni"),
        ("18.5", "BBQ Chicken"),
        ("18.5", "Vege lovers"),
        ("18.5", "Meatlovers")
    ]

    my_menu = [
        ("P", "See Pizza List"),
        ("O", "Order"),
        ("R", "Review Order"),
        ("Q", "Quit")
    ]

    order = []

    run = True
    while run == True:
        print_menu(my_menu)
        option = get_string("Please enter an option: ->")
        print("." * 60)
        if option == "P":
            print_list(pizza_list)
        elif option == "O":
            ordering(order, pizza_list)
        elif option == "R":
            review_order(order)
        elif option == "Q":
            print("Thank you")
            run = False
        else:
            print("This is not valid")


if __name__ == "__main__":
    menu()
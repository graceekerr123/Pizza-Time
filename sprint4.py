"""This is a pizza ordering program."""
from validationsoption2 import get_one_string2, validate_quantity, validate_index

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
        type_pizza = validate_index("Please chose the index number for the pizza you would like to order: -> ", 0, len(plist)-1, "This is not a valid index number, it is too low. Please enter a larger index number", "This entry is too big and/or too many digits, please try again and enter a smaller index number.")
        chosen_type_pizza = plist[type_pizza][1]
        quantity_pizza = validate_quantity("How many of the {} pizza would you like to order: ->".format(chosen_type_pizza), 1, 30, "Sorry you must order at least one pizza, please order a quantity bigger than 0")
        temp_list = [chosen_type_pizza, quantity_pizza]
        olist.append(temp_list)
        output = "You have ordered {} of the {} pizza".format(quantity_pizza, chosen_type_pizza)
        print(output)
        another_pizza = get_one_string2("Would you like to order another pizza? (y/n)-> ", ["y", "n"])
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

    actualpizza_list = [
        ("18.5", "Cheese"),
        ("18.5", "Pepperoni"),
        ("18.5", "BBQ Chicken"),
        ("18.5", "Vege lovers"),
        ("18.5", "Meatlovers"),
        ("22", "4 Cheese"),
        ("22", )
    ]

    order = [
        ("Cheese", 8)
        ("BBQ Chicken", 2)
        ("Meatlovers", 4)
        ("Pepperoni", 4)
             ]

    run = True
    while run == True:
        print_menu(my_menu)
        option = get_one_string2("Please enter an option: ->", ["P", "O", "R", "Q"])
        print(option)
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
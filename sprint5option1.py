"""This is a pizza ordering program."""
# import validation functions from another file
from validationsoption2 import get_one_string2, validate_quantity, validate_index


def print_list(plist):
    """
    Print pizza list with no index numbers

    :param plist: list (with name and prices of the pizza)
    this is a multidimensional list of [int, str]
    :return: None
    """
    print("Pizza Menu")
    for i in range(0, len(plist)):
        output = "${}0 : {}".format(plist[i][0], plist[i][1])
        print(output)


def print_menu(pmenu):
    """
    Print out the menu options for the user

    :param pmenu: list (with option letter and option description)
    this is a multidimensional list of [str, str]
    :return: None
    """
    print("." * 60)
    # prints out the menu options using a loop
    for i in range(0, len(pmenu)):
        # gets the menu options from the main function using the parameter 'pmenu'
        output = "{}: {}".format(pmenu[i][0], pmenu[i][1])
        print(output)


def print_indexlist(plist):
    """
    Print pizza list with index numbers
    By users, this is known as the menu from which they order from

    :param plist: list (with name and prices of the pizza)
    this is a multidimensional list of [int, str]
    :return: None
    """
    print("Pizza Menu")
    print("Index    Cost     Pizza")
    # prints out the pizza list from which the user can order from
    # it prints out the pizza list with the pizza name, indexes and prices
    for i in range(0, len(plist)):
        output = "{: <7}: ${}0 - {}".format(i, plist[i][0], plist[i][1])
        print(output)


def ordering(olist, plist):
    """
    Get customer's choice of pizza's and number of pizza's they want to order
    The request will loop until the user inputs no

    :param olist: list (user's ordered pizza's and quantities are added to this list)
    this is a multidimensional list of [int, str]
    :param plist: list (with name and prices of the pizza)
    this is a multidimensional list of [int, str]
    :return: None
    """
    # print pizza list with indexes
    print_indexlist(plist)
    # start a loop which will finish when the user doesn't wish to add more pizza's
    run = True
    while run == True:
        # get user choice for the index number from the menu
        type_pizza = validate_index("Please chose the index number for the pizza you would like to order: -> ", 0,
                                    len(plist) - 1,
                                    "This is not a valid index number, it is too low. Please enter a larger index number",
                                    "This entry is too big and/or too many digits, please try again and enter a smaller index number.")
        # get the pizza name from the pizza list using the index entered
        chosen_type_pizza = plist[type_pizza][1]
        # get quantity of the pizza
        quantity_pizza = validate_quantity(
            "How many of the {} pizza would you like to order: ->".format(chosen_type_pizza), 1, 30,
            "Sorry you must order at least one pizza, please order a quantity bigger than 0")
        # collect cost from the pizza list
        cost = plist[type_pizza][0]
        # calculate cost of the pizza order
        order_cost = cost * quantity_pizza
        # create list and then append to the order list
        temp_list = [chosen_type_pizza, quantity_pizza, order_cost]
        olist.append(temp_list)
        # confirmation message
        output = "You have ordered {} of the {} pizza".format(quantity_pizza, chosen_type_pizza)
        print(output)
        # request to add more pizza's
        another_pizza = get_one_string2("Would you like to order another pizza? (y/n)-> ", ["Y", "N"])
        if another_pizza == "N":
            return None
        elif another_pizza != "Y":
            print("Invalid Entry")


def review_order(olist):
    """
    Print all of the pizza's and the quantities that have been ordered so far

    :param olist: list (user's ordered pizza's and quantities are added to this list)
    this is a multidimensional list of [int, str]
    :return: None
    """
    # notifies the user that they haven't ordered yet
    # notifies user that it is necessary to order pizza before reviewing their order
    if len(olist) == 0:
        print("There's nothing in the order yet. Please order something using the 'Order' option in the menu.")
    # prints out the ordered pizza's and quantities for the user
    else:
        print("Here is your order so far:")
        print("Pizza          Amount")
        # prints the customer order list
        for i in range(0, len(olist)):
            output = "{: <12} - {}".format(olist[i][0], olist[i][1])
            print(output)


def receipt(olist):
    totalcost = 0
    totalquantity = 0
    for i in range(0, len(olist)):
        totalcost += olist[i][2]
        totalquantity += olist[i][1]
        output = "{:5} : {:<10} : {:<5} which costs ${}0".format(i, olist[i][0], olist[i][1], olist[i][2])
        print(output)
    output = "You have ordered a total of {} pizzas".format(totalquantity)
    print(output)
    output = "Total Cost: ${}0".format(totalcost)
    print(output)


def menu():
    """
    Loop to run the main option menu
    This is the starting function for the programme

    :return: None
    """
    # (test) main pizza data list
    # it is shorter so it is simpler
    practice_pizza_list = [
        (18.5, "Cheese"),
        (18.5, "Pepperoni"),
        (18.5, "BBQ Chicken"),
        (18.5, "Vege lovers"),
        (18.5, "Meatlovers")
    ]

    # menu option list for the user
    my_menu = [
        ("P", "See Pizza List"),
        ("O", "Order"),
        ("R", "Review Order"),
        ("Q", "Quit")
    ]

    # pizza list
    actualpizza_list = [
        ("18.5", "Cheese"),
        ("18.5", "Pepperoni"),
        ("18.5", "Ham & Cheese"),
        ("18.5", "Vege lovers"),
        ("18.5", "Meatlovers"),
        ("21.5", "Extreme Vege"),
        ("21.5", "BBQ Chicken"),
        ("21.5", "The Italian Pizza"),
        ("21.5", "Mega Meat Lover"),
        ("21.5", "Peri Peri Chicken")
    ]

    order = []

    run = True
    while run == True:
        print_menu(my_menu)
        option = get_one_string2("Please enter an option: ->", ["P", "O", "R", "Q"])
        print(option)
        print("." * 60)
        if option == "P":
            print_list(practice_pizza_list)
        elif option == "O":
            ordering(order, practice_pizza_list)
        elif option == "R":
            review_order(order)
            receipt(order)
        elif option == "Q":
            print("Thank you")
            run = False
        else:
            print("This is not valid")


if __name__ == "__main__":
    menu()
"""This is a pizza ordering program."""
# import validation functions from another file
from validationsoption2 import get_one_string2, validate_quantity, validate_index


def print_list(plist):
    """
    Print pizza list with no index numbers.

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
    Print out the menu options for the user.

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
    Print pizza list with index numbers.

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
    Get customer's choice of pizza's and number of pizza's they want to order.

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
    while run is True:
        # get user choice for the index number from the menu
        message = "Please chose the index number for the pizza you would like to order: -> "
        error_one = "This is not a valid index number, it is too low. Please enter a larger index number"
        error_two = "This entry is too big and/or too many digits, please try again and enter a smaller index number."
        type_pizza = validate_index(message, 0, len(plist) - 1, error_one, error_two)
        # get the pizza name from the pizza list using the index entered
        chosen_type_pizza = plist[type_pizza][1]
        # get quantity of the pizza
        message = "How many of the {} pizza would you like to order: ->".format(chosen_type_pizza)
        error_one = "Sorry you must order at least one pizza, please order a quantity bigger than 0"
        quantity_pizza = validate_quantity(message, 1, 30, error_one)
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


def review_order(olist, o):
    """
    Print all of the pizza's and the quantities that have been ordered so far.

    :param olist: list (user's ordered pizza's and quantities are added to this list)
    this is a multidimensional list of [int, str]
    :return: None
    """
    # declaring two variables as 0
    totalcost = 0
    totalquantity = 0
    # notifies the user that they haven't ordered yet
    # notifies user that it is necessary to order pizza before reviewing their order
    if len(olist) == 0:
        print("There's nothing in the order yet. Please order something using the 'Order' option in the menu.")
    # prints out the ordered pizza's and quantities for the user
    else:
        print("Here is your order so far:")
        print("Item number   Pizza               Amount     Cost")
        # prints the customer order list
        for i in range(0, len(olist)):
            output = "{: <12}  {: <18}  {: <9}  ${}0".format(i, olist[i][0], olist[i][1], olist[i][2])
            print(output)
        if o is True:
            # sum the total cost and quantity
            for i in range(0, len(olist)):
                totalcost += olist[i][2]
                totalquantity += olist[i][1]
            output = "You have ordered a total of {} pizzas".format(totalquantity)
            print(output)
            output = "Total Cost: ${}0".format(totalcost)
            print(output)


def update(olist, plist):
    """
    Update their current order.

    Change the quantity of a pizza order
    Delete a pizza order
    Add more pizza's to the order
    Send the user back to main menu

    :param olist: list (user's ordered pizza's and quantities are added to this list)
    this is a multidimensional list of [int, str]
    :param plist: list (with name and prices of the pizza)
    this is a multidimensional list of [int, str]
    :return: None
    """
    # while loop to give the customer options to update their order
    run = True
    while run is True:
        # limits options in the update menu if user hasn't ordered anything
        if len(olist) == 0:
            # limited update option list for the user
            update_order = [
                ("A", "Add a pizza"),
                ("E", "Exit (Go Back to Main Menu)")
            ]
            available_options = ["A", "E"]
        else:
            # full update option list for the user
            update_order = [
                ("C", "Change Order Quantity"),
                ("D", "Delete a Pizza Order"),
                ("A", "Add a pizza"),
                ("E", "Exit (Go Back to Main Menu)")
            ]
            available_options = ["C", "D", "A", "E"]
        print(50 * "-")
        # print out the update menu options for the user using a loop (using option letter and option description)
        for i in range(0, len(update_order)):
            # get the menu options from the multidimelsional list 'update_order'
            output = "{}: {}".format(update_order[i][0], update_order[i][1])
            print(output)
        # asks user what options they want to chose
        option = get_one_string2("What option would you like? : ", available_options)
        if option == "C":
            print(50 * "-")
            # print out order so far
            review_order(olist, False)
            print("Change Order Quantity:")
            # get item number of pizza to change
            message = "What pizza would you like to update? (please enter the correlating item number)"
            error_one = "This is not a valid item number, it is too low. Please enter a larger item number"
            error_two = "This entry is too big or too many digits, please try again and enter a smaller item number."
            item = validate_index(message, 0, len(olist) - 1, error_one, error_two)
            print("Currently, you have {} {} pizza/s in your order".format(olist[item][1], olist[item][0]))
            message = "How many {} pizzas would you like to order?: ".format(olist[item][0])
            error_one = "Sorry you must have a final order at least one pizza, please order a quantity bigger than 0"
            update_quantity = validate_quantity(message, 0, 30, error_one)
            print("Your order has been updated, now you ordered {} {} pizzas".format(update_quantity, olist[item][0]))
            # update quantity of pizza order
            olist[item][1] = update_quantity
            # update cost for each added pizza order
            olist[item][2] = plist[item][0] * update_quantity
            print(50 * "=")
        elif option == "D":
            print(50 * "-")
            # print out order so far
            review_order(olist, False)
            print("Delete a Pizza Order:")
            # get item number of pizza they want to delete
            message = "Which pizza order would you like to delete? (please enter the correlating item number)"
            error_one = "This is not a valid index number, it is too low. Please enter a larger index number"
            error_two = "This entry is too big or too many digits, please try again and enter a smaller index number."
            delete_item = validate_index(message, 0, len(olist) - 1, error_one, error_two)
            print("Now, you have {} {} pizza/s in your order".format(olist[delete_item][1], olist[delete_item][0]))
            m = "Are you sure you want to remove all {} pizzas in the order? (y/n) ->".format(olist[delete_item][1])
            confirmation = get_one_string2(m, ["Y", "N"])
            if confirmation == "Y":
                # delete list, which correlates to the selected pizza, inside the multidimentional list
                olist.pop(delete_item)
                # prints out order so far, without the deleted pizza
                review_order(olist, False)
                print("You have deleted all {} pizza's off your order".format(olist[item][0]))
            elif confirmation == "N":
                print("Your order has not been updated")
                print("Here is the update menu:")
            else:
                print("Validation Error 303")
            print(50 * "=")
        elif option == "A":
            print(50 * "-")
            # calls the order function so the user can add more pizzas
            ordering(olist, plist)
            print(50 * "=")
        elif option == "E":
            print(50 * "-")
            print("You will now return back to the main menu")
            return None
        else:
            print("Loop Error")
            return None


def menu():
    """
    Loop to run the main option menu.

    This is the starting function for the programme.

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
        ("U", "Update"),
        ("Q", "Quit")
    ]

    # pizza list
    actualpizza_list = [
        (18.5, "Cheese"),
        (18.5, "Pepperoni"),
        (18.5, "Ham & Cheese"),
        (18.5, "Vege lovers"),
        (18.5, "Meatlovers"),
        (21.5, "Extreme Vege"),
        (21.5, "BBQ Chicken"),
        (21.5, "The Italian Pizza"),
        (21.5, "Mega Meat Lover"),
        (21.5, "Peri Peri Chicken")
    ]

    order = []

    run = True
    while run == True:
        print_menu(my_menu)
        option = get_one_string2("Please enter an option: ->", ["P", "O", "R", "U", "Q"])
        print("." * 60)
        if option == "P":
            print_list(actualpizza_list)
        elif option == "O":
            ordering(order, actualpizza_list)
        elif option == "R":
            review_order(order, True)
        elif option == "U":
            update(order, actualpizza_list)
        elif option == "Q":
            print("Thank you")
            run = False
        else:
            print("This is not valid")


if __name__ == "__main__":
    menu()
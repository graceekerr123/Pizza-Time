"""This is a pizza ordering program."""
# import validation functions from another file
from validationsoption2 import get_one_string2, validate_quantity, validate_index, validate_string, validate_number


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
    :param o: bool
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
        return True


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
            print("Now, you have {} {} pizza/s in your order".format(olist[item][1], olist[item][0]))
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


def cancel(olist):
    """
    Clear the order list if user confirms.

    :param olist: list (user's ordered pizza's and quantities are added to this list)
    this is a multidimensional list of [int, str]
    :return: bool
    """
    run = True
    while run is True:
        message = "Are you sure you want to cancel your order? (y/n) -> "
        input = get_one_string2(message, ["Y", "N"])
        # return False to the main function so the loop in the main function repeats
        if input == "Y":
            olist.clear()
            print("Your order has been cancelled.")
            print("Welcome to Pizza Time! Feel free to start your order!")
            return True
        elif input == "N":
            print("Your order has not been cancelled")
            return False
        else:
            print("Validation Error 303")


def details(d):
    """
    Get customer details.

    Asking a series of questions to get all the customers details.

    :param d: list (containing all the details about the customer)
    this is a multidimensional list of [str, str] (ect)
    :return: int (amount of delivery charge)
    """
    if len(d) > 0:
        print("Your previous detail entry will be deleted so you can reenter them")
    # making sure the details list is clear
    # if a customer has already entered details, they will be deleted
    d.clear()
    service_menu = [
        ("P", "Pick up"),
        ("D", "Delivery (a $3 charge)")
    ]
    # program always asks for customer's name
    print("Pizza Time needs your details for your order")
    message = "What is your name? -> "
    name = validate_string(message, 3, 15)
    # give service options
    run = True
    while run is True:
        print("Receive order options:")
        for i in range(0, len(service_menu)):
            output = "{}: {}".format(service_menu[i][0], service_menu[i][1])
            print(output)
            run = False
    message = "Please choice an option: (p/d) -> "
    order_receive = get_one_string2(message, ["P", "D"])
    if order_receive == "P":
        receive = "Pick up"
        print("The pickup option has been selected")
        print("Please pickup at the Wellington Central Branch")
        pickup_information = [("Service", receive),
                              ("Name", name)]
        # the service option and name of customer can be used in other functions
        d.extend(pickup_information)
        # return amount of extra charges
        return 0
    elif order_receive == "D":
        receive = "Delivery"
        message = "Please enter your street name: -> "
        street = validate_string(message, 1, 50)
        message = "Please enter your street number: -> "
        error_one = "Your street number is not valid as it's too small. Enter a number bigger than 0."
        error_two = "Your street number is not valid as it's too big. Enter a number 3 digits or less."
        street_number = validate_index(message, 1, 999, error_one, error_two)
        message = "Please enter your suburb: -> "
        suburb = validate_string(message, 3, 15)
        message = "Please enter your phone number: (XXX XXX XXXX) -> "
        phone_number = validate_string(message, 10, 12)
        print(street)
        print(street_number)
        print(suburb)
        print(phone_number)
        pickup_information = [("Service", receive),
                              ("Name", name),
                              ("Street", "{} {}".format(street_number, street)),
                              ("Suburb", suburb),
                              ("Phone Number", phone_number)]
        # the service option, name, street address and phone number of customer can be used in other functions
        d.extend(pickup_information)
        print("If you want to change your details, please chose the Details option again, and reenter all of them.")
        print(100 * "-")
        # return amount of extra charges
        return 3
    else:
        print("Validation Error 303")


def print_details(d, o):
    """
    Print out customer details.

    :param d: list (containing all the details about the customer)
    this is a multidimensional list of [str, str] (ect)
    :return: None
    """
    if o is True:
        print("Here are your details:")
    for i in range(len(d)):
        output = "{:20} : {:20}".format((d[i][0]), d[i][1])
        print(output)
    print(50 * "-")


def finalise(olist, s, d):
    """
    Finalise the customer's order.

    Asks user to confirm that they want to complete their order
    Loops until it's certain at least one pizza and details have been inputed


    :param olist: list (user's ordered pizza's and quantities are added to this list)
    this is a multidimensional list of [int, str]
    :param s: int (the price of their preferred service (either delivery or pickup))
    :param d:  list (containing all the details about the customer)
    this is a multidimensional list of [str, str] (ect)
    :return: bool
    True or False to determine
    """
    totalcost = 0
    run = True
    while run is True:
        # sum the total cost with pizza order costs and service fee
        for i in range(0, len(olist)):
            totalcost += olist[i][2]
        totalcost += s
        # print customer details
        print_details(d, True)
        print(50 * "-")
        # print the ordered pizza's
        # the second argument is set to False so part of the function doesn't run
        review_order(olist, False)
        print(50 * "-")
        output = "Service charge ={:11} ${:<15.2f}".format(" ", s)
        print(output)
        gst = totalcost * 0.15
        output = "GST(included):{:13} ${:<15.2f}".format(" ", gst)
        print(output)
        output = "Total Cost: {:15} ${:<15.2f}".format(" ", totalcost)
        print(output)
        message = "Are you sure you want to confirm this order? (y/n) -> "
        confirm = get_one_string2(message, ["Y", "N"])
        if confirm == "Y":
            # clears the current customer's order and details to prepare for a new order
            olist.clear()
            d.clear()
            print("Thank you for ordering at Pizza Time :)")
            return True
        if confirm == "N":
            print("Your order is not finalised")
            return False




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
        ("D", "Details"),
        ("C", "Cancel Order"),
        ("F", "Finalise"),
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

    details_list = []

    service_charge = 0

    new_order = True
    run = True
    while run is True:
        if new_order is True:
            print("Welcome to Pizza Time. Please place your order by pressing 'O'")
            # should i also put order = [] here?
            service_charge = 0
            new_order = False
        print_menu(my_menu)
        option = get_one_string2("Please enter an option: ->", ["P", "O", "R", "U", "D", "F", "C", "Q"])
        print("." * 60)
        if option == "P":
            print_list(actualpizza_list)
        elif option == "O":
            ordering(order, actualpizza_list)
        elif option == "R":
            review_order(order, True)
            # when there's nothing in the details list
            if len(details_list) == 0:
                print_details(details_list, False)
            else:
                print_details(details_list, True)
        elif option == "U":
            update(order, actualpizza_list)
        elif option == "D":
            # returns either 0 or 3 depending on if the customer wanted pick up or delivery
            service_charge = details(details_list)
            print_details(details_list, True)
        elif option == "F":
            new_order = finalise(order, service_charge, details_list)
        elif option == "C":
            # notifies the customer if canceling the order is not an option
            # when there's no order, the order cannot be canceled
            if len(order) == 0:
                print("You have no order to cancel")
            else:
                # the return of true/false will determine whether the new_order loop runs
                new_order = cancel(order)
        elif option == "Q":
            print("Thank you")
            run = False
        else:
            print("Your answer is not appropriate, please reenter.")


if __name__ == "__main__":
    menu()

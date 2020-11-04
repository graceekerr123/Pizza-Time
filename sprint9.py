
# OPTION 1
def finalise(olist, s, d):
    run = True
    while run == True
        if len(olist) == 0:
            print("Your order is empty, please order!")
            # is this right?
            return None
        elif len(d) == 0:
            print("Please fill our your details")
            details(details_list)
            print_details(details_list, True)
            # is this right?
            # reloop through
            continue
        else:
            print_details(details_list, True)
            review_order(order, False)
            receipt(________)
            message = "Are you happy to confirm this order? (y/n) -> "
            confirm = get_one_string2(message, ["Y", "N"])
            if confirm == "Y":
                print("Thank you for ordering at Pizza Time :)")

            if confirm == "N":



        else:
            final = validate_y_and_n("This is the current status of your order, are you happy to confirm it? \n"
                                     "Enter 'y' for 'yes' and 'n' for 'no': ", 1, 1)
            # The user confirms their order
            if final in ["Y", "y"]:
                # Confirmation messages
                print("Thank you for shopping with Pizzaroo!!")
                print("Enjoy your pizzas :)")
                # The user's pizza order and information is cleared
                customer_pizzas.clear()
                customer_details.clear()
                # The 'start_new_order' loop repeats
                start_new_order = customer_information(customer_details)
            # The user does not confirm their order
            elif final in ["N", "n"]:
                # Confirmation message
                # No further changes are made
                print("Your order has not been completed.")
            # The user enters an inappropriate answer
            else:
                print("Please enter either 'y' for yes or 'n' for no")



# OPTION 2
if option == "F":
    run = True
    while run == True
        if len(olist) == 0:
            print("Your order is empty, please order!")
            # is this right?
            return None
        elif len(d) == 0:
            print("Please fill our your details")
            details(details_list)
            print_details(details_list)
            # is this right?
            # reloop through
            continue
        else:
            print_details(details_list)
            review_order(order, False)

    if len(olist) == 0:
        print("Your order is empty, start ordering!")
        # is this right?
        return None
    elif len(d) == 0:
        print("Please fill our your details")
        details(details_list)
        print_details(details_list)
        # is this right?
        #reloop through
        continue
    else:
        print_details(details_list)
        review_order(order, False)
        finalise(order, service_charge, details_list)


if option == F:
    finalise(order, service_charge, details_list)








##########################

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


    new_order = True
    run = True
    while run is True:
        if new_order is True:
            "Welcome to Pizza Time. Please place your order by pressing 'O'"
            # WHRE SHOULD I PUT THIS?????
            service_charge = 0
            new_order = False
        print_menu(my_menu)
        option = get_one_string2("Please enter an option: ->", ["P", "O", "R", "U", "D", "C", "Q"])
        print("." * 60)
        if option == "P":
            print_list(actualpizza_list)
        elif option == "O":
            ordering(order, actualpizza_list)
        elif option == "R":
            review_order(order, True)
            # when there's nothing in the deails list
            if details_list == len(0):
                print_details(details_list, False)
            else:
                print_details(details_list, True)
        elif option == "U":
            update(order, actualpizza_list)
        elif option == "D":
            service_charge = details(details_list)
            print_details(details_list, True)
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

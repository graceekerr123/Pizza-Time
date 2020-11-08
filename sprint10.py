def get_one_string2(m, char_list):
    '''
    get a single character input from the user.

    check that the input is part of a passed character list.
    rerequest user input if the input is not acceptable.

    :param m:
    :param char_list: list
    :return:
    '''
    while True:
        user_input = input(m)
        # test for empty string
        if len(user_input) == 0:
            print("You have not entered any value. Please try again.")
            continue
        # preparing the user input before check if it should be accepted
        user_input = user_input.strip()
        user_input = user_input.upper()
        user_input = user_input[0]
        # test if the prepared user of input is in the list that has been passed, via the parametre
        if user_input in char_list:
            # end loop by finishing the function
            return user_input
        else:
            # once error message has been printed the loop will rerun
            print("Your input is not part of the acceptable list, please reenter.")


def duplicate(olist, p):
    for i in range(0, len(olist)):
        # checks to see if the pizza type entered is one of a pizza already ordered
        if p is olist[i][2]:
            message = "You have already ordered {} of this pizza type, would you like to change the quantity ".format(olist[i][1])
            choice = get_one_string2(message, ["Y", "N"])
            if choice is "Y":
                message = "How many {} pizzas would you like to order?: ".format(olist[i][0])
                error_one = "Sorry you must have a final order at least one pizza, please order a quantity bigger than 0"
                update_quantity = validate_quantity(message, 0, 30, error_one)
                olist[i][0] = update_quantity
                print("You now have {} {} pizzas".format(update_quantity, p))
                # end of conditional statement
                return True
            elif choice is "N":
                print("The {} pizzas will not be updated", format(olist[i][0]))
                return False
            else:
                print("Validation Error 303, please try this option again with a appropriate response.")
    # no duplicate found
    return None


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
        scan = duplicate(olist, chosen_type_pizza)
        # if reuturn from scan is true, it prints the dash so it can go loop through again
        if scan:
            print(100 * "-")
        # if no duplicate is found, then continue on with order
        else:
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



# OPTION 1




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











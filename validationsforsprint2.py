def validate_quantity(m, min, max, minerror):
    """
    To ensure a valid integer is returned (when asked for the quantity of pizza)
    tests for inclusive minimum and maximum
    4 arguments string message int min int max string minor error
    it will test the user input comprehensively
    the tests will repeat (go through a loop) until the user has entered an appropriate integer

    :param m: str
    :param min: int
    :param max: int
    :param minerror: str
    :return: int
    """
    while True:
        try:
            user_input = int(input(m))
        except ValueError:
            print("unfortunately your entry is not valid. A whole number is needed, please try again")
            continue
        if user_input < min:
            print(minerror)
            continue
        elif user_input > max:
            sure = get_one_string2("This is a lot of pizza, are you sure you meant to order {} pizzas? (y/n)".format(user_input), ["Y", "N"])
            print(sure)
            if sure == "Y":
                return user_input
            else:
                print("Since you did not mean to enter previously entered quantity, please reenter the quantity of pizza's you want")
                continue
        else:
            return user_input


def validate_index(m, min, max, minerror, maxerror):
    """
    To ensure a valid integer is returned (when the index of the pizza is asked)
    tests for inclusive minimum and maximum
    5 arguments string message int min int max string minor error string max error
    it will test the user input comprehensively
    the tests will repeat (go through a loop) until the user has entered an appropriate integer

    :param m: str
    :param min: int
    :param max: int
    :param minerror: str
    :param maxerror: str
    :return: int
    """
    while True:
        try:
            type_pizza = int(input(m))
        except ValueError:
            print("unfortunately your entry is not valid. A whole number is needed, please try again")
            continue
        if type_pizza < min:
            print(minerror)
            continue
        elif type_pizza > max:
            print(maxerror)
            continue
        else:
            return type_pizza


def get_one_string2(m, char_list):
    '''
    get a single character input from the user
    check that the input is part of a passed character list
    rerequest user input if the input is not acceptable

    :param m:
    :param char_list:
    :return:
    '''
    while True:
        user_input = input(m)
        # preparing the user input before check if it should be accepted
        user_input = user_input.strip()
        user_input = user_input.upper()
        user_input = user_input[0]
        # test if the prepared user of input is in the list that has been passed, via the parameter
        if user_input in char_list:
            # end loop by finishing the function
            return user_input
        else:
            # once error message has been printed the loop will rerun
            print("Your input is not part of the acceptable list, please reenter.")


def validate_integer(m, min, max, minerror, maxerror):
    """
    To ensure a valid integer is returned
    tests for inclusive minimum and maximum
    5 arguments string message int min int max string minor error string max error
    it will test the user input comprehensively
    the tests will repeat (go through a loop) until the user has entered an appropriate integer

    :param m: str
    :param min: int
    :param max: int
    :param minerror: str
    :param maxerror: str
    :return: int
    """
    while True:
        try:
            user_input = int(input(m))
        except ValueError:
            print("unfortunately your entry is not valid. A whole number is needed")
            continue
        if user_input < min:
            print(minerror)
            continue
        elif user_input > max:
            print(maxerror)
            continue
        else:
            return user_input


def validate_integer2(m, min, max, minerror, maxerror, tf):
    """
    To ensure a valid integer is returned
    tests for inclusive minimum and maximum
    6 arguments string message int min int max string minor error string max error bool true/false
    it will test the user input comprehensively
    the tests will repeat (go through a loop) until the user has entered an appropriate integer
    if entry is over max and TRUE then the test will be asks to confirm the entry
    else will ask for a new value if over max

    :param m: str (message)
    :param min: int
    :param max: int
    :param minerror: str
    :param maxerror: str
    :param tf: bool (true: re confirm, false: requests new entry)
    :return: int
    """
    while True:
        try:
            user_input = int(input(m))
        except ValueError:
            print("unfortunately your entry is not valid. A whole number is needed, please try again")
            continue
        if user_input < min:
            print(minerror)
            continue
        elif user_input > max:
            if tf == False:
                print(maxerror)
                continue
            if tf == True:
                sure = get_one_string2("This is a lot of pizza, are you sure you meant to order {} pizzas? (y/n)".format(user_input), ["Y", "N"])
                print(sure)
                if sure == "Y":
                    return user_input
            else:
                print("Since you did not mean to enter previously entered quantity, please reenter the quantity of pizza's you want")
                continue
        else:
            return user_input


pizza_list = [
        ("18.5", "Cheese"),
        ("18.5", "Pepperoni"),
        ("18.5", "BBQ Chicken"),
        ("18.5", "Vege lovers"),
        ("18.5", "Meatlovers")
    ]


if __name__ == "__main__":
    #quantity_index = validate_integer("Please enter your index", 0, len(pizza_list)-1, "This is not a valid index number, it is too low. Please enter a larger index number", "This entry is too big and/or too many digits, please try again and enter a smaller index number.")
    #print(quantity_index)
    #quantity_pizza = validate_integer("Please enter your quantity of pizza", 1, 30, "Sorry you must order at least one pizza, please order a quantity bigger than 0", "There is a max of 30 pizza's per type")
    #print(quantity_pizza)

    #quantity_index = validate_index("Please enter your index", 0, len(pizza_list)-1, "This is not a valid index number, it is too low. Please enter a larger index number", "This entry is too big and/or too many digits, please try again and enter a smaller index number.")
    #print(quantity_index)

    #quantity_pizza = validate_quantity("Please enter your quantity of pizza", 1, 30, "Sorry you must order at least one pizza, please order a quantity bigger than 0")
    #print(quantity_pizza)

    quantity_index = validate_integer2("Please enter your index", 0, len(pizza_list) - 1,
                                    "This is not a valid index number, it is too low. Please enter a larger index number",
                                    "This entry is too big and/or too many digits, please try again and enter a smaller index number.", False)
    print(quantity_index)
    # m, min, max, minerror, maxerror, tf
    message = "Please enter your quantity of pizza"
    min_error="Sorry you must order at least one pizza, please order a quantity bigger than 0"
    max_error = ""
    type_pizza = validate_integer2(message, 1, 30, min_error, max_error, True)
    print(type_pizza)
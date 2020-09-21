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


def validate_quantity(m, min, max, minerror):
    """
    To ensure a valid integer is returned (when asked for the quantity of pizza)
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
            print("unfortunately your entry is not valid. A whole number is needed, please try again")
            continue
        if user_input < min:
            print(minerror)
            continue
        elif user_input > max:
            sure = get_one_string2("This is a lot of pizza, are you sure you meant to order {} pizzas? (y/n)".format(user_input), 1, 1)
            if sure == "y":
                return user_input
            else:
                print("")
                continue
        else:
            return user_input


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
        # test if the prepared user of input is in the list that has been passed, via the parametre
        if user_input in char_list:
            # end loop by finishing the function
            return user_input
        else:
            # once error message has been printed the loop will rerun
            print("Your input is not part of the acceptable list, please reenter.")



if __name__ == "__main__":
    another = validate_string("Would you like to order another pizza? (y/n)-> ", 1, 1)
    print(another)

    menu_option = validate_string("Please enter an option: ->", 1, 1)
    print(menu_option)




if __name__ == "__main__":
    get_one_string2("Please enter item off the menu", ["y", "n"])
    get_one_string2("Please enter item off the menu", ["y", "n"])
    get_one_string2("Please enter item off the menu", ["y", "n"])

    quantity_index = validate_index("Please enter your index", 0, 5, "e1", "e2")
    print(quantity_index)

    quantity_pizza = validate_quantity("Please enter your number", 0, 30, "e1")
    print(quantity_pizza)

    another = validate_string("Would you like to order another pizza? (y/n)-> ", 1, 1)
    print(another)

    another = validate_string("Please enter an option: ->", 1, 1)
    print(another)

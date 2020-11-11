def validate_index(m, min, max, minerror, maxerror):
    """
    To ensure a valid integer is returned (when the index of the pizza is asked).

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
            print(maxerror)
            continue
        else:
            return user_input


def validate_quantity(m, min, max, minerror):
    """
    To ensure a valid integer is returned (when asked for the quantity of pizza).

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
            sure = get_one_string2("This is a lot of pizza, are you sure you meant to order {} pizzas? (Y/N)".format(user_input), ["Y", "N"])
            if sure == "Y":
                return user_input
            else:
                print("")
                continue
        else:
            return user_input


def get_one_string2(m, char_list):
    """
    get a single character input from the user.

    check that the input is part of a passed character list.
    rerequest user input if the input is not acceptable.

    :param m:
    :param char_list: list
    :return: str
    """
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
        # test if the prepared user of input is in the list that has been passed, via the parameter
        if user_input in char_list:
            # end loop by finishing the function
            return user_input
        else:
            # once error message has been printed the loop will rerun
            print("That is not a valid option, please reenter.")


def validate_string(m, min, max):
    while True:
        user_input = input(m)
        if len(user_input) < min:
            print("Your answer is too short. Please type in an appropriate response.")
            continue
        elif len(user_input) > max:
            print("Your answer is too long. Please type in an appropriate response.")
            continue
        else:
            return user_input

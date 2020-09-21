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

def validate_string(m,min, max):
    """
    get user input and tests that the lengths of the string
    is greater than a minimum or less than a maximum
    loops until an acceptable input is received

    :param m: str
    :param min: int
    :param max: int
    :return: str
    """
    while True:
        my_string = input(m)
        if len(my_string) < min:
            print("Your entry is too short. The minimum required characters is {}.".format(min))
        elif len(my_string) > max:
            print("your entry is too many characters")
        else:
            return my_string


def validate_string(m,min, max):
    """
    get user input and tests that the lengths of the string
    is greater than a minimum or less than a maximum
    loops until an acceptable input is received

    :param m: str
    :param min: int
    :param max: int
    :return: str
    """
    while True:
        user_input = input(m)
        if len(user_input) < min:
            print("Your entry is too short. The minimum required characters is {}.".format(min))
        elif len(user_input) > max:
            print("your entry is too many characters")
        else:
            return user_input

#def get_one_string(m, ["y","n","R"]):
    #user_input = user_input.strip().upper()[0]
    #user_input = input(m)
    #user_input = user_input.strip()
    #user_input = user_input.upper()
    #user_input = user_input[0]

if __name__ == "__main__":
    #quantity_fruit = validate_integer("Please enter your number", 0, 20, "e1","e2")
    #print(quantity_fruit)
    type_fruit = validate_string("Please enter a fruit? ->", 3, 30)
    print(type_fruit)

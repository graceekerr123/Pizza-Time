def get_integer(m):
    my_integer = int(input(m))
    return my_integer


def get_string(m):
    my_string = input(m)
    return my_string


def print_list(plist):
    for i in range(0, len(plist)):
        output = "{} : {}".format(plist[i][0], plist[i][1])
        print(output)


def menu():
    pizza_list = [
        ("18.5", "Cheese"),
        ("18.5", "Pepperoni")
    ]

    my_menu = '''
            P: See Pizza List
            Q: Quit
            '''
    run = True
    while run == True:
        print(my_menu)
        option = get_string("Please enter an option: ->")
        print("." * 60)
        if option == "P":
            print_list(pizza_list)
            print("." * 60)
        elif option == "Q":
            print("Thank you")
            run = False
        else:
            print("This is not valid")



if __name__ == "__main__":
    menu()
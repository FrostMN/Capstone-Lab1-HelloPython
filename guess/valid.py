def menu_choice(choice):
    if is_int(choice):
        choice = int(choice)
        if choice > 0 and choice <= 3:
            print("choice is valid")
            return True
        else:
            print("choice is not valid")
            return False
    else:
        print("choice is not a number")
        return False


def guess(numb, min=0, max=100):
    if is_int(numb):
        numb = int(numb)
        if numb > min and numb <= max:
            return True
        else:
            return False
    else:
        return False


def is_int(number):
    try:
        numb = int(number)
        return True
    except:
        return False


if __name__ == '__main__':
    print("main")

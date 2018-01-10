def menu_choice(choice, lower=0, upper=3):
    if is_int(choice):
        choice = int(choice)
        if lower < choice <= upper:
            return True
        else:
            return False
    else:
        return False


def guess(numb, lower=0, upper=100):
    if is_int(numb):
        numb = int(numb)
        if lower < numb <= upper:
            return True
        else:
            return False
    else:
        return False


def is_int(number):
    try:
        int(number)
        return True
    except ValueError:
        return False


if __name__ == '__main__':
    print("main")

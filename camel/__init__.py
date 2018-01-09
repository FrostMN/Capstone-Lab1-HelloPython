
def ask_for_string():
    return input("please enter a string to camelify!")


def camelify(text=""):
    camelfied = ""
    lower_text =  text.lower()
    split_text = lower_text.split(" ")
    for word in split_text:
        camelfied += word[0].upper() + word[1:]
    return camelfied[0].lower() + camelfied[1:]


if __name__ == '__main__':
    string = ask_for_string()
    print(camelify(string))

# don't using regular expression to judge phone number
# which like '415-555-4242'

def isPhoneNumber(num: str) -> bool:
    """
    don't using regular expression to judge phone number
    which like '415-555-4242'

    :param num: 字符串号码
    :return: 字符串是否为电话的真假
    """
    if len(num) != 12:
        return False
    for i in range(3):
        if not num[i].isdecimal():
            return False
    if num[3] != '-':
        return False
    for i in range(4, 7):
        if not num[i].isdecimal():
            return False
    if num[7] != "-":
        return False
    for i in range(8, 12):
        if not num[i].isdecimal():
            return False
    return True


if __name__ == '__main__':
    number = input("Enter the number to see if it conforms to the rules: ")
    print("The number " + number + " is", end="")
    if isPhoneNumber(number):
        print(" a phone number.")
    else:
        print(" not a phone number.")

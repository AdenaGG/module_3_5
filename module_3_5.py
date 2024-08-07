def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if str_number.__len__() > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first


get_multiplied_digits(40203)
result = get_multiplied_digits(40203)
print(result)





def code_string_to_int(code_string):
    [s1, s2] = code_string.split("-")
    return int(s1+s2)


def code_int_to_string(code_int):
    first = int(code_int / 1000)
    second = int(code_int % 1000)
    return "{:02}-{:03}".format(first, second)


def codes_generator(code1, code2):
    first_code = code_string_to_int(code1)
    second_code = code_string_to_int(code2)
    codes_list = []
    
    if (first_code > second_code):
        print("podałeś złą kolejność kodów")
    else:
        for i in range(first_code+1, second_code):
            codes_list.append(code_int_to_string(i))
    return codes_list


if __name__ == "__main__":
    print(codes_generator("79-900", "80-155"))

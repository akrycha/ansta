def code_int_to_string(first, second):
    return "{:02}-{:03}".format(first, second)


def codes_generator(str1, str2):
    first_code_before_separator = int(str1.split("-")[0])
    second_code_before_separator = int(str2.split("-")[0])
    first_code_after_separator = int(str1.split("-")[1])
    second_code_after_separator = int(str2.split("-")[1])
    first_code = int(str1.split("-")[0]+str1.split("-")[1])
    second_code = int(str2.split("-")[0]+str2.split("-")[1])

    codes_list = []
    
    if (first_code > second_code):
        print("podałeś złą kolejność")
    else:
        for i in range(first_code_before_separator, second_code_before_separator+1):
            if i == first_code_before_separator:
                for j in range(first_code_after_separator, 1000):

                        codes_list.append(code_int_to_string(i, j))
            elif i == second_code_before_separator:
                for j in range(0, second_code_after_separator + 1):
                    codes_list.append(code_int_to_string(i, j))
            else:
                for j in range(0, 1000):
                    codes_list.append(code_int_to_string(i, j))

    return codes_list


if __name__ == "__main__":
    print(codes_generator("79-900", "80-155"))

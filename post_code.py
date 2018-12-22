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
                for j in range(first_code_after_separator, 999):
                    if j < 10:
                        codes_list.append(str(i)+"-"+"00"+str(j))
                    elif j in range(10, 100):
                        codes_list.append(str(i) + "-" + "0" + str(j))
                    else:
                        codes_list.append(str(i) + "-" + str(j))
            elif i == second_code_before_separator:
                for j in range(0, second_code_after_separator + 1):
                    if j < 10:
                        codes_list.append(str(i)+"-"+"00"+str(j))
                    elif j in range(10, 100):
                        codes_list.append(str(i) + "-" + "0" + str(j))
                    else:
                        codes_list.append(str(i) + "-" + str(j))
            else:
                for j in range(0, 1000):
                    if j < 10:
                        codes_list.append(str(i)+"-"+"00"+str(j))
                    elif j in range(10, 100):
                        codes_list.append(str(i) + "-" + "0" + str(j))
                    else:
                        codes_list.append(str(i) + "-" + str(j))

    return codes_list


codes_list1 = codes_generator("79-900","80-155")
for el in codes_list1:
    print(el)
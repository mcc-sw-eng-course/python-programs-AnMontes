
def roman(decimal):
    lst_roman = []
    str_roman = ""
    divider = 1
    counter = 0
    counter2 = 0
    lst_charset = ["M", "D", "C", "L", "X", "V", "I", "m", "d", "c", "l", "x", "v", "i"]
    if decimal > 3999999:
        return "Exceeds max."

    if decimal <= 0:
        return "Exceeds min."

    while counter < 11:
        if decimal >= 1000:     # Debido a que I y m ambos valen 1000, hay que desfasarlos.
            counter2 = 0
        else:
            counter2 = 1

        while decimal >= 1000000/divider:
            lst_roman.append(lst_charset[0 + counter + counter2])
            decimal -= 1000000 / divider

        if decimal >= 900000/divider:
            lst_roman.append(lst_charset[2 + counter + counter2])
            lst_roman.append(lst_charset[0 + counter + counter2])
            decimal -= 900000/divider

        if decimal >= 500000/divider:
            lst_roman.append(lst_charset[1 + counter + counter2])
            decimal -= 500000/divider

        while decimal >= 600000/divider:
            lst_roman.append(lst_charset[2 + counter + counter2])
            decimal -= 100000/divider

        if decimal >= 400000/divider:
            lst_roman.append(lst_charset[2 + counter + counter2])
            lst_roman.append(lst_charset[1 + counter + counter2])
            decimal -= 400000/divider

        while decimal >= 100000/divider:
            lst_roman.append(lst_charset[2 + counter + counter2])
            decimal -= 100000/divider

        counter += 2
        divider *= 10

    for x in lst_roman:
        str_roman = str_roman + x

    return str_roman


number = 100.15
print(str(number) + " to roman: " + str(roman(number)))

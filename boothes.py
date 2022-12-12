def booths_algorithm():
    multiplicand_dec = getInput("Mutiplicand")
    multiplier_dec = getInput("Multiplier")
    multiplicand_bin = convertDec(multiplicand_dec)
    multiplier_bin = convertDec(multiplier_dec)
    boothsTriumph(multiplicand_bin, multiplier_bin)
    print("Decimal Result: " + str(int(multiplier_dec)*int(multiplicand_dec)))


def boothsTriumph(mcand, plier):
    print("Multipcand: " + mcand + " Multiplier: " + plier)
    product = "00000000" + plier + "0"
    print("Product: " + product)
    print(buildLine(0, mcand, product))
    for i in range(1, 9):
        operation = product[len(product)-2:]
        product = perform_operation(product, mcand, operation)
        print(buildLine(i, mcand, product))
    product = shift(product)
    product = product[9:17]
    print("Product: " + product)
    return


def perform_operation(product, mcand, operation):
    if operation == "00":
        product = shift(product)
        print("No Op")
        return product
    elif operation == "01":
        temp = binAdd(product[0:8], mcand)
        product = temp + product[8:]
        product = shift(product)
        print("Add")
        return product
    elif operation == "10":
        product = subtraction(product, mcand)
        product = shift(product)
        print("Sub")
        return product
    elif operation == "11":
        product = shift(product)
        print("No Op")
        return product
    else:
        print("An error has occured when choosing operation: Exiting program")
        return 0


def subtraction(product, mcand):
    carry = 0
    prime_product = product[:8]
    final_product = ""
    for i in range(len(prime_product)-1, -1, -1):
        if (mcand[i] == "0" and prime_product[i] == "0"):
            if (carry == 1):
                final_product = "1" + final_product
            else:
                final_product = "0" + final_product
        elif (mcand[i] == "1" and prime_product[i] == "0"):
            if (carry == 1):
                final_product = "0" + final_product
            else:
                final_product = "1" + final_product
                carry = 1
        elif (mcand[i] == "0" and prime_product[i] == "1"):
            if (carry == 1):
                final_product = "0" + final_product
                carry = 0
            else:
                final_product = "1" + final_product
        elif (mcand[i] == "1" and prime_product[i] == "1"):
            if (carry == 1):
                final_product = "1" + final_product
                carry = 1
            else:
                final_product = "0" + final_product
        else:
            print("An error has occurred when subtracting: Exiting program")
            return 0
    return final_product + product[8:]


def shift(product):
    product = "0"+product[:len(product)-1]
    return product


def binAdd(num, num2):
    product = ""
    carry = "0"
    for i in range(len(num)-1, -1, -1):
        if carry == "0":
            if num[i] == "0" and num2[i] == "0":
                product = "0" + product
            elif num[i] == "1" and num2[i] == "1":  # case 1 and 1
                product = "0" + product
                carry = "1"
            else:
                product = "1" + product
        elif carry == "1":
            if num[i] == "0" and num2[i] == "0":
                product = "1" + product
                carry = "0"
            elif num[i] == "1" and num2[i] == "1":  # case 1 and 1
                product = "1" + product
                carry = "1"
            else:
                product = "0" + product
                carry = "1"
    return product


def buildLine(iteration, mcand, product):
    line = "Step: " + str(iteration) + " | Multiplicand: " + mcand + " | Product: " \
        + product[0:8] + " | " + product[8:16] + " | " + product[16]
    return line


def convertDec(dec):
    if int(dec) < 0:
        bin = twos_complement(int(dec))
    else:
        bin = "{0:b}".format(int(dec))
        for i in range(8-len(bin)):
            bin = "0" + bin
    return bin


def getInput(varName):
    boothIn = input('Please enter your ' + varName + ": ")
    while int(boothIn) > 127 or int(boothIn) < -128:
        print("Absolute value too big, please try again")
        boothIn = input('Please enter your ' + varName + ": ")
    return boothIn


def twos_complement(dec):
    adjusted = abs(int(dec) + 1)
    binint = "{0:b}".format(adjusted)
    flipped = flip(binint)
    for i in range(8-len(flipped)):
        flipped = "1" + flipped
    return flipped


def flip(string):
    flipped_string = ""
    for bit in string:
        if bit == "1":
            flipped_string += "0"
        else:
            flipped_string += "1"
    return flipped_string


booths_algorithm()

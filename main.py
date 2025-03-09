def int_to_roman(num):
    roman=""
    if type(num)!= int:

        return "not valid"

    else:

        M=int(num/1000) #1000
        num-=M*1000
        roman+="M"*M

        if num<400:         #100
            C=int(num/100)
            roman="C"*C
        elif 400<=num<500:
            roman += "CD"
        elif 500<=num<900:
            C=int((num-500)/100)
            roman=roman + "D"+"C"*C
        else :
            roman+="CM"
        num-=int(num/100)*100

        if num<40:      #10
            X=int(num/10)
            roman+="X"*X
        elif 40<=num<50:
            roman+="XL"
        elif 50<=num<90:
            X=int((num-50)/10)
            roman=roman + "L"+"X"*X
        else:
            roman+="XC"
    
        num-=int(num/10)*10

        if num<4:
            roman+="I"*num
        elif num==4:
            roman+="IV"
        elif num==5:
            roman+="V"
        elif 9>num>5:
            I=num-5
            roman=roman + "V" + "I"*I
        else:
            roman+="IX"
        return roman

    """
    Convert an integer to a Roman numeral.

    :param num: Integer value between 1 and 3999 inclusive.
    :return: A string representing the Roman numeral of the integer.
    """
print(int_to_roman(3))
print(int_to_roman(58))
print(int_to_roman(400))
print(int_to_roman(1994))
print(int_to_roman(3999))
print(int_to_roman("alallaal"))
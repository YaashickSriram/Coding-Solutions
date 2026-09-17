def sum_of_digits(num):
    string = str(num)

    result = 0
    for ch in string:
        result = result + int(ch)
   
    print(result)

sum_of_digits(1234)
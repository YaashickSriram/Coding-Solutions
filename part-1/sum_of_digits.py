def sum_of_digits(num):
    string = str(num)

    result = 0
    for ch in string:
        result = result + int(ch)
   
    print(result)

sum_of_digits(1234)

def sum_of_digits_using_while(num):
    sum = 0

    while num > 0:
       digit = num%10
       sum += digit
       num //= 10

    print(sum)

sum_of_digits_using_while(12345)
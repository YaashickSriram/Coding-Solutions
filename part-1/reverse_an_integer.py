def reverse_an_integer(num):
    reversed = 0

    while num > 0:
        digits = num%10
        reversed = (reversed * 10) + digits
        num //= 10

    print(reversed)

reverse_an_integer(1234)

        
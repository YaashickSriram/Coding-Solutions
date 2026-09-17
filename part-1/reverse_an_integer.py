def reverse_an_integer(num):

    string = str(num)
    reversed = ""

    for _ in string:
        reversed += string[len(string)-1]
        reversed = string

    print(int(reversed))
reverse_an_integer(12345)
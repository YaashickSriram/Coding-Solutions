def even_or_odd(num: int):
    if num%2 == 0:
        print("Even")
    elif num%2 != 0 and num > 0:
        print("Odd")
    elif num < 0 :
        print ("Negative Number")
    else:
        print("Invalid")

even_or_odd(1)
def smallest_int(a,b,c):
    smallest = a

    if b < smallest:
        smallest = b

    if c < smallest:
        smallest = c

    print(smallest)

smallest_int(1,2,3)
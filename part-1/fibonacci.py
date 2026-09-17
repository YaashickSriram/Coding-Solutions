def fibonnaci(num):
    series = [0,1]

    for i in range(2, num):
        next_set = series[-1]+series[-2]
        series.append(next_set)

    print(series)
fibonnaci(10)

def fibonacci_swap_var(num):
    a,b = 0,1
    for i in range(2,num):
        print(a, end=" ")
        a,b = b,a+b

fibonacci_swap_var(10)
    
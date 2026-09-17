def count_dig(num):
    count = 0

    while num > 0:
        digit = num%10
        count+= 1
        num //=10

    print(count)

count_dig(19760097898)
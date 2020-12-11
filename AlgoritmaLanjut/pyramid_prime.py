def is_prime(n):
    prime = False
    i = 2
    while i <= n:
        if (n % i) == 0 and n == i:
            prime = True
        elif (n % i) == 0:
            break
        i = i + 1
    return prime


def pyramid(t=1, n=2):
    if is_prime(n):
        pyramid_array = [str(n)]
        print " ".join(pyramid_array)
        i = 1
        j = 1
        while i < t:
            prime = False
            while not prime:
                prime = is_prime(n + j)
                j = j + 1
            pyramid_array.append(str(n+j-1))
            print " ".join(pyramid_array)
            i = i + 1


pyramid(5, 2)

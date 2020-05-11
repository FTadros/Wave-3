def shipping(n):
    if n > 1:
        return round((10.95 + 2.95 * (n-1)), 2)
    else:
        return (10.95)

n = int(input("Enter number of items: "))

shipping = str(shipping(n))

print('$' + shipping)
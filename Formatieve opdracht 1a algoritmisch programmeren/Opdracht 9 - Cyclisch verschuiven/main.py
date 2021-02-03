def cyclic(ch=1011000, n=3):
    if n < 1:
        return str(ch)
    else:
        return str(ch)[n:] + str(ch)[:n]

print(cyclic())

def snowball(n, k):
 offset = 0.5
    ray = n/2

    for x in range(n):
        print(k * " ", end="")
        for y in range(n):
            if (x + offset - ray) ** 2 + (y + offset - ray) ** 2 <= ray ** 2:
                print("#", end="")
            else:
                print(" ", end="")
        print()

def snowman(n):
     snowball(n, 2)
    snowball(n + 2, 1)
    snowball(n + 4, 0)

snowman(7)

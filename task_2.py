def chess_board(n, k):
    for i in range(n):
        for _ in range(k):
            print((k * " " + k * "#") * n)
        for _ in range(k):
            print((k * "#" + k * " ") * n)

print(chess_board(4, 2))

def Gener(data, page_size):
    for i in range(0, len(data), page_size):
        yield data[i:i + page_size]


big = list(range(1, 101))
p = Gener(big, 15)

for i in p:
    print(i)

import heapq

stocks = {
    'shampo': 520.54,
    'ris': 20.54,
    'shabon': 50.54,
    'brid': 52.54,
    'lotion': 523.54,
    'pamp': 4520.54,
}
zip_1 = list(sorted(zip(stocks.values(), stocks.keys())))

for x in range(len(zip_1)):
    print(zip_1[0], " ", zip_1[1])

y = [1, 2, 3, 4, 5]
x = iter(y)
while True:
    try:
        j = next(x)
        print(j)
    except StopIteration:
        break


# -----------------------------------------
class Portfloio:
    def __init__(self):
        self.holdings = {}

    def buy(self, ticker, shares):
        self.holdings[ticker] = self.holdings.get(ticker, 0) + shares

    def sell(self, ticker, shares):
        self.holdings[ticker] = self.holdings.get(ticker, 0) - shares

    def __iter__(self):
        return iter(self.holdings.items())


p = Portfloio()
p.buy('Alpha', 15)
p.buy('beta', 23)
p.buy('gama', 9)
p.buy('gama', 20)

for (x,y) in p.__iter__():
    print(x,y)

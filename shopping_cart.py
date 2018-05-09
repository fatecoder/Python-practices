#!/bin/python

class Article(object) :
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

class Stock(object) :
    def __init__(self):
        self.articles_stock = {}

    def add_articles_stock(self, nam, pri, sto) :
        self.articles_stock[nam] = [pri, sto]

    def view_stock(self):
        return self.articles_stock

    def check_articles_stock(self, nam, cant):
        if nam in self.articles_stock and self.articles_stock[nam][1] >= cant :
            self.articles_stock[nam][1] = self.articles_stock[nam][1] - cant
            return True
        else :
            return False

class ShoppingCart(object):
    def __init__(self):
        self.articles = {}

    def add_article(self, nam, cant):
        if nam in self.articles:
            self.articles[nam] = self.articles[nam] + cant
        else:
            self.articles[nam] = cant

    def rem_article(self, nam, cant):
        if nam in self.articles:
            self.articles[nam] = self.articles[nam] - cant
            if self.articles[nam] <= 0:
                del self.articles[nam]

sho_car = ShoppingCart()
stock = Stock()
cookies = Article("Cookies", 3, 10)
soda = Article("Soda", 5, 12)
chips = Article("Chips", 4, 9)
gum = Article("Bubble gum", 1, 50)
donuts = Article("Donuts", 6, 30)
coffee = Article("Coffee", 4, 15)
icecream = Article("Ice cream", 8, 5)

stock.add_articles_stock(cookies.name, cookies.price, cookies.stock)
stock.add_articles_stock(soda.name, soda.price, soda.stock)
stock.add_articles_stock(chips.name, chips.price, chips.stock)
stock.add_articles_stock(gum.name, gum.price, gum.stock)
stock.add_articles_stock(donuts.name, donuts.price, donuts.stock)
stock.add_articles_stock(coffee.name, coffee.price, coffee.stock)
stock.add_articles_stock(icecream.name, icecream.price, icecream.stock)

def buy():
    print "--------------------"
    ans = raw_input("1.- Add Article\n2.- Remove Article\n3.- View My cart\n4.- Finish\n: ")
    if ans.isdigit() :
        if int(ans) is 1:
            art = str(raw_input("Choose an article: "))
            cant = int(raw_input("How many?: "))
            if stock.check_articles_stock(art, cant):
                sho_car.add_article(art, cant)
            else:
                print "Articles insuficient or not exists"
            buy()
        elif int(ans) is 2:
            art = raw_input("Choose an article: ")
            cant = int(raw_input("How many?: "))
            sho_car.rem_article(art, cant)
            buy()
        elif int(ans) is 3:
            print sho_car.articles
            buy()
        elif int(ans) is 4:
            total = 0
            for ks in sho_car.articles:
                total = total + (stock.articles_stock[ks][0] * sho_car.articles[ks])
            print "Total $%i" %total
        else:
            print "Choose a valid option"
            buy()
    else:
        print "Choose a valid option"
        buy()

buy()

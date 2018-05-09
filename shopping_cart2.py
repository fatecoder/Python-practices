#!/bin/python

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

def getArticles():
    f = open("products.txt", "r")
    for li in f:
        n = li[:len(li)-1].split(",")
        stock.add_articles_stock(n[0], int(n[1]), int(n[2]))
    f.close()

def articlesToFile():
    f =  open("list.txt", "a")
    for el in sho_car.articles:
        f.write("%s " %el + "%i " %sho_car.articles[el] + "$%i\n" %stock.articles_stock[el][0] )
    f.write("______________\nTotal: $%i \n###############\n\n" %total())
    f.close()

def updateFile():
    f = open("products.txt", "r+")
    for el in sho_car.articles:
        for li in f:
            if el in li:
                s = li[:len(li)-1].split(",")
                f.write("%i \n" %s[2])

def total():
    total = 0
    for ks in sho_car.articles:
        total = total + (stock.articles_stock[ks][0] * sho_car.articles[ks])
    return total

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
            print "Total: $%i" %total()
            articlesToFile()
        else:
            print "Choose a valid option"
            buy()
    else:
        print "Choose a valid option"
        buy()

sho_car = ShoppingCart()
stock = Stock()

getArticles()
buy()

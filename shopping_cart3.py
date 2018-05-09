#!/bin/python

class Stock(object) :
    def __init__(self):
        self.articles_stock = {}

    def add_articles_stock(self, nam, pri, sto) :
        self.articles_stock[nam] = [pri, sto]

    def check_articles_stock(self, nam, cant):
        if nam in self.articles_stock and self.articles_stock[nam][1] >= cant :
            self.articles_stock[nam][1] = self.articles_stock[nam][1] - cant
            return True
        else :
            return False

    def return_to_stock(self, nam, cant):
        if nam in self.articles_stock:
            self.articles_stock[nam][1] = self.articles_stock[nam][1] + cant

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

def getArticles(sto, arch):
    f = open(arch, "r")
    for li in f:
        n = li[:len(li)-1].split(",")
        sto.add_articles_stock(n[0], int(n[1]), int(n[2]))
    f.close()

def articlesToFile(my_car, sto, fil):
    f =  open(fil, "a")
    for el in my_car.articles:
        f.write("%s " %el + "%i " %my_car.articles[el] + "$%i\n" %sto.articles_stock[el][0] )
    f.write("______________\nTotal: $%i \n###############\n\n" %total(my_car,sto))
    f.close()

def updateFile(sto, fil):
    f = open(fil, "w")
    i = 0
    for el in sto.articles_stock:
        if i != len(sto.articles_stock):
            f.write("%s," %el + "%i," %sto.articles_stock[el][0] + "%i\n" %sto.articles_stock[el][1])
        else:
            f.write("%s," %el + "%i," %sto.articles_stock[el][0] + "%i" %sto.articles_stock[el][1])
        i = i + 1
    f.close()

def total(my_car, sto):
    total = 0
    for ks in my_car.articles:
        total = total + (sto.articles_stock[ks][0] * my_car.articles[ks])
    return total

sho_car = ShoppingCart()
stock = Stock()
getArticles(stock, "products.txt")

def buy(my_car, sto):
    print "--------------------"
    ans = raw_input("1.- Add Article\n2.- Remove Article\n3.- View My cart\n4.- Finish\n: ")
    if ans.isdigit() :
        if int(ans) is 0:
            print sto.articles_stock
            buy(my_car, sto)
        elif int(ans) is 1:
            art = raw_input("Choose an article: ")
            cant = int(raw_input("How many?: "))
            if sto.check_articles_stock(art, cant):
                my_car.add_article(art, cant)
            else:
                print "Articles insuficient or not exists"
            buy(my_car, sto)
        elif int(ans) is 2:
            art = raw_input("Choose an article: ")
            cant = int(raw_input("How many?: "))
            #checar
            sto.return_to_stock(art, my_car.articles[art]-cant)
            my_car.rem_article(art, cant)
            buy(my_car, sto)
        elif int(ans) is 3:
            print my_car.articles
            buy(my_car, sto)
        elif int(ans) is 4:
            print "Total: $%i" %total(my_car, sto)
            articlesToFile(my_car, sto, "list.txt")
            updateFile(stock, "products.txt")
        else:
            print "Choose a valid option"
            buy(my_car, sto)
    else:
        print "Choose a valid option"
        buy(my_car, sto)

buy(sho_car, stock)


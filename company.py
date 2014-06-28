__author__ = 'usucuha'

import random

class Company:
    def __init__(self, name, startingPrice, totalShares, mean, stddeviation):
        self.name = name
        self.price = round(startingPrice, 2)
        self.totalShares = totalShares
        self.mean = mean
        self.stddeviation = stddeviation
        self.lastChange = 2
        self.lastPrice = round(self.price - self.lastChange, 2)

    def nextPrice(self):
        mean = self.lastChange/self.mean
        stdDev = (self.price + self.lastChange)/ (self.stddeviation * 100)
        self.lastChange = round(mean + (stdDev - (random.random() * (stdDev * 2))), 2)
        self.lastPrice = round(self.price, 2)
        self.price = round(self.price + self.lastChange, 2)
        return self.price



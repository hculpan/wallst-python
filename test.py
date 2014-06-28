__author__ = 'usucuha'

import company

if __name__ == "__main__":
    company = company.Company("Boeing Aerospace", 80, 10000)

    for count in range(0, 100):
        newPrice = company.nextPrice()
        print ("New price: %.2f [%.2f]" % (newPrice, company.lastChange))
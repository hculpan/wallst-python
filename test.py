__author__ = 'usucuha'

import concatjsondecoder, json

import company

if __name__ == "__main__":
    print (json.load(open('./test/game.json'), cls=concatjsondecoder.ConcatJSONDecoder))

    company = company.Company("Boeing Aerospace", 80, 10000, 2.5, .5)

    for count in range(0, 100):
        newPrice = company.nextPrice()
        print ("New price: %.2f [%.2f]" % (newPrice, company.lastChange))
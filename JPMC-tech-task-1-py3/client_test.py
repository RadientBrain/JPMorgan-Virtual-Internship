import unittest
from client3 import getDataPoint, getRatio


class ClientTest(unittest.TestCase):
    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
                'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """
        for quote in quotes:
            self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'],
                                                   quote['top_ask']['price'], (quote['top_bid']['price']+quote['top_ask']['price'])/2))

        # prices = {}
        # for quote in quotes:
        #     price = (quote['top_ask']['price'] + quote['top_bid']['price'])/2
        #     prices[quote["stock"]] = price

        # self.assertEqual(getRatio((quotes[0]["top_ask"]["price"]+quotes[0]["top_bid"]["price"])/2,
        #                           (quotes[1]["top_ask"]["price"]+quotes[1]["top_bid"]["price"])/2), (prices['ABC']/prices['DEF']) )

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
                'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """
        for quote in quotes:
            self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'],
                                                   quote['top_ask']['price'], (quote['top_bid']['price']+quote['top_ask']['price'])/2))

        # # self.assertEqual(getDataPoint(quote),dataPoint)
        # # self.assertEqual(1,1)
        # prices = {}
        # for quote in quotes:
        #     price = (quote['top_ask']['price'] + quote['top_bid']['price'])/2
        #     prices[quote["stock"]] = price

        # self.assertEqual(getRatio((quotes[0]["top_ask"]["price"]+quotes[0]["top_bid"]["price"])/2,
        #                           (quotes[1]["top_ask"]["price"]+quotes[1]["top_bid"]["price"])/2), (prices['ABC']/ prices['DEF']) )
        
        
    """ ------------ Add more unit tests ------------ """

    def test_getRatio_priceBZero(self):
            price_a = 142.67
            price_b = 0
            self.assertIsNone(getRatio(price_a, price_b))
            
    def test_getRatio_priceAZero(self):
            price_a = 0
            price_b = 182.32
            self.assertEqual(getRatio(price_a, price_b), 0)
        
    def test_getRatio_greaterThan1(self):
            price_a = 206.98
            price_b = 110.23
            self.assertGreater(getRatio(price_a, price_b), 1)

    def test_getRatio_LessThan1(self):
            price_a = 121.43
            price_b = 310.45
            self.assertLess(getRatio(price_a, price_b), 1)

    def test_getRatio_exactlyOne(self):
            price_a = 498.10
            price_b = 498.10
            self.assertEqual(getRatio(price_a, price_b), 1)
 


if __name__ == '__main__':
    unittest.main()

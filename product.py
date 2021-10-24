from priceType import PriceType

class Product:
    def __init__(self, productId:str, price:float, priceType:PriceType, productName:str):
        self._productId = productId
        self._price = price 
        self._priceType = priceType
        self._productName = productName

    def getproductName(self):
        return self._productName

    def getProductId(self):
        return self._productId     
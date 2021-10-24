from product import Product
import csv

class ProductRegister:

    def __init__(self) :
        self._listOfProducts = []
        self.productInfo=[]
        with open ("productRegister.csv", "r") as file:
            listOfProducts= csv.DictReader(file)
            self.newList=[]
            for row in listOfProducts:
                self.newList.append(row)

    def find(self, productid) -> Product:
        for product in self._listOfProducts:
            if product.getProductId() == productid:
                return product
        return None

    def findProductDetails(self,productId:str)->str:
        i=0
        for product in self.newList:
            i+=1
            for key in product:
                if productId in product[key]:
                    print(product[key],i)
                    self.productInfo=self.newList[i-1]
                    return self.newList[i-1]
            
    def findProductName(self,productId):
        for key in self.productInfo:
            if key=="productName":
                return self.productInfo[key]
        return "No anything"
            #     return self.productInfo[key]
    
    def findProductPrice(self,productId):
        for key in self.productInfo:
            if key=="price":
                return self.productInfo[key]
            #     return self.productInfo[key]  


    def readFromFile(self):
        with open ("productRegister.csv", "r") as file:
            listOfProducts= csv.DictReader(file)
            newList=[]
            for row in listOfProducts:
                newList.append(row)
        return newList


        # läs från fil och stoppa in i listan
        # read from file and store in list

    def saveToFile(self, path:str):
        pass
        # sparar alla i listan till fil
        # saves all in list to file
      
    

# with open ("productRegister.csv", "r") as file:
#     productReg= csv.DictReader(file)

#     for i in productReg:
#         print(i)

#     for i in productReg:
#         if i ["productId"]=="005":
#             print (i)        
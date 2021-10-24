from productRegister import ProductRegister
import datetime


def getInputBetween(startval: int,endval: int)->int:
    while True:
        try:
            val=int(input("Mata in (Enter):"))
            if val >= startval and val <= endval:
                return val
            print(f"Ogiltigt val, mellan {startval} och {endval}, tack")
        except:
            print("Ange ett tal tack!")


def startNewReceipt():
    purchaseGoing=True
    productReg = ProductRegister()
    # print(productReg.readFromFile())
    inventry=productReg.readFromFile()
    time=datetime.datetime.now()
    timeFormated=time.strftime("%Y-%m-%d %H:%M:%S")
    
    print("Kommandon:")
    print("<productid> <antal (nr)>")
    print("PAY")
    
    receipt_list=[]

    total=0
    while purchaseGoing:
        # ProductRegister
        kommando = input("Kommando:")
        if kommando == "PAY":
            for receipt in receipt_list:
                print(receipt)
            print (f"total:{total}")
            purchaseGoing=False
            break
        else:
            parts = kommando.split(" ")
            productId = parts[0]
            amount = int(parts[1])
            productReg.findProductDetails(productId)
            productName=productReg.findProductName(productId)
            print(productName)
            if productName !="No anything":
                print("TESTING")
                price=float(productReg.findProductPrice(productId))
                total+=amount*price
                receipt=f"{productName} {amount} * {price:.2f} = {amount*price:.2f}"
                receipt_list.append(receipt)
                receipt=""   
            else:
                print("Product not found")
                break

        #write receipt to a file

    print("")
    print("KASSA")
    print(f"KVITTO (Receipt) {timeFormated} ")
    productName=productReg.findProductName(productId)
    price=float(productReg.findProductPrice(productId))
    # print(f"{productName} {amount} * {price:.2f} = {amount*price:.2f}")
    for receipt in receipt_list:
        print(receipt)
    



    # product = productReg.find(productId)
    # if product == None:
    #     print("Finns ej (Product does not exist)")
    # else:
    #     print(f"Bra - adding to receipt: {product.getNamn()}")        



while True:
    print("KASSA")
    print("1. New customer)")
    print("0. Avsluta (End)")
    sel = getInputBetween(0,1)
    if sel == 0:
        break
    if sel == 1:
        startNewReceipt()

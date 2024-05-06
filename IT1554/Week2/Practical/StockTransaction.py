shareCount = 2000
buyPrice = 0.4
brokerCommBuy = 0.03 * (shareCount * buyPrice)

sellPrice = float(input("Enter current price for ABC Bank Corporation (S$): "))
brokerCommSell = 0.02 * (shareCount * sellPrice)
totalBrokerComm = brokerCommSell + brokerCommBuy
profit = (sellPrice * shareCount) - totalBrokerComm - (shareCount * buyPrice)
print("You paid total commission of (S$): {0:.1f}".format(totalBrokerComm))
print("You have made a profit of (S$): {0:.1f}".format(profit))


# Oneliner because why not
print("You paid total commission of (S$): {0:.1f}\nYou have made a profit of (S$): {1:.1f}".format(totalComm:=(lambda x, y: x + y)(brokerCommBuy:=0.03*(2000*0.4), brokerCommSell:=0.02*(2000*(sellPrice:=float(input("Enter current price for ABC Bank Corporation (S$): "))))), (sellPrice * 2000 - totalComm - (2000 * 0.4))))


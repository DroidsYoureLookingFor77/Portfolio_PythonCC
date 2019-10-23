#Connor Crowe
#Sales Receipt
numItems = 4
costPerItem = 10.0
taxRate = 0.08
subTotal = numItems * costPerItem
taxAmount = subTotal * taxRate
totalPrice = taxAmount + subTotal
print("Sales Receipt")
print("Number of items" + " : " + str(numItems))
print("Cost per item" + "   : " + "$" + str(costPerItem))
print("Tax rate" + "        : " + str(taxRate))
print("Sub-total" + "       : " + "$" + str(subTotal))
print("Tax amount" + "      : " + "$" + str(taxAmount))
print("Price of sale" + "   : " + "$" + str(totalPrice))

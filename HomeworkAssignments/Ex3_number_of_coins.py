costOfItem = 21
amountPaid = 50
change = (amountPaid - costOfItem)

print("Cost of item:", costOfItem, "kr")
print("Amount paid:", amountPaid, "kr")
print("Change:", change, "kr")

numberOfKr10 = change//10
print("Number of 10 kr coins:", numberOfKr10)

remainder = change%10
#print("remainder:", remainder)

numberOfKr5 = remainder//5
print("Number of 5 kr coins:", numberOfKr5)

remainder = remainder%5
#print("remainder:", remainder)

numberOfKr2 = remainder//2
print("Number of 2 kr coins:", numberOfKr2)

remainder = remainder%2
#print("remainder:", remainder)

numberOfKr1 = remainder//1
print("Number of 1 kr coins:", numberOfKr1)

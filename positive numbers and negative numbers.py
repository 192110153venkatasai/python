list1 = [7,-2,9,-8,-6,-4,10,-1]
pos_count, neg_count = 0, 0
for num in list1:
    if num >= 0:
        pos_count += 1
    else:
        neg_count += 1
print("Positive numbers in the list: ", pos_count)
print("Negative numbers in the list: ", neg_count)

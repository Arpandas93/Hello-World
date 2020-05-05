test = [5, 4, 1, 2, 3]
length = len(test)
positive_index = 0
negative_index = -1


while (positive_index < length):
    print("test[", positive_index, "] =", test[positive_index])
    positive_index += 1

print("****************************")


while(negative_index > (-1 -length)):
    print("test [",negative_index, "] =", test[negative_index])
    negative_index -= 1

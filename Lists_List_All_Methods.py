test = [5, 62, 15, 48, 37]

print("test in the beginning is", test)
print()
#Append
test.append(12)
print("After test.append[12] = ", test)
print("***********************************************")
#Index
print("After we perform test.index(15) =")
print("The index number of = ", 15, "is", test.index(15))
print("***********************************************")
#Count
print(5, "Appears in test for", test.count(5), "time's")
print("***********************************************")
#Extend
test.extend([13, 99])
print("After test.extend([13, 99]) = ", test)
print("***********************************************")
#Sort
test.sort()
print("After the test.sort() = ", test)
print("***********************************************")
#Reverse
test.reverse()
print("After test.reverse()= ",test)
print("***********************************************")
#Clear
test.clear()
print("After the test.clear() = ", test)



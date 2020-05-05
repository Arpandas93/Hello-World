test = [52, 97, 864, 394]

print("test in the beginning is", test)
print()

print("Don't forget that the lists are mutable! so, we can modify them")
print()

del test [-1]
print("After deleting the last number of test, we got", test)

test [0] = "Its Modify"
print("test's this number", test)


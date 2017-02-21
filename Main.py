def testFunc(n, m):
    n = n+m
    return n

test_var = 1
while test_var <=100:
    test_var = testFunc(test_var, 2)
    print(str(test_var))

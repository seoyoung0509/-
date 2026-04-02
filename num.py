i, k, g = 0, 0, ""
for i in range(2,10):
    g = g + ("# %d단 #" % i)
print(g)
for i in range(1,10):
    g = ""
    for k in range(2,10):
        g = g + str("%2dX %2d= %2d" % (k, i, k*i))
    print(g)


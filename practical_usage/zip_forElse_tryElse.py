

y=1
try:
    x = int(y)
except:
    print("error!!!")
else:
    print("finished !")
finally:
    print("done")

print("--------")

arr  = ["a", "b", "c"]
for x in arr:
    if "d" == x:
        print("found")
        break
else:
    print("not found")

x = [1,2,3,4]
y=[5,6,7,8]
x_y = zip(x, y)

# print(list(zip(x, y)))
for (i,j) in x_y:
    print(i, j)

for (i,j) in x_y: #run out of iterators, should be converted to list if want to use more than once
    print(i, j)


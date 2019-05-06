"""
op = ["+","-","*","/"]

for i in range(1000,10000):
    for j in range(len(op)):
        for k in range(len(op)):
            for l in range(len(op)):
                ans = eval(str(i)[0] + j + str(i)[1] + k + str(i)[2] + l + str(i)[3])
                if ans == str(i)[::-1]:
                    print(ans)

"""
def arepalinrome(x, y):
        return str(x) == str(y)[::-1]

op = ['*','']
for num in range(1000,9999):
    if "0" in str(num):
        continue
    for i in op:
        for j in op:
            for k in op:
                val = str(num)[0] + i + str(num)[1] + j +str(num)[2] + k + str(num)[3]
                if len(val) > 4:
                    if arepalinrome(num, eval(val)):
                        print (val + "=" + str(eval(val)))

num = 11
while True:
    if str(num) == str(num)[::-1] and str(bin(num))[2:] == str(bin(num))[2:][::-1] and str(oct(num))[2:] == str(oct(num))[2:][::-1]:
        print(num)
        break
    num += 2

for num in range(100):
    if num > 9:
        if str(num + 1)[1] == '7' or str(num + 1)[0] == '7' or (num + 1) % 7 == 0:
            pass
        else:
            print(num + 1)
    else:
        if num + 1 == 7:
            pass
        else:
            print(num + 1)

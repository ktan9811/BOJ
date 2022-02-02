while(True):
    curin = input()
    if curin == '0':
        break
    res = True
    for i in range(len(curin)//2):
        if curin[i] != curin[-i-1]:
            res = False
            break
    if res:
        print('yes')
    else:
        print('no')
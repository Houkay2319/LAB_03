def Fibonacchi(N):
    if(N < 2):
        return None
        print("Введите число не меньше 2")
    else:
        fibo = [1, 1]
        for i in range(N-2):
            Fn = fibo[i]+fibo[i+1]
            fibo.append(Fn)
    print(fibo)
    return fibo

def Puzirec(a):
    for i in range(len(a) - 1):
        for j in range(len(a) - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a

def Calc(a, b, sign):
    calculator = {
        '+': a+b,
        '-': a-b,
        '*': a*b,
        '/': a/b
    }
    return calculator[sign]
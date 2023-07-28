import sys

def fizzbuzz(N):
    for i in range(1,N+1):
        strg = ""
        if i % 3 == 0:
            strg = strg + "Fizz"
        if i % 5 == 0:
            strg = strg + "Buzz"
        if i % 3 != 0 and i % 5 != 0:
            strg = strg + str(i)
        print(strg)

n = input("What will N, the limit, be? : ")
fizzbuzz(int(n))
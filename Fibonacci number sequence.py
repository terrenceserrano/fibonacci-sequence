#create a program that will display the output of fibonacci sequence

# example of this is 0 1 1 2 3 5 8 13 21 ....
# the number is add before it, link 0 + 1 = 1, then 1 + 1 = 2 etc

from math import *

n = int(input("Enter range of number or fibonacci here: ")) #input from user

n1, n2 = 0, 1 #bale yung index neto is n1 = 0 and n2 = 1
count = 0 #eto yung initial na count ng fibo

if n <= 0: #for positive series
    print("Enter a positive number")
elif n == 1: #for 1 term input
    print("The result is " + n)
else:
    print("Fibonacci sequence are:")
    while count < n: #eto yung block of code na paulit ulit na mag rurun until false, n yung input ng user
        print(n1) #eto kasi yung sa start
        series = n1 + n2 #eto yung main formula nung fibo
        n1 = n2 #equal eto kasi na reretain yung sa pag add ng previous
        n2 = series #eto naman yung para limit na iinput ng user
        count += 1 #increasing from zero, count from zero




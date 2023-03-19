userNumber = int(input('Please enter a number: '))
def collatz(number):
    x = number
    if x % 2 == 0:
        res = x // 2
        print(res)
        return(res)
    elif x % 2 == 1:
         res = 3 * x + 1
         print(res)
         return(res)
userNumber = collatz(userNumber)
while userNumber != 1:
    userNumber = collatz(int(userNumber))


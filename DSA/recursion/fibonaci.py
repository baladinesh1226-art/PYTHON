def PrintNum(n):
    if n == 0:
        return
    PrintNum(n-1)
    print(n)


def fun(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fun(n-1) + fun(n-2)


def SumOfrec(n):
    if n == 0:
        return 0
    return n + SumOfrec(n-1)

def Factorial(n):
    if n == 1:
        return 1
    return n * Factorial(n-1)

def RevSting(s):
    if s == "":
        return ""
    return RevSting(s[1:]) + s[0]


def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def Palindrome(n):
    if len(n) <=1:
        return True
    if n[0] != n[-1]:
        return False

    return Palindrome(n[1:-1])

def print_reverse(n):
    if n <=0:
        return 0
    else:
        print(n)
        print_reverse(n-1)

def sum_digit(n):
    if n <=0:
        return 0
    else:
        num =n %10
        return num + sum_digit(n//10)


def count_digits(n):
    if n <=9:
        return 1
    else:
        return 1+ count_digits(n//10)


def power(x,n):
    if n == 1:
        return n*n
    else:
        return x * power(x,n-1)




# print("print fibonacci number")
# print(fun(5))
# print("======print num using recursion======")
# PrintNum(5)
# print("===== print sum of num =======")
# print(SumOfrec(10))
# print("=====factorial =======")
# # print(Factorial(5))
# s ="madam"
# print(RevSting(s))
# print(s," is Palindrome or not:",Palindrome(s))
# print(rev_string(s))
num=394829834940
print("sum of digit:",sum_digit(num))
print("count of digits:",count_digits(num))
print(power(2,5))

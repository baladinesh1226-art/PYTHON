try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    c = a/b
    print(c)
except ZeroDivisionError:
    print("Division by zero")
except ValueError:
    print("Invalid input")


# list index error

try:
    lst =[1,2,3]
    index = int(input("Enter a number: "))
    print(lst[index])
except IndexError:
    print("Index out of range")


try:
    num= int(input("enter value: "))
    result = 100/num
    print(result)

except (ValueError, ZeroDivisionError):
   print("Invalid input or division by zero")

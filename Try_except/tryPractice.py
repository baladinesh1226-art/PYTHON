# #program using while and try
#
# while True:
#     try:
#         number = int(input("Enter a number: "))
#         print("you entered :",number)
#         break
#     except (ValueError):
#         print("Invalid input")
#         continue
#
# atmpin = 9876
# balance = 79243829
# coutnt =3
#
# try:
#     while coutnt > 0:
#         pin = int(input("Enter your atm pin:"))
#         if pin == atmpin:
#             print("your available balance:", balance)
#             break
#         else:
#             coutnt -= 1
#             print(f"invalid input you only have {coutnt} attempts")
# except Exception as e:
#     print("got some error:",e)


while True:
    try:
        value = int(input("Enter num one:"))
        value2 = int(input("Enter num two:"))
        simple = input("Enter a simple like + , -,*,/")
        if simple == "+":
            print("the added value is:", value + value2)
        elif simple == "-":
            print("the subtract value is:", value - value2)
        elif simple == "*":
            print("the  multiply value:", value * value2)
        elif simple == "-":
            print("the devision value is:", value / value2)

    except Exception as e:
        print("error accured:", e)

    con = input("do you want to continue(type y/n):").lower()
    if con == 'y':
        continue
    elif con == 'n':
        break



from tensorflow.python.keras.utils.conv_utils import conv_output_length

 #revernum
def revernum(num):
    ans =0
    while num >0:
        value = num % 10
        ans = ans*10 + value
        num =num //10
    return ans

#palindrom
def palindrome(num):
    original = num
    ans = 0
    while num > 0:
        val = num % 10
        ans = (ans * 10) + val
        num = num // 10

    return original == ans


#digit count
def degitCout(num):
    count =0
    while num >0:
        num //=10
        count+=1
    return count

inpt = 123454321
print("Is this number a palindrome?", palindrome(inpt))
print("Is this number a degit?", degitCout(inpt))



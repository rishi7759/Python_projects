
import math , random



def generateotp() :
    list = "0123456789"
    otp = ""

    for i in range(4):
     otp += list[math.floor(random.random() * 10)]

    return otp


print("otp of 4 digits is :", generateotp())



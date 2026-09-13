
user = input("enter your name : ")
print(user)

dob, roll = input("enter dob and roll..").split()
print("\n")

print("*** 5 QUESTIONS ARE THERE ***")
print("\n")

print("Q1 > what is your name ? ")
print("  1> rishikesh")
print("  2> prachi")
print("  3> aryan")
print(f"  4> {user}")

choice = int(input("Choose your ans : "))

if user == "rishikesh" and choice == 1:
    print("ans 1 is correct")

elif user == "prachi" and choice == 2:
    print("ans 2 is correct ")

elif user == "aryan" and choice == 3:
    print("ans 3 is correct ")

elif user == f"{user}" and choice == 4:
    print("yep .....")

else:
    print("wrong user entered nikalo usko yaha seee..")

print("\n")

print("Q2 > what is your roll ? ")
print("  1> 246059")
print(f"  2> {roll}")
print("  3> 246081")
print("  4> 246066")



choic = int(input("Choose your ans : "))
if user == "prachi" and choic == 1:
    print("hn tera he roll hai sahi pakadi hai ")

elif roll == f"{roll}" and choic == 2:
    print("yes it's your roll......")

elif user == "aryan" and choic == 3:
    print("sahi hai yaad hai tmko tera roll")

elif user == "rishikesh" and choic == 4:
    print("hn mera v yaad hai ")

else:
    print("TU AVU TK GAYA NHI H REHHH NIKL YAHA SEEE....")

print("\n")

print("Q3 > who teaches you python ")
print("1> alok sir")
print("2> ankit sir")
print("3> jyoti mam ")
print("4> all of above")


choi = int(input("Choose your ans : "))
if choi == 3:
    print("ans 3 is correct")

else:
    print("wrong answer..")

print("\n")
print("Q4 > when is your B.DAY ?")
print("  1> 4th april")
print("  2> 2 july")
print(f"  3> {dob}")
print("  4> 23rd sept")



ch = int(input("Choose your ans : "))
if user == "prachi" and ch == 1:
    print("4 footiya ka b.day koi nhi bhulta haiiiii ")

elif user =="aryan" and ch == 2:
    print("wahh beta yaad hai b.day")

elif user == "rishikesh" and ch == 4:
    print("aacha hai yaad hai ")

elif dob == f"{dob} " and ch == 3:
    print("sahi date hai aapkaaa  ")

else:
    print("wrong answer..")

print("\n")

print("Q5 > who is user  ? ")
print("  1> prachi")
print(f"  2> {user}")
print("  3> rishikesh")
print("  4> aryan")



c = int(input("Choose your ans :  "))
if user == "prachi" and c == 1:
    print("hn hn tera he account hai tmhi user hoo")

elif user == "rishikesh" and c == 3:
    print("hn bhai tmhi user hai tera he code haii ")

elif user == "aryan" and c == 4:
    print("hn mithu bhai tmhi hooo")

elif user == f"{user}" and c == 2:
    print("hn hn tmhi user hooo ")

else:
    print("wrong user nikl saala tuuuu..")

print("\n")
print("\n")

print("TASK COMPLETED.....")







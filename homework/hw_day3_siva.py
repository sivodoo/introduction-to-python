# Homework - Day3 - Sivakumar
#
# Question
#
usnam = "Peng2021"
pwd = "@124abc"

get_un = input("Please enter your username...")
get_pw = input("Please enter your password...")

if usnam != get_un :
    print("User name is incorrect...")
elif pwd != get_pw :
    print ("Password is not matching...")
else :
    print ("Succesful login...")

# Extra
#
dict = {"Peng2021":"@124abc", "Sher0789":"()$$Tig"}

get_un = input("Please enter your username...")
get_pw = input("Please enter your password...")

if get_un not in dict.keys() :
    print("User name is incorrect...")
elif pwd != dict[get_un] :
    print ("Password is not matching...")
else :
    print ("Succesful login...")

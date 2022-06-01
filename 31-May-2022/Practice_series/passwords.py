
print("A good password should be at least 10 characters and should have # in it")

pwd = input("Enter a password => ")


if len(pwd) >= 10 and pwd.find("#") != -1:
    print("You have done a great job!")
else:
    print("This password is too short or does not have #")


# let's write the reverse condition

if len(pwd) < 10 or pwd.find("#") == -1:
    print("This password is too short or does not have #")
else:
    print("You have done a great job!")


# Different rules for password

print("Either have a super long password, 12+ characters, great password")
print("If you have a password 8-11 character but with a # symbol, that is ok password")

print()
print()
if len(pwd) >= 12:
    print("You have a very strong password")
elif len(pwd) >= 8 and pwd.find('#') != -1:
    print("You have an acceptable password")
else:
    print("You have a weak password")

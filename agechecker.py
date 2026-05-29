age = int(input("Enter your age: "))
if age < 0:
    print("You've entered an invalid age")
elif age > 10 and age < 20:
    print("You are a inbetween 10 and 20 years old")
    if age >10 and age < 18:
        print("You are a teenager")
    print("You can enter the class")
elif age > 0 and age < 10:
    print("You are a child")
    print("You are too young to enter the class")
else: 
    print("You are an adult")
    print("You are too old to enter the class")

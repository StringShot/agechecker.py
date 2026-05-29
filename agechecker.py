age = int(input("Enter your age: "))
if age < 0:
    print("You've entered an invalid age")
elif age > 10 and age < 20:
    print("You are a inbetween 10 and 20 years old")
    if age >10 and age < 18:
        print("You are a teenager")
elif age > 0 and age < 10:
    print("You are a child")
else: 
    print("You are an adult")
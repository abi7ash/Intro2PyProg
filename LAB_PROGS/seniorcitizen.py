#program to check whether a person is senior citizen
name = input("Enter the name of the person : ")
#age = int(input("Enter the age of the person : "))
print('Enter year of birth')
yob = input()

age = (2023 - yob)
if (age >= 60) :
    print("The person by name "+ name +" is a senior citizen")
else :
    print("The person by name "+ name +" is not a senior citizen")
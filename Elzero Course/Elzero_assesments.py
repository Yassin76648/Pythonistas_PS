""" 
this file is the solutions of Elzero assesments
in python course
""" 
from random import random
import email
name = 'Yassin'
age = "21"
country= 'sudan'

print(f' "Name : {name}"\n "Age : {age}"\n "Country : {country}"')
result = "My name is " + name +", My age is "+ age +", I'm from :"+country
print(result)

print(type(name))
print(type(age))
print(type(country))

result = "Hello "+ "'" +name+"'," +"How you doing \ " + '""" + '+" Your age is " +'"'+age+'"'+'"'+" Your country is : "+country
print(result)

result = "Hello "+ "'" +name+"'," +"How you doing \ \n" + '""" + '+" Your age is " +'"'+age+'"'+'"\n'+" Your country is : "+country
print(result)


name ="Elzero" 

print(f'Second Letter Is : {name[1:2]} \nThird Letter is : {name[2]}\nLast Letter Is :{name[-1]}')

print(f'{name[1:4]}')
print(f'{name[0:5:2]}')
print(f'{name[::-1][1:6:2]}')


name = "#@#@Elzero#@#@"
print(name.strip("#@"))


# num = "9"
# num = "15"
num = "130"
# num = "950"
# num = "1500"

print(num.zfill(4))

name_one = "Osama"
name_two = "Osama_Elzero"

print(name_one.rjust(20,"@"))
print(name_two.rjust(20,"@"))

name_one = "OSamA"
name_two = "osaMA"

print(name_one.swapcase())
print(name_two.swapcase())

msg = "I Love Python And Although Love Elzero Web School"

print(msg.count("Love"))


name = "Elzero"
print(name.index("z"))

msg = "I <3 Python And Although <3 Elzero Web School"

print(msg.replace("<3","Love", 1))

msg = "I <3 Python And Although <3 Elzero Web School"

print(msg.replace("<3","Love"))


name = "Yassin"
age = 21
country = "Sudan"

print(f"My Name is {name} I'm {age} Years Old, I'm from {country}")

print(type(10))
print(type(1.23))
print(type(1+5j))

num = 1+2j

print(num.real)
print(num.imag)

num = 10

print(f'{float(num): .10f}')

num = 159.650

print(f'{int(num)}\n{type(int(num))}')

# 100 - 115 = -15
# 50 * 30 = 1500
# 21 % 4 = 1
# 110 // 11 = 10
# 97 // 20 = 4


friends =['Yassin', 'Osama', 'Ali', 'Osman', 'Taha']

print(friends[0])
print(friends[-5])
print(friends[4])
print(friends[-1])


print(friends[0::2])
print(friends[1::2])

friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

print(friends[1:4])
print(friends[-2:])
friends[-1]='Elzero'
friends[-2]='Elzero'
print(friends)

friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

friends.insert(0,"Nasser")
friends.append("Salem")
print(friends)
friends.remove('Nasser')
friends.remove('Osama')
print(friends)

friends.pop()

print(friends)


friends = ["Ahmed", "Sayed"]
employees = ["Samah", "Eman"]
school = ["Ramy", "Shady"]

# Needed Output
# ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]

result = friends+employees+school
print(result)

friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]

# Needed Output
# ['Ahmed', 'Eman', 'Ramy', 'Samah', 'Sayed', 'Shady']
# ['Shady', 'Sayed', 'Samah', 'Ramy', 'Eman', 'Ahmed']

friends.sort()
print(friends)
friends.reverse()
print(friends)

print(len(friends))


technologies = ["Html", "CSS", "JS", "Python", ["Django", "Flask", "Web"]]

# Needed Output
# Django
# Web
print(technologies[-1][0])
print(technologies[-1][-1])


name = 'yassin',
# Needed Output

# "Osama"
# <class 'tuple'>
print(name[0])
print(type(name))

friends = ("Osama", "Ahmed", "Sayed")

# Needed Output

# ("Elzero", "Ahmed", "Sayed")
# <class 'tuple'>
# 3 Elements
friends_list = list(friends)
friends_list[0] = 'Elzero'
friends = tuple(friends_list)
print(friends)
print(type(friends))
print(len(friends))


nums = (1, 2, 3)
letters = ("A", "B", "C")

# Needed Output

# nums_and_letters_one = (1, 2, 3, "A", "B", "C")
# 6 Elements

nums_and_letters_one =nums +letters
print(nums_and_letters_one)
print(len(nums_and_letters_one))


my_tuple = (1, 2, 3, 4)

# Needed Output

# 1
# 2
# 4
a, b, _, c, = my_tuple
print(a)
print(b)
print(c)


my_list = [1, 2, 3, 3, 4, 5, 1]
# Needed Output

# 1, 2, 3, 4, 5
# <class 'list'>
# 1, 2, 3, 4

unique_list = (set(my_list))
my_list = list(unique_list)
print(my_list)
print(type(my_list))
print(my_list[0:-1])


nums = {1, 2, 3}
letters = {"A", "B", "C"}

# Needed Output

# {1, 2, 3, "A", "B", "C"}
# {1, 2, 3, "A", "B", "C"}
# {1, 2, 3, "A", "B", "C"}
print(nums.union(letters))
print(nums | letters)
nums_copy = nums.copy()
nums_copy.update(letters)
print(nums_copy)


my_set = {1, 2, 3}
letters = {"A", "B", "C"}

# Needed Output

# {1, 2, 3}
# set()
# {"A", "B"}
print(my_set)
my_set.clear()
print(my_set)
my_set.add("A")
my_set.add("B")
print(my_set)

set_one = {1, 2, 3}
set_two = {1, 2, 3, 4, 5, 6}

# Needed Output

print(set_two.issuperset(set_one))


dictionary = {'Html' : "30%", 'CSS':"20%", "python":"70%", "AI":"10%"}

print(f'HTML Progress is  {dictionary['Html']}' )
print(f'CSS Progress is  {dictionary['CSS']}' )
print(f'python Progress is  {dictionary['python']}' )
print(f'AI Progress is  {dictionary['AI']}' )

dictionary['Web'] = "40%"
print(f'Web Progress is  {dictionary['Web']}' )


print(bool(5))
print(bool("hello"))
print(bool([1, 4]))
print(bool({2, 4}))
print(bool(""))
print(bool(0))
print(bool([]))
print(bool({}))

html = 80
css = 60
javascript = 70

# Needed Output

print(bool(html>50 and css>50 and javascript>50))


num_one = 10
num_two = 20
num = 20

# Needed Output
print(bool(num > num_one or num > num_two))
print(bool(num > num_one and num > num_two))




num_one = 10
num_two = 20

# Needed Output
result = num_one + num_two
print(result)
result2 = pow(result,3)
print(result2)
result3 = result2%26000
print(result3)
print(float(result3/5))
print(type(str(float(result3/5))))

# name = input("Enter Your Name :")
# print("Hello ", name.strip().capitalize(), "Happy to see you here")


# age = int(input("Enter Your age ... :"))
# if age < 16 :
#    print("Hello Your Age Is Under 16, Some Articles Is Not Suitable For You")
# else:
#   print("Hello Your Age Is ", age ," All Articles Is Suitable For You")

# f_name = input("First Name : ")
# l_name = input("Last Name : ")
# print("Welcome ", f_name.strip().capitalize() , l_name.strip().capitalize()[0], "")


# u_email = input("Enter Your Email : ")
# pure_email = u_email.strip().lower()
# name_identfier = pure_email.index("@")
# domain_dot = pure_email.index(".")
# print("your Name Is ", pure_email[:name_identfier].capitalize())
# print("Email Service Provider : ", pure_email[name_identfier+1:domain_dot])
# print("Email Service Provider : ", pure_email[domain_dot+1:])



# num1 = int(input("Enter first num: ").strip())
# num2 = int(input("Enter Second num: ").strip())

# opration = input("Enter the oprator :").strip()

# if opration=="*":
#     result= num1*num2
# elif  opration=="+":
#    result= num1+num2
# elif opration=="-":
#    result= num1-num2
# elif opration=="÷":
#    result= num1/num2
# print(result)

age = 17

result = "You allowed to visit" if age >18 else "You'r not allowed to visit"
print(result)


# age = int(input("Enter Your age : ").strip())

# if age > 10 and age <100 :
#    age_delta = 2025 - age
#    print("You was born in ", 2025 - age)
#    print("Your age in Years =", age)
#    print("Your age in months =", age*12 )
#    print("Your age in weeks = ", age*52)
#    print("Your age in Days =", age*356)
#    print("Your age in hours =", age*356*24 )
#    print("Your age in mintues =", age*356*24*60 )
#    print("Your age in seconds =", age*356*24*60*60 )


# countries = ["Egypt", "Palestine", "Syria", "Yemen", "KSA", "USA", "Bahrain", "England"]
# discount = 30
# country = input("Enter Your country : ").strip().capitalize()
# price = 100

# if country in countries:
#     print("Your Country is", country , "is Eligible For Discount And The Price After Discount Is $",  price-discount)
# else:
#     print("Your Country is", country , "is not Eligible For Discount And The Price Is $",  price)


# num = int(input("Enter Your Number... "))

# if not str(num).isdigit() and num < 0 :
#     print("Your number is not digit or < 0  ") 
# else :
#     count = 0
#     i = 1
#     while(num != i) :
#         num = num-1
#         if num == 6:
#             continue
#         print(num)
#         count = count+1

#     print(count,  "Numbers Printed Successfully.")


# friends = ["Mohamed", "Shady", "ahmed", "eman", "Sherif"]
# i = 0
# count =0 
# while i < len(friends):
#     if friends[i][0].islower() :
#         count +=1
#         i +=1
#         continue
#     print(friends[i])
#     i +=1

# print("Friends Printed And Ignored Names Count Is ", count)


# Code
skills = ["HTML", "CSS", "JavaScript", "PHP", "Python"]

while skills:
    print(skills.pop(0))


# my_friends = []
# count =0
# while len(my_friends) < 4:
#     name = input("Enter the name you want to add ")
#     if name.isupper() :
#         print("Sorry this name is unacceptable")
#     elif name.islower():
#         name = name.capitalize()
#         my_friends.append(name.strip())
#         count +=1
#         print("Name Capitalized", name)
#         print("You have ", 4-count, "names left to insert")

#     elif name[0].isupper():
#         my_friends.append(name.strip())
#         count +=1
#         print("You have ", 4-count, "names left to insert")
#     else:
#         print("Finished")

# print("List", my_friends)


# Input
my_nums = [15, 81, 5, 17, 20, 21, 13]

# Needed Output
"1 => 20"
"2 => 15"
"3 => 5"
"All Numbers Printed"
count =0
sorted_list = sorted(my_nums, reverse=True)
for  i in sorted_list:
    if i%5 == 0:
        print(count+1 ," => ", i)
        count+=1
print("All Numbers Printed")

for i in range(0,21):
    if i == 6 or i == 8 or i == 12:
        continue
    if i < 10 :
        print(f"0{i}")
    else:
        print(i)
print("All Numbers Printed")


# Input
my_ranks = {
    'Math': 'A',
    "Science": 'B',
    'Drawing': 'A',
    'Sports': 'C'
}

# Needed Output
"My Rank in Math Is A And This Equal 100 Points"
"My Rank in Science Is B And This Equal 80 Points"
"My Rank in Drawing Is A And This Equal 100 Points"
"My Rank in Sports Is C And This Equal 40 Points"
"Total Points Is 320"
dic = {
    "A" : 100 , 
    "B": 80 , 
    "C": 40
}
sum =0
for i in my_ranks:
    sum += dic[my_ranks[i]]
    print(f"My Rank in {i} Is {my_ranks[i]} And This Equal {dic[my_ranks[i]]} Points")
print(f"Total Points Is {sum}")



# Input
students = {
  "Ahmed": {
    "Math": "A",
    "Science": "D",
    "Draw": "B",
    "Sports": "C",
    "Thinking": "A"
  },
  "Sayed": {
    "Math": "B",
    "Science": "B",
    "Draw": "B",
    "Sports": "D",
    "Thinking": "A"
  },
  "Mahmoud": {
    "Math": "D",
    "Science": "A",
    "Draw": "A",
    "Sports": "B",
    "Thinking": "B"
  }
}
rank = {
    'A':100,
    'B':80,
    'C':40,
    'D':20,
}


for student in students:
    print(f'''"------------------------------"
"-- Student Name => {student}"
"------------------------------"''')
    total = 0
    for subject in students[student]:
        print(f"{subject} ==> {rank[students[student][subject]]} Points")
        total+= rank[students[student][subject]]
    print(f"Total Points for {student} is {total } ")



# Needed Output
"------------------------------"
"-- Student Name => Ahmed"
"------------------------------"
"- Math => 100 Points"
"- Science => 20 Points"
"- Draw => 80 Points"
"- Sports => 40 Points"
"- Thinking => 100 Points"
"Total Points For Ahmed Is 340"
"------------------------------"
"-- Student Name => Sayed"
"------------------------------"
"- Math => 80 Points"
"- Science => 80 Points"
"- Draw => 80 Points"
"- Sports => 20 Points"
"- Thinking => 100 Points"
"Total Points For Sayed Is 360"
"------------------------------"
"-- Student Name => Mahmoud"
"------------------------------"
"- Math => 20 Points"
"- Science => 100 Points"
"- Draw => 100 Points"
"- Sports => 80 Points"
"- Thinking => 80 Points"
"Total Points For Mahmoud Is 380"


for student in students:
    print(f'''"------------------------------"
"-- Student Name => {student}"
"------------------------------"''')
    for subject, grade in students[student].items():
        print(f"{subject} ==> {rank[grade]} Points")
    print(f"Total Points for {student} is {total } ")



def calculate(num1, num2, opration):
    if opration == "add" or opration == "a":
        return  num1 + num2
    elif opration == "subtract" or opration== "s":
        return num1 - num2
    elif opration == "multiply" or opration==  "m":
        return num1 * num2
    else:
        return "Sorry , Invalid Opration"

# num1 = int(input("Enter The First Number : "))
# num2 = int(input("Enter The Second Number : "))
# opration = input("Type The the Opration (add, subtract, multiply) or the first letter of the opration (a, s, m) : ").lower()

# print(calculate(num1, num2, opration))


def addition(*nums):
    sum =0
    for i in nums:
        sum = sum +i 
    return sum

print(addition(6,7))   


def show_skills(name, *skills):
    print (f"Hi {name}  Your Skills are")
    for skill in skills:
        print (f"- {skill}")


show_skills("Yassin", "HTML", "CSS", "JS", "Python")


def say_hello(**kwargs):
    name = kwargs.get("name", "Unknown")
    age = kwargs.get("age", "Unknown")
    country = kwargs.get("country", "Unknown")

    print(f"Hello {name}, Your Age Is {age}, You Live In {country}")
    

say_hello(name="Yassin", age=21, country="Sudan")


def get_score(**kwargs):
    for i in kwargs:
        print(f"{i} => {kwargs[i]}" )

get_score(Math=90, Science=80, Language=70)



def get_people_scores(*name, **kwargs):
    if name and kwargs:
        print(f"Hello {name[0]} This Is Your Score Table:")
        for i in kwargs:
            print(f"{i} => {kwargs[i]}" )
    elif name and not kwargs :
        print(f"Hello {name[0]} You have no score tables")
    elif not name and kwargs:
        for i in kwargs:
            print(f"{i} => {kwargs[i]}" )
get_people_scores(Logic=70, Problems=60)




def get_the_scores(name = None, **score):
    if name and score :
        print(f"Hello {name} This Is Your Score Table:")
        for i in score:
            print(f"{i} => {score[i]}" )
    elif name and not score :
        print(f"Hello {name} You have no score tables")
    elif score and not name:
        for i in score:
            print(f"{i} => {score[i]}" )

scores = {
    "Math" : 90,
    "Scince" : 80,
    "Language" :70,
}
get_the_scores("Osama", **scores)



import os

path = r"C:\Users\dell\Desktop\Python"

# file = open(os.path.join(path, "assign.py"),"w").close()

# for i in range(1, 51):
#     if i == 25:
#         name25 = "Special_text.txt"
#         open(os.path.join(path, name25), "w").close()
#     else:
#         name = f"txt{i}.txt"
#         file_path = os.path.join(path, name)
        
#         with open(file_path, "w") as file:
#             file.write(f"Elzero Web School =>{i}")


print(os.getcwd())
print(os.path.dirname(__file__))
print(os.path.basename(__file__))

python_folder = os.path.dirname(os.path.abspath(__file__))
print(len(os.listdir(python_folder)))



# file = open(os.path.join(path, "txt1.txt"), "a")
# for i in range(1, 51):
#     file.write("\nAppended => Elzero Web School")
# file.close()

# file = open(os.path.join(path, "txt1.txt"), "r")
# content = file.read()

# lines_count = content.count("\n") +1
# words_count = len(content.split())
# i_count = content.count("I")
# # print(len(content))

# print(f"Number Of Lines Is = {lines_count}")
# print(f"Number Of Words Is => {words_count}")
# print(f"Number Of Chars Is => {len(content)}")
# print(f"Number Of I's Is => {i_count}")


# for i in range(41, 51):
#     name = f"txt{i}.txt"
#     os.remove(os.path.join(path, name))


values = (0, 1, 2) # tuple => 0 = false , 1 = true, 2 = true 

if any(values): # 1 & 2 are true then it's true
    my_var = 0

my_list = [True, 1,  1, ["A", "B"], 10.5, my_var] # list of trues exept mylist[5]
    # will pass         # not gonna pass    #  not gonna pass
if all(my_list[:4]) or all(my_list[:6]) or all(my_list[:]):
    # will print good
    print("Good")
else:
    print("Bad")

# Good


def my_all(list):
    for i in list:
        if not i:
            return False
    return True
print(my_all([1, 2, 3]))
print(my_all([1, 2, 3, []])) # False

def my_any(list):
    for i in list:
        if i:
            return True
    return False

print(my_any([(), 0, False])) # False

print(my_any([0, 1, [], False])) # True

def my_min(list):
    for i in list:
        current = i
        for j in list:
            if current > j:
                min = j
    return min

print(my_min([10, 100, -20, -100, 50])) # -100


def my_max(list):
    for i in list:
        current = i
        for j in list:
            if current < j:
                min = j
    return min

print(my_max([10, 100, -20, -100, 50])) # -100


def remove_chars(string):
    return string[1:len(string)-1]

friends_map = ["AEmanS", "AAhmedS", "DSamehF", "LOsamaL"]

result = map(remove_chars, friends_map)
for i in result:
    print(i)


result = map(lambda string : string[1:len(string)-1] , friends_map)
for i in result:
    print(i)


def get_names(string):
    return string[-1] == "m"

friends_filter = ["Osama", "Wessam", "Amal", "Essam", "Gamal", "Othman"]

result = filter(get_names, friends_filter)
for i in result:
    print(i)


result = filter(lambda string: string[-1] == "m", friends_filter)
for i in result:
    print(i)

from functools import reduce

nums = [2, 4, 6, 2]

result = reduce(lambda num1, num2: num1*num2, nums)
# Output

print(result)


skills = ("HTML", "CSS", 10, "PHP", "Python", 20, "JavaScript")

# Output
"50 - JavaScript"
"52 - Python"
"53 - PHP"
"55 - CSS"
"56 - HTML"

for i in range(0, len(skills)):
    if type(skills[-(i+1)]) == int:
        continue
    print(f"{i + 50} => {skills[-(i+1)]}")


for count, skill in enumerate(reversed(skills), 50):
    if type(skill) == int:
        continue
    print(f"{count} => {skill}")


import random 

print(f"Random Number Between 10 And 50 => {random.randint(10, 50)}")

# num = random.randrange(2,11)
# if num %2 ==0:
#     print(f"Random Even Number Between 2 And 10 => {num}")


num = random.choice(range(2, 11, 2))
print(f"Random Even Number Between 2 And 10 => {num}")


num = random.choice(range(1,10, 2))
if num %2 !=0:
    print(f"Random Odd Number Between 1 And 9 => {num}")

print(dir(random))



# path = r"C:\Users\dell\Desktop\Python"
# file = open(os.path.join(path, "main.py"), "w").close()
# file = open(os.path.join(path, "my_mod.py"), "w").close()


import datetime
start_date = datetime.date(2026, 1, 6)
today = datetime.date.today()
diffrence = today - start_date

print(f"Days From {today} To {start_date} Is => {diffrence.days}")

myBirthdate = datetime.datetime(2004, 12, 31)
print(myBirthdate.strftime("%Y-%d-%m"))
print(myBirthdate.strftime("%b %d, %Y"))
print(myBirthdate.strftime("%d - %b - %Y"))
print(myBirthdate.strftime("%d / %b / %y"))
print(myBirthdate.strftime("%d / %B / %y"))
print(myBirthdate.strftime("%a, %m %B  %Y"))


def reverse_string(my_string):
    for i in reversed(my_string):
        yield i
# Reverse The String
for c in reverse_string("Elzero"):
  print(c)



def reverse_string(my_string):
    for i in range(1, len(my_string)+1):
        yield my_string[-i]
# Reverse The String
for c in reverse_string("Elzero"):
  print(c)



def my_decoretor(func):
    def nested_func():
        print("Sugar Added From Decorators")
        func()
        print("#"*50)
    return nested_func
# Create Your Decorator Here
@my_decoretor
def make_tea():
    print("Tea Created")

@my_decoretor
def make_coffee():
    print("Coffe Created")

make_tea()

make_coffee()

# Needed Output

"Tea Created"
"####################"
"Sugar Added From Decorators"
"Coffe Created"
"####################"


my_list = ["E", "Z", "R", 1, 2, 3]
my_tuple = ("L", "E", "O")
my_data = []
for data in zip(my_list, my_tuple):
    if type(data[0]) == str :
        if type(data[1]) == str :
            my_data.append(data[0])
            my_data.append(data[1])

final_string = "".join(my_data)
print(my_data) # Elzero
print(final_string.capitalize()) # Elzero



my_list1 = ["E", "L", "Z", "E", "R", "O", 1, 2]
my_tuple = ("E", "Z", "R", 1, 2, "E", "R", "O")
my_list2 = ("L", "E", "O", 1, 2, "E", "R", "O")
my_data = []

for item1, item2, item3 in zip(my_list1, my_tuple, my_list2):
    if type(item1) == str :
        my_data.append(item1)

final_string = "".join(my_data)
print(final_string.capitalize())



from PIL import Image

img = Image.open(r"C:\Users\dell\Pictures\elzero-pillow.png")
# img.show()

# l_letter = img.crop((400, 0, 800, 400))
# myconverted_img = l_letter.convert("L")
# myconverted_img.save(r"C:\Users\dell\Pictures\l_img.png")
# myconverted_img.show()

# half_img = img.crop((0, 400, 1200, 800))
# converted_img = half_img.convert("L").rotate(180)
# converted_img.show()
# converted_img.save(r"C:\Users\dell\Pictures\rotated_img.png")


def say_hello_to(name):
    """
    This function prints hello to the name given 
        parameter :
            name => name of the person
        return :
            return hello massage to name
    """
    print(f"Hello {name} How Are You!")

# print(dir(say_hello))
print(say_hello_to.__doc__)
help(say_hello_to)


# NUM = input("Add Your Number ")

# # Your Code Here
# if len(NUM) > 1:
#     raise IndexError("Only One Character Allowed")

# if NUM == 0:
#     raise ValueError("Number Must Be Larger Than 0")
# if not NUM.isdigit():
#     raise Exception("Only Numbers Allowed")

# print(f"Number Is {NUM}")



# LETTER = input("Add Letter From A to Z")

# try :
#     if len(LETTER) > 1 :
#         raise Exception("You Must Write One Character Only")
#     if not LETTER.isalpha() or not LETTER.isupper() :
#         raise Exception("The Letter Not In A - Z")

# except Exception as msg:
#     print(msg)
# else:
#     print(f"You Typed {LETTER}")


def calculate(num1, num2) -> int:
    return num1 + num2

print(calculate(20, 30))


# Reguler Exeprisions
# [A-Za-z]\s
# L(Elzero)
# \D{2}\d{4}\D\s\d+-\d{4}
# https?:\/\/(www\.)?elzero\.(org|com)(:[0-9]{4})?\/link\.(php|py)
# https?
# ^https?$
# https?$



class Game:
    # Write Class Content
    def __init__(self, name, developer, year, price):
        self.name = name
        self.developer = developer
        self.year = year
        self.price = price

    def price_in_pounds(self) :
        return self.price
    

    
game_one = Game("Ys", "Falcom", 2010, 50)

print(f"Game Name Is \"{game_one.name}\", ", end="")
print(f"Developer Is \"{game_one.developer}\", ", end="")
print(f"Release Date Is \"{game_one.year}\", ", end="")
print(f"Price In Egypt Is {game_one.price_in_pounds()}")




class User:
    # Write Class Content
    def __init__(self, fname, lname, age, gender):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.gender = gender
        
    def years(self):
        return 40 - self.age
    
    def full_details(self):
        if self.gender == "Male":
            return f"Hello Mr {self.fname} {self.lname[0]}.  [{self.years()}] To Reach 40"
        elif self.gender == "Female":
            return f"Hello Mrs {self.fname} {self.lname[0]}.  [{self.years()}] To Reach 40"
user_one = User("Osama", "Mohamed", 38, "Male")
user_two = User("Eman", "Omar", 25, "Female")

print(user_one.full_details()) # Hello Mr Osama M. [02] Years To Reach 40
print(user_two.full_details()) # Hello Mrs Eman O. [15] Years To Reach 40


class Message:
    # Write Class Content
    def print_message():
        return "Hello From Class Message"

print(Message.print_message())

# Output
# Hello From Class Message



class Games:
    # Write Class Content
    def __init__(self, data):
        self.data = data

    def show_games(self):
        if isinstance(self.data , str):
            print(f"I Have One Game Called : {self.data}")
        elif isinstance(self.data, list):
            print(f"I Have Many Games: ")
            for i in self.data:
                print(f"- {i}")
        elif isinstance(self.data, int):
            print(f"I Have {self.data} Game.")


my_game = Games("Shadow Of Mordor")
my_games_names = Games(["Ys II", "Ys Oath In Felghana", "YS Origin"])
my_games_count = Games(80)

my_game.show_games()
# Ouput
# I Have One Game Called "Shadow Of Mordor"

my_games_names.show_games()
# Ouput
# I Have Many Games:
# -- Ys II
# -- Ys Oath In Felghana
# -- YS Origin

my_games_count.show_games()
# Output
# I Have 80 Game.


# Main Class
class Members:

    def __init__(self, n, p):

        self.name = n

        self.permission = p

    def show_info(self):

        return f"Your Name Is {self.name} And You Are {self.permission}"

# Create Admin Class Here
class Admins(Members):

    def __init__(self, n, p):
        super().__init__(n, p)

# Create Moderators Class Here
class Moderators(Members):
    def __init__(self, n, p):
        Members.__init__(self, n, p)


member_one = Admins("Osama", "Admin")
member_two = Moderators("Ahmed", "Moderator")

print(member_one.show_info())
# Output
# Your Name Is Osama And You Are Admin

print(member_two.show_info())
# Output
# Your Name Is Ahmed And You Are Moderator


class A:

    def __init__(self, one):

        self.one = one

class B:

    def __init__(self, two):

        self.two = two

class C:

    def __init__(self, three):

            self.three = three

# Write The Class Called "Name" Here
class Name(A, B, C):
    def __init__(self, one, two, three):
        B.__init__(self, two)
        A.__init__(self, one)
        C.__init__(self, three)

    def show_name(self):
        return f"The name is {self.one}{self.two}{self.three}"
the_name = Name("El", "ze", "ro")

print(the_name.show_name())

# Ouput
# The Name Is Elzero

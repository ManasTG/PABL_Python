#%% Q1-1 The code that prints the sum of the values from 1 to 3 using the print() function is print(1+2+3). With reference to this code, print the sum of the values from 1 to 5 as follows.

print(1+2+3+4+5)

#%% Q2-1
N = 0
S = 0


#%% Q2-2

print('Enter an integer:')
n = int(input())

if n%2 == 0:
    print('n is even')
else:
    print('n is odd')

#%% Q3-1

i = 10
print('*'*i*2)
print('# '*i)

#%% Q4-1

name_in = input('Enter your Name: ')
add_in = input('Enter your Address: ')

print(f"Your Name is {name_in} and address is {add_in}")

#%% Q5-1
x = 1
y = 0
print(x and y)
print(x or y)
print(not x)
print(not y)

## Output
# 0
# 1
# False
# True

#%% Q6-1

num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))

if num1 > num2:
    print(num2, num1)
    
elif num1 < num2:
    print(num1, num2)
else:
    print("Numbers are invalid")
    
#%% Q7-1
adult = int(input("Are you an Adult?(0 or 1) "))
marriage = int(input("Are you married?(0 or 1) "))

if adult:
    adult_ans = "an adult" 
else:
    adult_ans = "not an adult"

if marriage:
    marriage_ans = "married"
else:
    marriage_ans = "not married"

print(f"You are {adult_ans} who is {marriage_ans}")


#%% Q8 - 1
for i in range(2, 13):
    is_prime = True
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        print(i, ": Prime number")
    else:
        print(i, ": Composite number")
        
        
#%% Q9-1
armstrong = []
for i in range(100, 1000):
    a = i // 100
    b = (i // 10) % 10
    c = i % 10
    if a**3 + b**3 + c**3 == i:
        armstrong.append(i)
print("Three-digit Armstrong numbers:", *armstrong)

#%% Q10-1

l1 = ['I like', 'I love']
l2 = ['pancake.', 'kiwi juice.', 'espresso.']
for a in l1:
    for b in l2:
        print(a, b)
        
        
#%% Q11-1

person = {'Name' : 'David Doe', 'Age' : 26, 'Weight' : 82, 'Job' : 'Data scientist'}
person['Father'] = 'John Doe'
print(person)

lst = [5, 6, 3, 9, 2, 12, 3, 8, 7]
for i in range(len(lst) - 1):
    if lst[i] > lst[i + 1]:
        lst[i], lst[i + 1] = lst[i + 1], lst[i]
print(lst)


#%% Q12-1
a = [[1, 2], [3, 4], [5, 6]]
flat = []
for sub in a:
    for num in sub:
        flat.append(num)
print(flat)

#%% Q13-1

a = [[1, 2], [3, 4], [5, 6]]
flat = []
for sub in a:
    for num in sub:
        flat.append(num)
print(flat)


#%% Q14-1

maria = {'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83}
print(sum(maria.values()) / len(maria))

#%% Q15-1
import copy
school = {'kim': {'age': 16, 'hei': 170, 'grade': 3}, 'lee': {'age': 15, 'hei': 168, 'grade': 2}, 'choi': {'age': 14, 'hei': 173, 'grade': 1}}
school2 = copy.deepcopy(school)
print(school is school2)


#%% Q16-1

scores = (('Hyun', 88, 95, 90), ('Kang', 85, 90, 95), ('Park', 70, 90, 80), ('Hong', 90, 90, 95))
names, eng, math, sci = zip(*scores)
print(sum(math) / len(math))



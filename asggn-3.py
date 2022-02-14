


#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ASSIGNMENT 3^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#Name-Devank Garg
#SID-21104098
#branch-EE


#Problem-1

print('Answer-1')
input_string=input("Enter the string: ")
checking_list = input_string.split(" ") 
if len(checking_list) == 1 :
 
    letter_list = list(input_string.lower())       
    a={}

    for letter in letter_list:
        if letter in a:
            a[letter] = a[letter] + 1
        else:
           a[letter] = 1
    for key in a:
        print(f'This letter "{key}" showed up {a[key]} time')

else:
    new_string=input_string.lower()
    word_list=new_string.split(" ")   
    b={}                           

    for word in word_list:
        if word in b:
            b[word] +=1
        else:
            b[word]=1
    for key in b:
        print(f'This word "{key}" appeared {b[key]} times')
        
        
#***********************************************************************************

#Problem-2-

print('\n\nAnswer-2')
day = int(input("Enter the day: "))
month = int(input("Enter the month: "))
year = int(input("Enter the year: "))



for i in range(1):
    if month in (1, 3, 5, 7, 8, 10):                    
        if day > 31 or day < 0:
            print("You entered day cannot exist")
        elif 0 < day <= 30:
            day += 1
            print(f'The next date is {day}/{month}/{year}')
        else:
            day = 1
            month = month + 1
            print(f'The next date is {day}/{month}/{year}')
            break
    if month in (4, 6, 9, 11):                                 
        if day > 30 or day < 0:
            print("You entered day cannot exist")
        elif 0 < day <= 29:
            day += 1
            print(f'The next date is {day}/{month}/{year}')
        else:
            day = 1
            month = month + 1
            print(f'The next date is {day}/{month}/{year}')
            break

    if month == 2:
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:  
            if day == 28:
                day = day + 1
                print(f'The next date is {day}/{month}/{year}')

            elif day == 29:
                day = 1
                month = month + 1
                print(f'The next date is {day}/{month}/{year}')
                break
            else:
                print("Your entered date is invalid")

        else:
            if day > 28 or day < 0:
                print("This day cannot exist")
            elif 0 < day <= 27:
                day = day + 1
                print(f'The next date is {day}/{month}/{year}')
            else:
                day = 1
                month = month + 1
                print(f'The next date is {day}/{month}/{year}')
                break

    if month == 12:
        if day > 31 or day < 0:
            print("You entered day cannot exist")
        elif 0 < day <= 30:
            day += 1
            print(f'The next date is {day}/{month}/{year}')
        else:
            day = 1
            month = 1
            year = year + 1
            print(f'The next date is {day}/{month}/{year}')
            break

    if month > 12 or month < 0:
        print("Your entered month is invalid,Please enter a valid month")
             
        
#***********************************************************************************

#Problem-3-

print('\n\nAnswer-3')
    
number_of_element=int(input("how many number you want to enter>> "))

list1=[]                                         


for i in range(number_of_element):
    n=float(input("enter the number - "))         
    list1.append(n)

list2=[]                                          
for number in list1:
    new_number=number*number
    list2.append(new_number)



required_output=list(zip(list1,list2))
print("output is",required_output)

        
#***********************************************************************************

#Problem-4-

print('\n\nAnswer-4')

# Taking input
grade_points = int(input("Enter your grade point- "))     
if grade_points == 10:
    print("Your Grade is 'A+' and Excellent Performance")

elif grade_points == 9:
    print("Your Grade is 'A' and Excellent Performance")

elif grade_points == 8:
    print("Your Grade is 'B+' and Excellent Performance")

elif grade_points == 7:
    print("Your Grade is 'B' and Excellent Performance")

elif grade_points == 6:
    print("Your Grade is 'C+' and Excellent Performance")

elif grade_points == 5:
    print("Your Grade is 'C' and Excellent Performance")

elif grade_points == 4:
    print("Your Grade is 'D' and Excellent Performance")

else:
    print("Error")

        
#***********************************************************************************

#Problem-5-

print('\n\nAnswer-5')

letters=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']
for i in range(11):
    output =""                

    for letter in range(11 - 2 * i):
        output += letters[letter]
    k=" "                      
    print(k * i + output)

        
#***********************************************************************************

#Problem-6-

print('Answer-6')

dictionary ={}   

while True:
    user_choice = input("Enter 'Y' if you want to enter more data ,else enter 'N' --> ")


    if user_choice.upper() == 'N':
        break
    if user_choice.upper() == 'Y':
        name = input("Enter your name :")
        sid = int(input("Enter your sid : "))
        dictionary[sid] = name
    else:
        print("Your enter  invalid choice,Please enter valid choice")  
# part (a)
print("Answer-6(a)")
print(dictionary)

#part (b)

print("Answer-6(b)")
print({i:j for i,j in sorted(dictionary.items(), key = lambda a:a[1])})  

#part (c)

print("Answer-6(c)")
print({i:j for i,j in sorted(dictionary.items())})  

#part (d) 
print("Answer-6(d)")
sid=int(input("Please enter a sid which you want to search>>"))
print("your searched student name is-",dictionary[sid])

        
#***********************************************************************************

#Problem-7-

print('\n\nAnswer-7')

n=int(input("terms of fibonacci serie you want to print-"))
if n<0:
    print("invalid input,please enter a positive number")
sum1=0                                                         
def fib(n):  
    if n <= 1:
        return n
    else:
        return (fib(n - 1) + fib(n - 2))

for i in range(n):

    print(fib(i))
    sum1 += fib(i)

if n==0:                      
    print(" average is 0")
else:
    print("the average of above series is ", sum1 / n)
    
set1={1,2,3,4,5}
set2={2,4,6,8}
set3={1,5,9,13,17}

        
#***********************************************************************************

#Problem-8-

print('\n\nAnswer-8')

# part (a)
print("Answer-8(a)")
new_set= set1^set2

print(new_set)

# Part (b)

print("Answer-8(b)")
set4=set3^set2^set1

print(set4)

# part (c)

print("Answer-8(c)")
set5= set1&set2 | set2&set3 | set3&set1

print(set5)

#Part (d)

print("Answer-8(d)")
our_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10 }
set6 = our_set - set1

print(set6)

# part (e)

print("Answer-8(e)")
set7 = our_set - set1 -set2 - set3

print(set7)

#************************************************************************************
print('\n\n\nName-Devank garg')
print('SID-21104098')
print('Branch-EE')

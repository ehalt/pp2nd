import math

# ------------> area of a rectangle <--------------

# length = int(input('enter length here: '))
# breadth = int(input('enter breadth here: '))
# area = length * breadth
# print('Area of a rectangle is ', area)

# ----------> print() <----------------

# print('assalamu alaikum')
# print('welcome to the programming contest')
# print('kemon hocce sob?')

# -----------> print() <-------------

# print('hello world', end = ' ')
# print('What is going on?', end = ' ')
# print('Godebye', end = ' ')


# ----------> write a program to add one integer and floating type number <------------

# num1 = int(input('Enter an integer number here: ')) 
# num2 = float(input('Enter a floating number here: '))
# total = num1 + num2
# print('Entered integer number is : ', num1)
# print('Entered floating number is : ', num2)
# print('Total sum is: ', total)


# -------------> Eval <----------------

# x = eval('123')
# print(x)
# print(type(x))

# -------> Write a program to display details entered by a user, name, age, gender and height <---------

# name = input('Enter name here: ')
# age = eval(input('Enter age here:'))
# gender = input('Enter gender here: ')
# height = eval(input('Enter height here: '))

# print('User details are as follows:')
# print('Name  of user : ', name)
# print('Age of user: ', age)
# print('Height of user: ', height)


#-----> write a program to calculate the radius of a circle <--------

# radius = int(input('Enter raidus here: '))
# pi = 3.1416
# area = pi * radius * radius
# print('Area of a circle is :',area)

#-----------> Write a program to clalculate the hypotenuse of the right-angle triangle given as follows: <-------------

# base = int(input('Enter the base of a right - angleed triangle: '))
# height = int(input('Enter the height of a right-angled tringle: '))
# print('----------> Tringle details are as follows <-----------')
# print('Base: ', base)
# print('Height: ', height)
# hypotenus = math.sqrt(base * base + height * height)
# print('Hypotenus : ', hypotenus)


# --------> The ord() function <-------------

# a = ord('A')
# b = ord('z')
# c = ord('a')
# print(a)
# print(b)
# print(c)


# ---------> write a program to find the difference between the ASCII code of any lower case letter nad its corresponding upper case letter -----------

# char1 = 'b'
# char2 ='B'
# print('letter\tASCII value :')
# print(char1,'\t', ord(char1))
# print(char2, '\t', ord(char2))
# print('========== Difference  between ascii value of two letters ==========')
# print(ord(char1), '-', ord(char2), '=', end=' ')
# print(ord(char1) - ord(char2))



# ====================================================================================
# ============================= Chapter - 3 ==========================================
# ---------------------- Operators and Expressions -----------------------------------
# ====================================================================================


# Read the cost and selling price of an object and write a program to find the profit earned by a seller

# apple = 200
# banana = 120
# carrot = 130
# totalbuy = apple + banana + carrot

# applesp = int(input('Apple price: '))
# bananasp = int(input('Banana price: '))
# carrotsp = int(input('Carrot price: '))
# totalsell = applesp + bananasp + carrotsp
# profit = totalsell - totalbuy

# print('Total sell price: ', totalsell)
# print('Profit ', profit, ':D')


# ---------------> Write a program to calculate the square and cube of a number using * <--------------

# num = int(input('Enter a number to calculate square and cube: '))
# sqr = num * num
# cube = num * num * num
# print(f'square of this number : {sqr} and cube of this number : {cube}')


# ----------> Write a program to calculate simple interest. Read the principle rate of interest and number of years form the user <-------------

# p = eval(input('Enter principle amount in taka = ')) #read p
# roi = eval(input('Enter rate of inerest = ')) #read roi
# years = eval(input('Enter the number of years = ')) #read years
# print('printciple : ', p)
# print('Rate of interest : ', roi)
# print('Number of years : ', years)

# si = p * roi * years / 100
# print('Simple interest = ', si)

# ---------> Write a program to read temperature in celsius from the user and convert it into farenheit <---------

# celsius = eval(input('Enter degree is celsius: '))
# print('celsius : ', celsius)
# farenheit = (9 / 5 ) * celsius + 32
# print('Farenheit = ', farenheit)


# ---------> Write a program to read the weight of an object in grams and display its weight in kilograms and grams, respectively ----------

# w1 = eval(input('Enter the weight of the object in grams: '))
# print('Weight of object = ', w1, 'grams')

# w2 = w1 // 1000
# w3 = w1 % 1000
# print('Weight of object = ', w2, 'kg and ', w3, 'g')

# # #Fundamental data types
# # #int
# # #float
# # #bool
# # #str
# # #list
# # #tuple
# # #set
# # #dict

# # #Classes -> custom types

# # #Specialized Data Types

# # #None

# # #
# # #
# # #
# # #
# # #PART 16 NUMBERS

# # # print(2 + 4)
# # # print(2 - 4)
# # # print(2 / 4)
# # # print(2 * 4)

# # # print(type(2 + 4))
# # # print(type(2 - 4))
# # # print(type(2 / 4))
# # # print(type(2 * 4))

# # # print(2 ** 3) #to the power of
# # # print(2 // 3) #returns int rounded down
# # # print (5 % 3) #mod

# # #MATH  FUNCTIONS
# # print(round(3.9)) #rounds number up
# # print(abs(-20))   #gives absolute value

# # bin(5) #will return the binary value of the number
# # print(int('b101', 2)) #this will convert the number into int from binary

# # #VARIABLES

# iq = 190
# user_age = iq/4
# a = iq/user_age


# print(a)
# a,b,c = 1,2,3
# print(a)
# print(b)
# print(c)

# AUGMENTED ASSIGNMNT OPERATOR
# Value = 5
# Value2 = 2 + Value
# Value3 += 2

# print(Value)
# print(Value2)
# print(Value3)

# #STRINGS

# Long_String = '''
# this
# is
# a
# long 
# String 
# '''
# print(Long_String)
# First_Name = 'James'
# Last_Name = 'Urias'
# Full_Name = First_Name + Last_Name
# print(Full_Name)

# #STRING CONCATENATION
# print('Hello' + 'James')

# #TYPE CONVERSION
# print(str(100))
# a = str(100)
# b = int(a)
# c = type(b)
# print(c) 

# #ESCAPE SEQUENCE
# print('that's')
# print('that\'s')
# \t = Tab
# \n = newline 


# #FORMATTED STRINGS
# Name = 'James'
# Age = 23

# print(f'Hi {Name}. You are {Age} years old.')

# STRING INDEX  
# Selfish = 'me me me '
# print(Selfish[0])
# #[start:stop:stepover]
# Numbers = '01234567'
# print(Numbers[0:7:2])
# print(Numbers[1:])
# print(Numbers[:5])
# print(Numbers[-1]) #starts from the end
# print(Numbers[::-1])

#strings cannot be changed only reassigned 


# BUILT IN FUNCTIONS AND METHODS 

# test = '12345'
# print(len(test))
#methods will start with a . and only work on strings 

# quote = 'to be or not to be'
# print(quote.upper())

########################################
#SECTION 34 EXCERCISE 
# Year = input('What year were you born? ')
# Age = 2019 - int(Year)

# print(f'You are {Age} years old')
# number = int(input('Number'))
# print(type(number))

########################################
#SECTION 36 EXCERCISE 
# Username = input("What is your username? ")
# Password = input("What is your password? ")
# Pass_Length = len(Password)
# Hidden_Pass = '*' * Pass_Length

# print(f'Hi {Username} your password {Hidden_Pass} is {Pass_Length} characters long')

#LISTS
# List1 = [1,2,3,4,5]
# List2 = ['a','b','c']
# List3 = [1,2,'a',True]

# Cart = [
#   'book',
#   'pen',
#   'glasses',
#   'pencil'
#   ]

# print(Cart[0:2])

# Cart2 = Cart #this will make cart2 always match cart 
# Cart2 = Cart[0:3] #this will make a copy 

# #MATRIX
# Matrix = [
#   [1,2,3],
#   [4,5,6],
#   [7,8,9]
# ]

# List1 = [1,2,3,4,5]
# List1.apend(6) #this will modify the list in place not copy it
# List1.insert(5,6) #same as above but will place ist where specified 
# List1.extend(6) #will add to the list
# List1.pop() # will remove from the list
#.index wil give you the index of an item, you can also look through a range within the index
#.count will count the instances of an item
#.sort will modify a list  
# Alpha = ['b','c','a']
# sorted(Alpha)
# print(Alpha)

# Alpha.sort() 
# print(Alpha)
# print(list(range(100)))
# Sentence = ''
# New_Sentence = ' '.join(['This','is','a','sentence'])
# print(New_Sentence)

#LIST UNPACKING

# a,b,c,*other,d = [1,2,3,4,5,6,7]
# print(a) 
# print(b)
# print(c) 
# print(other)
# print(d) 


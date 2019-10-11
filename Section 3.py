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

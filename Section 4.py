### CONDITIONAL LOGIC

# Is_Old = True
# Is_Licensed = True

# if Is_Old:
#     print('You are old enough to drive!')
# elif Is_Licensed:
#     print('You can drive now!')
# else:
#     print('You Can not drive!')

# print('Check ')

# #or
# if Is_Old and Is_Licensed:
#     print('You can drive!')
# else:
#     print('You can not drive!')
#Ternary operators
# Condition_If_True if Condition else Condition_Is_False

# Is_Friend = False
# Can_Message = "Message allowed" if Is_Friend else "Not allowed to message"

# print (Can_Message)

# is_magician = True
# is_expert = False
# if not is_magician:
#   print('You need magic powers')

# elif not is_expert:
#   print('At least you are getting there')

# elif is_expert and is_magician:
#   print('You are a master magician')
####FOR LOOPS
# for itm in (1,2,3,4):
#   print(itm)
#   print(itm)

###Iterables
# user = {
#  'name': "Golem",
#  'Age' : 100,
#  'Can_swim' : False
#  }

# for key, value in user.items():
#   print(key,value)

# for item in user.values():
#   print(item)

# for item in 50:
#   print(item)

# #COUNTER QUIZ
# my_list = [1,2,3,4,5,6,7,8,9,10]
# sum = 0
# for Num in my_list:
#   sum+=Num

# print(sum)

##RANGE()
# print(range(100))

# for _ in range (0,10,2):
#   print(_)

# for _ in range (0,10,-1):
#   print(_)

###ENUMERATE()
# for i,char in enumerate('Hello'):
#   print(i,char)

# for i in enumerate('Hello'):
#   print(i)

# for i, num in enumerate(range(100)):
#   if num == 50:
#     print(f'the index of 50 is{i}')

###WHILE LOOPS
# i = 0
# while i<50:
#   print(i) 
#   break  

# i = 0
# while i<50:
#   print(i) 
#   i+=1
# else:
#   print("done with all the work")

# while True:
#   input('Say something: ')

# my_list = [1,2,3,4]
# for iteam in my_list:
#   print(iteam)
#   continue
#   print('stop')

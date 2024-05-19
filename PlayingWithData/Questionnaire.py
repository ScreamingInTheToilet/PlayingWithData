from QuestionFile import Topic
import random
import json

file_ = r'C:/Users/dell/OneDrive - Nord Anglia Education/AnhKhoaProgramming/PlayingWithData/UserData.py'

with open(file_) as f:
   UserInfo = json.load(f)

def bin_to_dec(binary):
  decimal = 0
  
  index = len(binary) 
  '''For loop required to translate all the digits.'''
  for digit in binary:
    index -= 1
    '''
    The index will start off with 1 lower than the length of the string, so
    the last index would be 0.
    '''
    decimal += int(digit) * (2 ** index)
    '''Applying the formula (1 or 0) multiply 2^(index)'''
  return decimal

def dec_to_hexadec(decimal):
  Latin = ['A', 'B', 'C', 'D', 'E', 'F']
  hexadecimal_list = []
  while decimal >= 1:
    if decimal%16 < 10:
      hexadecimal_list.append(decimal%16)
    else:
      hexadecimal_list.append(Latin[decimal%16 - 10])
    decimal = decimal // 16
  return ''.join([str(i) for i in hexadecimal_list[::-1]])

name = input('Enter your name: ')

code_A = int()

list = []
for i in range(20):
    topic_ = random.choice(Topic)
    entry = input(f'do you {topic_}? ').lower()
    if entry == 'yes':
        list.append('1')
        code_A = code_A + Topic.index(topic_)
    elif entry == 'no':
       list.append('0')
    else:
       print('Incorrect input') 
       break
    Topic.remove(topic_)


fib = ''
for i in list:
   fib = fib + i

UserInfo["User"].append({"User": name, "Code": f"{dec_to_hexadec(bin_to_dec(fib))}-{code_A}"})

with open(file_, 'w') as f:
   json.dump(UserInfo, f)

print(f'Your code is: {dec_to_hexadec(bin_to_dec(fib))}')


  
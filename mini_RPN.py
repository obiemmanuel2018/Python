import re
import operator
import time

# def compile_time(func):
#     def wrapper(*args,**kwargs):
#         t1 = time.time()
#         ret_val = func(*args,*kwargs)
#         print('{:.2f} milliseconds'.format(time.time() - t1))
#         return  ret_val
#     return wrapper



stack = []


def evaluate(action):
      while 1:
          if len(stack) > 2:
              op2 = stack.pop()
              op1 = stack.pop()
              result = action(op1, op2)
              stack.append(result)
              break
          elif len(stack) == 2:
              op2 = stack.pop()
              op1 = stack.pop()
              result = action(op1, op2)
              stack.append(result)
              break
          elif len(stack) == 1:
              return
          else:
              break
      return result

def main():
    result = 0
    pat2 = r'[-+*/]'
    pat1 = r'\d'
    pat3 = r'[a-zA-Z]'
    while 1:
          try:
               input_val = input('Enter RPN Expression: ')
               input_val = input_val.split(' ')
               for i in range(len(input_val)):
                   if re.match(pat1, input_val[i]):
                       input_val[i] = int(input_val[i])
                       stack.append(input_val[i])
                   elif re.match(pat2, input_val[i]):
                       m = re.match(pat2, input_val[i])
                       if m.group() == '+':
                           result = evaluate(operator.add)
                       elif m.group() == '-':
                           result = evaluate(operator.sub)
                       elif m.group() == '*':
                           result = evaluate(operator.mul)
                       elif m.group() == '/':
                           result = evaluate(operator.truediv)
                   elif re.match(pat3, input_val[i]):
                       print('Unrecognise Input {}!'.format(input_val[i]))
                       print('{:*^19}'.format('previous result'))
                       break
                   else:
                       print('Unrecognise Input {}!'.format(input_val[i]))
                       print('{:*^19}'.format('previous result'))
                       break
               print('{:.3f}'.format(result))
          except Exception:
               print('Stack Underflow')
main()

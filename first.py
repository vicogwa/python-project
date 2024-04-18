# print("this is it")

# for x in range (1,12):
#     print(x)

# x = input('enter num ')
# y = input('enter num ')
# if  x > y:
#     print('greater')
    
# elif x < y:
#     print('less than')
# else:
#     print('equal num')   

# tuple = ('python ')*3
# print(tuple) 


# x = 3
# y = 4
# z = 5
# print(x if not x + y * z else y)

print("enter two number and i'll divide it for you ")
print("enter 'q' to quit")

while True:
    f_num = ("enter first num ")
    if f_num == 'q':
        break
    s_num = ("enter second num ")
try:
    anwser= int(f_num) / int (s_num)
except:
    ZeroDivisionError
    print("number is indivisible by 0") 
else:
    print(anwser)       
        
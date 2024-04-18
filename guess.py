import random
import time

OPERATORS = ['+', '-', '*']
OPERAND_1 = 3
OPERAND_2 = 12
total_problems = 12

def generate_problems():
    left = random.randint(OPERAND_1, OPERAND_2)
    right = random.randint(OPERAND_1, OPERAND_2)
    Operator = random.choice(OPERATORS)

    expr = str(left) + " " + Operator + " " + str(right)
    answer = eval(expr)
    return expr, answer

wrong = 0
input("press enter to start")
print("----------------")

start_time = time.time()

for i in range(total_problems):
    expr, answer = generate_problems()
    while True:
        guess = input("problems #" + str(i + 1) + ": " + expr + " = " )
        if guess == str(answer):
            break
        wrong += 1
end_time = time.time()
TOTAL_time = round(end_time - start_time, 2)
print("---------------------")
print("wow! you finished in", TOTAL_time , "seconds")            


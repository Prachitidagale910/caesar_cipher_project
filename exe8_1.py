import math

def check_Prime(num):
    for i in range(2,num - 1):
        if(num % 2 == 0):
            return False
    return True


def paint_calc(height, width, covre):
    area = height * width
    cans = math.ceil(area / covre)
    return cans


test_h = int(input("Height of wall : "))
test_w = int(input("Widht of wall : "))

coverage = 5

total_cans = paint_calc(height =test_h, width = test_w, covre=coverage)
print("Total cans required are :", total_cans)

#prime number checker

result = check_Prime(1)
print(result)
def find_median(num1, num2):
    num3 = num1 + num2
    num3.sort()
    if len(num3) %2 == 0:
        val = len(num3) // 2
        return (num3[val - 1] + num3[val]) / 2
    return num3[len(num3) // 2]


num1 = [1, 3]
num2 = [2]
print(find_median(num1, num2))

num1 = [1, 2]
num2 = [3, 4]
print(find_median(num1, num2))
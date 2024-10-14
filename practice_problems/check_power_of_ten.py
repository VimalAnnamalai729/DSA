
def is_power_of_ten(num):
    if num <= 0:
        return False

    while num % 10 == 0:
        num //= 10
    return num == 1

if __name__ == "__main__":
    print(is_power_of_ten(10))
    print(is_power_of_ten(100))

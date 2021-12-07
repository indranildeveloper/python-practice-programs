# Calculate the factorial of a given number and find the number of trailing zeros


def factorial(number):
    if (number == 0 or number == 1):
        return 1
    else:
        return number * factorial(number - 1)


def factorialTrailingZeros(number):
    # factorial_num = factorial(number)
    # print(factorial_num)
    # count = 0
    # while(factorial_num % 10 == 0):
    #     count = count + 1
    #     factorial_num = factorial_num / 10
    # return count

    count = 0
    i = 5
    while(number / i != 0):
        count += int(number / i)
        i = i * 5
    return count


if __name__ == '__main__':
    number = int(input("Enter a number: \n"))
    factorial_num = factorial(number)
    print(f"The factorial is {factorial_num}")
    print(factorialTrailingZeros(number))

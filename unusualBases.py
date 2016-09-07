# Decimal to "Base Fib" - "Base Fib" to Decimal Converter

# Base Fib: use (1) or don't use (0) a Fibonacci Number to create any positive integer
# example: 
# 13   8   5   3   2   1   1
#  1   0   0   0   1   1   0 = 16 in "Base Fib"

# collect and save user input
input_line = raw_input("Enter base (F or 10) and number to be converted: ")

input_list = input_line.split(" ")
base = input_list[0]
number = input_list[1]

# translate from base fib to decimal
if base == "F":
    # Create sufficient amount of Fibonacci Numbers
    a, b = 0, 1
    fib_numbers = []
    for i in range(len(number)):
        a, b = b, a+b
        fib_numbers.append(a)
        fib_numbers.sort(reverse=True)

    result = []
    number_digit_list = [int(i )for i in str(number)]
    for item1, item2 in zip(number_digit_list, fib_numbers):
        if item1 == 1:
            result.append(item2)
        else:
            pass

    print(sum(result))

# translate from decimal to base fib
elif base == "10":
    # Create sufficient amount of Fibonacci Numbers
    a, b = 0, 1
    fib_num_list = []
    while True:
        a, b = b, a+b
        fib_num_list.append(a)
        if fib_num_list[-1] >= int(number):
            fib_num_list.sort(reverse=True)
            break

    fib_result = []
    for entry in fib_num_list:
        if int(number)/entry == 1:
            fib_result.append(int(number)/entry)
            number = int(number)%entry
        else:
            fib_result.append(0)
    
    # remove first item of fib_results since excess 0 is added (?)    
    print(" ".join(str(x) for x in fib_result[1:]))












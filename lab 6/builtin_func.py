import math

#task1
def multiply_numbers(numbers):
    return math.prod(numbers)

numbers = [2, 3, 4, 5]
result = multiply_numbers(numbers)
print("Result:", result)


#task2
def count_upper_lower(string):
    upper_count = sum(1 for char in string if char.isupper())
    lower_count = sum(1 for char in string if char.islower())
    return upper_count, lower_count

input_string = "Hello World! How Are You Doing?"
upper_count, lower_count = count_upper_lower(input_string)
print("Number of uppercase letters:", upper_count)
print("Number of lowercase letters:", lower_count)


#task3
def is_palindrome(string):
    string = string.lower().replace(" ", "")
    return string == string[::-1]


input_string = "А роза упала на лапу Азора"
if is_palindrome(input_string):
    print('палиндром') 
else:
    print('не палиндром')


#task4
import time
import math

def square_root_after_delay(number, milliseconds):
    time.sleep(milliseconds / 1000)  # Convert milliseconds to seconds
    result = math.sqrt(number)
    print(f"Square root of {number} after {milliseconds} milliseconds is {result}")


number = 25100
milliseconds = 2123
square_root_after_delay(number, milliseconds)


#task5
def all_true(tuple_data):
    return all(tuple_data)


tuple1 = (True, True, True)
tuple2 = (True, False, True)
print("All elements in tuple1 are True:", all_true(tuple1))
print("All elements in tuple2 are True:", all_true(tuple2))
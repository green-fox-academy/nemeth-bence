# Create a function called `min_max_diff` that takes a list of numbers as parameter
# and returns the difference between maximum and minimum values in the list
# Create basic unit tests for it with at least 3 different test cases


def min_max_diff(numbers):
     max = numbers[0]
     min = numbers[0]
     try:
        for number in numbers:
            if number > max:
                max = number
            if number < min:
                min = number
        return max - min

     except ZeroDivisionError:
         return None

print(min_max_diff([4, 10, 23, 17, 22]))

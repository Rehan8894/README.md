#Task 1# prompt: Problem Statement: Write a Python program that:

# 1.   Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.
# 2.   Returns the calculated factorial.
# 3.   Calls the function with a sample number and prints the output.

def factorial(n):
  """
  This function calculates the factorial of a non-negative integer.
  """
  if n < 0:
    return "Factorial is not defined for negative numbers."
  elif n == 0:
    return 1
  else:
    fact = 1
    for i in range(1, n + 1):
      fact *= i
    return fact

# Get input from the user
num = 5  # Example number, you can change this

# Calculate the factorial
result = factorial(num)

# Print the result
print(f"The factorial of {num} is {result}")

#Task 2

# prompt: Problem Statement: Write a Python program that:
# 1.   Asks the user for a number as input.
# 2.   Uses the math module to calculate the:
# o   Square root of the number
# o   Natural logarithm (log base e) of the number
# o   Sine of the number (in radians)
# 3.   Displays the calculated results.

import math

def factorial(n):
  if n == 0:
    return 1
  else:
    fact = 1
    for i in range(1, n + 1):
      fact *= i
    return fact

try:
  num = float(input("Enter a number: "))

  sqrt_num = math.sqrt(num)
  log_num = math.log(num)
  sin_num = math.sin(num)

  print("Square root:", sqrt_num)
  print("Natural logarithm:", log_num)
  print("Sine:", sin_num)

  sample_number = 5
  fact = factorial(sample_number)
  print(f"The factorial of {sample_number} is {fact}")

except ValueError:
  print("Invalid input. Please enter a valid number.")
except Exception as e:
  print(f"An error occurred: {e}")

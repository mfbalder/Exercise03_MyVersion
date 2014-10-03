# In the file arithmetic.py, these function signatures are required

# add(int, int) -> int
# Returns the sum of the two input integers

# subtract(int, int) -> int
# Returns the second number subtracted from the first

# multiply(int, int) -> int
# Multiplies the two inputs together

# divide(int, int) -> float
# Divides the first input by the second, returning a floating point

# square(int) -> int
# Returns the square of the input

# cube(int) -> int
# Returns the cube of the input

# power(int, int) -> int
# Raises the first integer to the power of the second integer and returns the value.

# mod(int, int) -> int
# Returns the remainder when the first integer is divided by the second integer.

def add(nums):
    """Returns the sum of the two input integers"""
    total = 0
    for num in nums:
    	total = total + num
    return total

def subtract(nums):
    """Returns the second number subtracted from the first"""
    total = nums[0]
    for num in nums[1:]:
        total = total - num
    return total

def multiply(nums):
    """Multiplies the two inputs together"""
    total = 1
    for num in nums:
        total = total * num
    return total

def divide(nums):
    """Divides the first input by the second, returning a floating point"""
    total = nums[0]
    for num in nums[1:]:
        total = total / num
    return total

def square(nums):
    """Returns the square of the input"""
    # if len(args[0]) > 1:
    #     return "Square only takes one argument"
    return nums[0] ** 2

def cube(nums):
    """ Returns the cube of the input"""
    # if len(args[0]) > 1:
    #     return "Cube only takes one argument"
    return nums[0] ** 3

def power(nums):
    """Raises the first integer to the power of the second integer and returns the value"""
    total = nums[0]
    for num in nums[1:]:
        total = total ** num
    return total

def mod(nums):
    """Returns the remainder when the first integer is divided by the second integer."""
    total = nums[0]
    for num in nums[1:]:
        total = total % num
    return total
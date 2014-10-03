"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""
import arithmetic

def main():
	# declares a dictionary that matches a operator to its function
	arithmetic_functions = {
        '+': arithmetic.add,
        '-': arithmetic.subtract,
        '*': arithmetic.multiply,
        '/': arithmetic.divide,
        'pow': arithmetic.power,
        'square': arithmetic.square,
        'cube': arithmetic.cube,
        'mod': arithmetic.mod
        }

	while True:
		# get an expression from the user
		user_input = raw_input("> ")
		# break that expression input into a list of elements
		tokens = user_input.split()

		operator = tokens[0]
		inputted_numbers = tokens[1:]
		

		# if the first element that the user enters is a 'q', quit the program
		if operator == 'q':
			break

		# if the first number the user enters isn't an operator, send them back to the top
		if operator not in arithmetic_functions:
			print "Please enter an operator first."
			# sends the user back to the beginning
			continue 

		# if the operator is a square or cube, check to ensure the user has only input one number
		if operator == 'square' or tokens[0] == 'cube':
			if len(inputted_numbers) > 1:
				print "You may only input one number to be squared or cubed"
				continue
		# otherwise, check to ensure that user has input at least 2 numbers
		elif len(inputted_numbers) < 2:
			print "You must enter at least 2 numbers"
			continue

		# if the inputted number strings can be converted to floats, do that	
		try:
			inputted_numbers_as_floats = map(float, inputted_numbers)
		# otherwise return an error and send user back to the top
		except ValueError:
			print "This calculator can only calculate numbers"
			continue

		# call the appropriate function
		print arithmetic_functions[operator](inputted_numbers_as_floats)
		
		# if inputted_numberes ARE ALL NUMBERS:
		# 	try:
		# 		int(x)
		# 	except:

		# else:
		# 	print error

		# try:
		# 	# calls the appropriate function, passing it all the numbers the user has input
		# 	print arithmetic_functions[operator](inputted_numbers)
		# # if not, print an error message and send the user back to the beginning
		# except ValueError:
		# 	print "This calculator can only calculate numbers"
		# 	continue


   
if __name__ == '__main__':
    main()
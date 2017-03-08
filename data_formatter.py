import os

_NEWLINE = '_NEWLINE'
_INDENT = '_INDENT'
_PYTHON = 'python'
_C_PLUS_PLUS = 'c++'

DATA_DIR = 'data'
LANGUAGE = _PYTHON

def format_training_data():
	code_chef_path = os.path.join(DATA_DIR, 'codechef')
	code_forces_path = os.path.join(DATA_DIR, 'codeforces')

	# Create description.txt and code.txt files
	with open(os.path.join(DATA_DIR, 'description.txt'), 'w') as description_output:
		with open(os.path.join(DATA_DIR, 'code.txt'), 'w') as code_output:

			for root, dirs, files in os.walk(code_chef_path):
				description_sentence = None
				solution_sentence = None

				if root.endswith('description'):
					description_file = files[0] if files else None
					description_sentence = format_description_into_sentence(root, description_file)

				elif root.endswith('solutions_' + LANGUAGE):
					# Take the first code solution provided and pair it with the description.
					# TODO: Later we can try using more than one solution.
					first_solution_file = files[0] if files else None
					solution_sentence = format_code_into_sentence(root, first_solution_file)

				# Sometimes there isn't a solution for the given problem. Ignore such problems.
				if description_sentence: # and solution_sentence:
					print 'Writing to output'
					description_output.write(description_sentence + '\n')
					# code_output.write(solution_sentence + '\n')

def format_description_into_sentence(root, description_file):
	"""
	Convert description file into a single sentence string.
	"""
	if not root or not description_file:
		return None

	with open(os.path.join(root, description_file), 'r') as description:
		print os.path.join(root, description_file)
		output_sentence = ''
		for line in description:
			output_sentence += line.rstrip() + ' '
		print 'Output sentence: ', output_sentence
		return output_sentence

def format_code_into_sentence(root, solution_file):
	"""
	Convert code solution file into a single sentence string.
	"""
	if not root or not solution_file:
		return None

	return ''
	

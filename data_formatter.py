import os

_NEWLINE = '_NEWLINE'
_INDENT = '_INDENT'
_PYTHON = 'python'
_C_PLUS_PLUS = 'c++'

DATA_DIR = 'data'
LANGUAGE = _C_PLUS_PLUS

TRAINING_RATIO = 0.5
DEV_RATIO = 0.25

create_small_data_set = True

def create_data_set():
	output_data_dir = DATA_DIR + '_small' if create_small_data_set else DATA_DIR + '_large'
	num_examples = _format_training_data()

	# Only use half of the examples for creating a small data set.
	if create_small_data_set:
		num_examples = num_examples / 2

	num_examples_in_training_set = int(TRAINING_RATIO * num_examples)
	num_examples_in_dev_set = int(DEV_RATIO * num_examples)

	description_file_name = 'description'
	code_file_name = 'code'

	with open(os.path.join(DATA_DIR, 'description.txt'), 'r') as description_all_data:
		with open(os.path.join(output_data_dir, 'description.train.txt'), 'w') as description_training, \
			open(os.path.join(output_data_dir, 'description.dev.txt'), 'w') as description_dev, \
			open(os.path.join(output_data_dir, 'description.test.txt'), 'w') as description_test:

			num_examples_seen_so_far = 0
			for line in description_all_data:
				if num_examples_seen_so_far == num_examples:
					break
				# Write to the training set.
				if num_examples_seen_so_far < num_examples_in_training_set:
					description_training.write(line)
				# Write to the dev set.
				elif num_examples_seen_so_far < num_examples_in_training_set + num_examples_in_dev_set:
					description_dev.write(line)
				# Write to the test set.
				else:
					description_test.write(line)
				num_examples_seen_so_far += 1

	with open(os.path.join(DATA_DIR, 'code.txt'), 'r') as code_all_data:
		with open(os.path.join(output_data_dir, 'code.train.txt'), 'w') as code_training, \
			open(os.path.join(output_data_dir, 'code.dev.txt'), 'w') as code_dev, \
			open(os.path.join(output_data_dir, 'code.test.txt'), 'w') as code_test:

			num_examples_seen_so_far = 0
			for line in code_all_data:
				if num_examples_seen_so_far == num_examples:
					break
				# Write to the training set.
				if num_examples_seen_so_far < num_examples_in_training_set:
					code_training.write(line)
				# Write to the dev set.
				elif num_examples_seen_so_far < num_examples_in_training_set + num_examples_in_dev_set:
					code_dev.write(line)
				# Write to the test set.
				else:
					code_test.write(line)
				num_examples_seen_so_far += 1

# def convert_sentences_back_to_code():
# 	with open(os.path.join(DATA_DIR, 'code_decoded.txt'), 'w') as output: 
# 		with open(os.path.join(DATA_DIR, 'code.txt'), 'r') as solution:
# 			for line in solution:
# 				# line = line.replace(' ' + _INDENT + ' ', '  ')
# 				line = line.replace(' ' + _NEWLINE + ' ', '\n')
# 				output.write(line)

def _format_training_data():
	code_chef_path = os.path.join(DATA_DIR, 'description2code_current', 'codechef')
	code_forces_path = os.path.join(DATA_DIR, 'description2code_current', 'codeforces')

	num_examples = 0

	# Create description.txt and code.txt files
	with open(os.path.join(DATA_DIR, 'description.txt'), 'w') as description_output:
		with open(os.path.join(DATA_DIR, 'code.txt'), 'w') as code_output:

			description_sentence = None
			solution_sentence = None

			for root, dirs, files in os.walk(code_chef_path):
				if root.endswith('description'):
					description_file = files[0] if files else None
					description_sentence = _format_description_into_sentence(root, description_file)

				elif root.endswith('solutions_' + LANGUAGE):
					# Take the first code solution provided and pair it with the description.
					# TODO: Later we can try using more than one solution.
					first_solution_file = files[0] if files else None
					solution_sentence = _format_code_into_sentence(root, first_solution_file)

					# Sometimes there isn't a solution for the given problem. Ignore such problems.
					if description_sentence and solution_sentence:
						description_output.write(description_sentence + '\n')
						code_output.write(solution_sentence + '\n')
						num_examples += 1

	return num_examples

def _format_description_into_sentence(root, description_file):
	"""
	Convert description file into a single sentence string.
	"""
	if not root or not description_file:
		return None

	with open(os.path.join(root, description_file), 'r') as description:
		output_sentence = ''
		for line in description:
			output_sentence += line.rstrip() + ' '
		return output_sentence

def _format_code_into_sentence(root, solution_file):
	"""
	Convert code solution file into a single sentence string.
	"""
	if not root or not solution_file:
		return None

	with open(os.path.join(root, solution_file), 'r') as solution:
		output_sentence = ''
		for line in solution:
			formatted_code_line = _format_code_line(line)
			if formatted_code_line is None:
				return None
			output_sentence += formatted_code_line
		return output_sentence

def _format_code_line(code_line):
	"""
	Edit code line with special _NEWLINE and _INDENT characters
	"""
	if '\0' in code_line:
		return None
	code_line = code_line.replace('\n', ' ')
	# code_line = code_line.replace('  ', ' ' + _INDENT + ' ')
	return code_line

# Run this script to train a model with certain parameters and get data

import os
import sys

# Run this script by passing in num_layers, size, and data_dir as command line arguments




def main():
	# Only have to modify the following two lines of parameters
	num_layers, size, data_dir = sys.argv[1], sys.argv[2], sys.argv[3]

	from_train_data = data_dir + "/description.train.txt"
	to_train_data = data_dir + "/code.train.txt"
	from_dev_data = data_dir + "/description.dev.txt"
	to_dev_data = data_dir + "/code.dev.txt"
	train_dir = "ckpt_" + str(num_layers) + "_" + str(size)

	if not os.path.exists(train_dir):
		os.makedirs(train_dir)

	endOfString = "--data_dir " + data_dir + " --train_dir " + train_dir + " --from_train_data " + \
		from_train_data + " --to_train_data " + to_train_data + " --from_dev_data " + from_dev_data + \
		" --to_dev_data " + to_dev_data + " --num_layers " + num_layers + " --size " + size
	os.system("python3 desc2code.py " + endOfString)
	# os.system("python3 desc2code.py --decode " + endOfString)

main()
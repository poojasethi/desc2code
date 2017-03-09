import data_formatter

def run_tests():
	data_formatter.create_data_set()
	data_formatter.convert_sentences_back_to_code()

def main():
	run_tests()

if __name__ == "__main__":
	main()
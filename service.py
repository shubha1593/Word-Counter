import utils

def read_file_into_list(file_name):
	'''
	Reads the content of given file line by line, as 
	it prevents us from loading the entire file into
	the memory.
	Args:
		file_name (str): file name as a string
	Output:
		file_content (list): List of sentences/lines
			read from the file
	'''
	with open(file_name) as file:
		file_content = []
		for line in file:
			file_content.append(line)

	return file_content

def count_words(file_name):
	# Read the content from the file into a list
	file_content = read_file_into_list(file_name)

	# Pre-process the obtained content to remove the noise
	utils.preprocess_basic(file_content)

	# Form the word cloud
	word_cloud = utils.form_word_cloud(file_content)

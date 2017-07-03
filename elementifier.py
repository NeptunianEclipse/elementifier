import os
from optparse import OptionParser

def init():
	elements = load_list('elements.txt')
	word_list = load_list('dictionary.txt')

	parser = config_parser()

	handle_options(parser, elements)

def config_parser():
	parser = OptionParser(usage = 'Usage: %prog [options] OR %prog [input-string]')
	parser.add_option('-f', '--file', help = 'generate encodings for each line-seperated string in FILE')
	parser.add_option('-d', '--destination', help = 'output result to DESTINATION file')

	return parser


def handle_options(parser, elements):
	(options, args) = parser.parse_args()

	if options.file is not None:
		if len(args) > 0:
			parser.error('[input-string] and any [options] are mutually exclusive')

		if os.path.isfile(options.file):
			print('Generating all possible encodings of all strings in {}'.format(options.file))

			if options.destination is not None:
				print('Output will be put in {}'.format(options.destination))
				dest_path = options.destination

			else:
				print('Output will be put in encodings.txt')
				dest_path = 'encodings.txt'

			save_all_encodings(options.file, dest_path, elements)

			print('Finished')

		else:
			parser.error('option -f: FILE does not exist')

	else:
		if options.destination is not None:
			parser.error('option -d requires option -f')

		try:
			input_str = args[0]
			encodings = encode_in_elements(input_str, elements)

			if len(encodings) > 0:
				print('Found {} possible encodings of \'{}\' in elemental symbols:'.format(len(encodings), input_str))
				print('\n'.join(encodings))

			else:
				print('Found no encodings of \'{}\' in elemental symbols'.format(input_str))

		except IndexError:
			parser.error('no [input-string] or [options] provided')


def save_all_encodings(file_path, dest_path, elements):
	input_list = load_list(file_path)
	all_encodings = encode_all_in_elements(input_list, elements)

	with open(dest_path, 'w') as dest_file:
		if len(all_encodings) > 0:
			for string_encoding in all_encodings:
				dest_file.write(string_encoding[0].lower() + ': ' + ', '.join(string_encoding) + '\n')

		else:
			dest_file.write('No encodings found for all strings in {}'.format(file_path))


# Returns a list of lists of encodings of all strings in the provided string_list
def encode_all_in_elements(string_list, elements):
	all_encodings = []

	for index, word in enumerate(string_list):
		elements_encoding = encode_in_elements(word, elements)

		if len(elements_encoding) > 0:
			all_encodings.append(elements_encoding)

	return all_encodings


# Returns a list of all possible encodings of str in element symbols
def encode_in_elements(str, elements):
	encodings = []
	
	for element in elements:
		if element.lower() == str[:len(element)].lower():
			if len(str) <= len(element):
				encodings.append(element)

			resulting_encodings = encode_in_elements(str[len(element):], elements)

			for encoding in resulting_encodings:
				new_encoding = element + encoding
				encodings.append(new_encoding)
	
	return encodings

# Loads the file at the given path and returns a list of lines
def load_list(path):
	with open(path) as list_file:
		return list_file.read().splitlines()


if __name__ == '__main__':
	init()

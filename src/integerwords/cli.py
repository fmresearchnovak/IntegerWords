
import sys

from .IntegerWords import EnglishInteger

def main():
	if(len(sys.argv) != 2):
		print("Usage: intw <number>")
		sys.exit(1)

	user_input = sys.argv[1]
	user_input = user_input.replace(",", "")
	num = int(user_input)
	print(EnglishInteger(num))
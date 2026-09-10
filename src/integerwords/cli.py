
import os
import sys

from .IntegerWords import EnglishInteger

def main():
	prog = os.path.basename(sys.argv[0]) or "intw"

	if(len(sys.argv) != 2):
		print("Usage: " + prog + " <number>")
		sys.exit(1)

	user_input = sys.argv[1]
	user_input = user_input.replace(",", "")
	num = int(user_input)
	print(EnglishInteger(num))
	
if __name__ == "__main__":
	main()

# IntegerWords
Converts integers to English words.  For example, convert 331002651 to "three hundred thirty one million two thousand six hundred fifty one"

## CLI
Use on the command line

```
user@machine$ python3 IntegerWords.py 331002651
three hundred thirty one million two thousand six hundred fifty one
user@machine$
```
Command line use is the intended use-case.

### Installation
For convenient CLI use I recommending "installing" with the following commands

```
user@machine$ sudo cp IntegerWords.py /usr/local/bin/intw
user@machine$ sudo chmod +x /usr/local/bin/intw
```

Installation makes casual use easy and convenient for example:

```
user@machine$ intw 331002651
three hundred thirty one million two thousand six hundred fifty one 
user@machine$

```





## API
Use as a python3 module

```
import IntegerWords


def main():
	num = 331002651
	print(IntegerWords.EnglishInteger(num))
```




## Details
* Negative numbers are not yet supported.
* Integers only.
* Maximum supported value is 999 decillion followed by subsequent 9's (i.e., 999,999,999,999,999,999,999,999,999,999,999,999)
* This program never outputs the word "and."  For example, when inputting 3001 the output is "three thousand one" not "three thousand and one"  This is acceptable grammar in the United States, but it may seem a bit odd in some cases.  For example, when inputting 3000001 the output is "three million one."  This may seem more awkward then the more colloquial "three million and one", but it is the intended output.
* For documentation about the API consider reading the source code in `IntegerWords.py`
* Inputs with delimiters other than commas are currently not supported (e.g., "331.002.651").

## Pull Requests
Don't like something?  Make a pull request.  This is a very simple project and should be accessible to even beginner programmers.
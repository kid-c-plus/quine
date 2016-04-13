a = "'"
def do():
	y = x()
	print(y + a + y.replace(chr(92), chr(92) * 2).replace(chr(9), chr(92) + "t").replace(chr(10), chr(92) + "n").replace(chr(39), chr(92) + chr(39)) + a + '\ndo()')
def x():
	return 'a = "\'"\ndef do():\n\ty = x()\n\tprint(y + a + y.replace(chr(92), chr(92) * 2).replace(chr(9), chr(92) + "t").replace(chr(10), chr(92) + "n").replace(chr(39), chr(92) + chr(39)) + a + \'\\ndo()\')\ndef x():\n\treturn '
do()

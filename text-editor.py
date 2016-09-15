import os
import sys

text = []
filename = "file.txt"


def open_text(name=filename):
	global text

	f = open(name, "rU")
	text[:] = []
	for line in f:
		text.append(line.replace("\n",""))
	f.close()

def print_text():
	x = 0
	for line in text:
		print(x, line)
		x+=1

def save_text(name=filename):
	f = open(name, "w")
	for line in text:
		f.write(line + "\n")
	f.close()


def interperit(command):
	global text
	global filename
	global auto_print
	command_list = command.split(",")
	
	if command_list[0] == "change":
		text[int(command_list[1])] = command_list[2][1:]
	elif command_list[0] == "open":
		if len(command_list) > 1:
			filename = command_list[1][1:]
			open_text(filename)
		else:
			open_text()
	elif command_list[0] == "save":
		if(len(command_list) > 1):
			save_text(command_list[1][1:])
		else:
			save_text()
	elif command_list[0] == "print":
		if len(command_list) > 1:
			print(text[int(command_list[1])])
		else:
			print_text()
	elif command_list[0] == "nl" or command_list[0] == r"\n" or command_list[0] == "new line":
		text.insert(int(command_list[1]), command_list[2][1:])
	elif command_list[0] == "find":
		if len(command_list) > 2:
			for b in range(int(command_list[2]), len(text)):
				if text[b].find(command_list[1][1:]) != -1:
					print(b, text[b])
		else:
			for b in range(0, len(text)):
				if text[b].find(command_list[1][1:]) != -1:
					print(b, text[b])
	elif command_list[0] == "clear": os.system("cls")


def main():
	os.system("cls")
	global filename

	if len(sys.argv) > 1:
		filename = sys.argv[1]

	global text
	open_text(filename)

	while 1:
		interperit(input(">>>"))

main()
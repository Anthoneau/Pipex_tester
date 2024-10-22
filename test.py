import subprocess
import os
import sys

RED = 31
GREEN = 32
YELLOW = 33
BLUE = 34
MAGENTA = 35
CYAN = 36
BOLD = 1

def print_colored(text, color_code):
    print(f"\033[{color_code}m{text}\033[0m")

def check_pipex_exists():
    if not os.path.exists('./pipex') or not os.access('./pipex', os.X_OK):
        print_colored("Aucun programme n'a été trouvé", f"{RED}")
        sys.exit(1)

def execute_pipex(infile, command1, command2, my_outfile):
	try:
		command = f"./pipex {infile} '{command1}' '{command2}' {my_outfile}"
		result = subprocess.run(command, shell=True, capture_output=True, text=True)
		return result.stdout, result.stderr, result.returncode
	except Exception as e:
		return -1

def execute_shell(infile, command1, command2, real_outfile):
	try:
		command = f"< {infile} {command1} | {command2} > {real_outfile}"
		result = subprocess.run(command, shell=True, stderr=subprocess.DEVNULL)
		return result.returncode
	except Exception as e:
		return -1

def compare_files(file1, file2):
	try:
		with open(file1, 'r') as f1, open(file2, 'r') as f2:
			return f1.read() == f2.read()
	except Exception as e:
		return False

def compare_files(file1, file2):
	try:
		with open(file1, 'r') as f1, open(file2, 'r') as f2:
			f1_lines = f1.readlines()
			f2_lines = f2.readlines()
			for line1, line2 in zip(f1_lines, f2_lines):
				if ("my_outfile.txt" in line1 or "my_outfile.txt" in line2
					or "real_outfile.txt" in line1 or "real_outfile.txt" in line2):
					continue
				if line1 != line2:
					return False
			return True
	except Exception as e:
		return False

def clear_file(file_path):
	with open(file_path, 'w') as f:
		f.write("")

commands_to_test = [
	[" ", "ls -l"],
	["", "ls -l"],
	["cat", "grep Now"],
	["cat", "wc -l"],
	["cat", "ls"],
	["echo Hello", "cat"],
	["", ""],
	[" ", " "],
	["", " "],
	[" ", ""],
	["", "ls"],
	[" ", "ls"],
	["cat", "head -1"],
	[" cat", "     head -1   "],
	[" ", "notexisting"],
]

infile = "infile.txt"
my_outfile = "my_outfile.txt"
real_outfile = "real_outfile.txt"

check_pipex_exists()
for commands in commands_to_test:
	command1 = commands[0]
	command2 = commands[1]
	print_colored(f"Test des commandes: {command1} | {command2}", f"{BOLD};{CYAN}")
	pipex_stdout, pipex_stderr, pipex_returncode = execute_pipex(infile, command1, command2, my_outfile)
	shell_result = execute_shell(infile, command1, command2, real_outfile)
	if compare_files(my_outfile, real_outfile):
		if not pipex_stdout and (pipex_stderr or not pipex_stderr):
			print_colored(f"OK\n", f"{BOLD};{GREEN}")
		elif pipex_stdout:
			print_colored(f"OK\n", f"{BOLD};{YELLOW}")
	else:
		print_colored(f"KO\n", f"{BOLD};{RED}")

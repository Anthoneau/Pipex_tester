import subprocess
import os
import sys
import time

RED = 31
GREEN = 32
YELLOW = 33
BLUE = 34
MAGENTA = 35
CYAN = 36
BOLD = 1

env_to_test = [
	None,
    {},
    {'PATH': ''},
    {'PATH': '/bin:/usr/bin'},
]

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
	["cat", "cat"],
	["/bin/cat", "cat"],
	["cat", "/bin/cat"],
	["/bin/cat", "/bin/cat"],
	["ls -l", "wc -l"],
	["grep a1", "wc -w"],
	["notexisting", "ls -l"],
	["ls -la", "notexisting"],
	["/bin/ls", "bin/notexisting"],
	["ls -l /root", "wc -l"],
	["grep", "wc"],
	["true", "false"],
	["cat /dev/null", "cat"],
	["cat", "od -c"],
	["yes", "head -n 10"],
	["               cat              ", "                 wc                -l"],
	["ls -la --color=always --group-directories-first --time-style=full-iso", "grep .txt"]
]

infiles = [
	["infile.txt"],
	["no_file"],
	["/dev/null"],
	["file_without_perm"]
]

my_outfile = "my_outfile.txt"
real_outfile = "real_outfile.txt"

#print in color
def print_colored(text, color_code):
    print(f"\033[{color_code}m{text}\033[0m")

#Check if the program compile correctly with make re
def check_compile():
	result = subprocess.run('make re -C ..', shell=True)
	if result.returncode == 0:
		return True
	else:
		print_colored("Compilation failed with make re...", f"{RED}")
		sys.exit(1)

#Check the norminette
def norminette():
	result = subprocess.run("norminette ..", shell=True, capture_output=True, text=True)

	error_found = False

	for line in result.stdout.splitlines():
		if "Error" in line:
			error_found = True
			break

	if error_found:
		print_colored("NORM ERROR", f"{BOLD};{RED}")
		return False
	else:
		print_colored("NORM OK", f"{BOLD};{GREEN}")
		return True

#Execute the program
def execute_pipex(infile, command1, command2, my_outfile, env):
	try:
		command = f"../pipex {infile} '{command1}' '{command2}' {my_outfile}"
		#print(f"{command}")
		result = subprocess.run(command, shell=True, capture_output=True, text=True, env=env)
		return result.stdout, result.stderr, result.returncode
	except Exception as e:
		return -1

#Execute the same command in the shell
def execute_shell(infile, command1, command2, real_outfile, env):
	try:
		command = f"< {infile} {command1} | {command2} > {real_outfile}"
		#print(f"{command}")
		result = subprocess.run(command, shell=True, stderr=subprocess.DEVNULL, env=env)
		return result.returncode
	except Exception as e:
		return -1

#Compare the created files
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
					#print(f"my__ : {line1}")
					#print(f"real : {line2}")
					return False
			return True
	except Exception as e:
		print_colored("Files can't be opened !", f"{BOLD};{RED}")
		return False

#Run the program and the shell with different infiles, env and commands
def run_test():
	ok_counter = 0
	ko_counter = 0
	seg_counter = 0
	for infile in infiles:
		print_colored(f"Test with the file : {infile}", CYAN)
		time.sleep(0.5)
		for env in env_to_test:
			print_colored(f"Test with environment : {env}", CYAN)
			time.sleep(0.5)
			for commands in commands_to_test:
				command1 = commands[0]
				command2 = commands[1]
				print_colored(f"Test commands: {command1} | {command2}", f"{BOLD};{CYAN}")
				pipex_stdout, pipex_stderr, pipex_returncode = execute_pipex(infile, command1, command2, my_outfile, env)
				shell_result = execute_shell(infile, command1, command2, real_outfile, env)
				if pipex_returncode == 139:
						print_colored("SEGFAULT\n", f"{BOLD};{RED}")
						seg_counter += 1
				elif compare_files(my_outfile, real_outfile):
					if not pipex_stdout and (pipex_stderr or not pipex_stderr):
						print_colored(f"OK\n", f"{BOLD};{GREEN}")
					elif pipex_stdout:
						print_colored(f"OK\n", f"{BOLD};{YELLOW}")
					ok_counter += 1
				else:
					print_colored(f"KO\n", f"{BOLD};{RED}")
					ko_counter += 1
	if ok_counter > 0:
		print(f"\033[1m\033[32mOK\033[0m : {ok_counter}")
	if ko_counter > 0:
		print(f"\033[1m\033[31mKO\033[0m : {ko_counter}")
	if seg_counter > 0:
		print(f"\033[1m\033[32mSEGFAULT\033[0m : {seg_counter}")

check_compile()
norm = norminette()
time.sleep(1)
subprocess.check_call(['touch','file_without_perm'])
subprocess.check_call(['chmod','000','file_without_perm'])
run_test()
if norm == True:
	print_colored("NORM OK", f"{BOLD};{GREEN}")
else:
	print_colored("NORM ERROR", f"{BOLD};{RED}")
print_colored("MAKE OK", f"{BOLD};{GREEN}")
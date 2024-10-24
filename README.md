Little tester for pipex.

Check the norm, the compilation and different commands.
Also check the program's error messages. If they're in stdout and the tests work, an OK will be written in yellow.

List of the infiles :

- infile.txt
- non existant file
- /dev/null, which does not contain any information
- file_without_perm, which is a created file from the program with 0 permission

List of the environment tested :
- Default
- None
- PATH': ''
- PATH': '/bin:/usr/bin'

List of the commands tested :
- " ", "ls -l"
- "", "ls -l"
- "cat", "grep Now"
- "cat", "wc -l"
- "cat", "ls"
- "echo Hello", "cat"
- "", "
- " ", " "
- "", " "
- " ", ""
- "", "ls"
- " ", "ls"
- "cat", "head -1"
- " cat", "     head -1   "
- " ", "notexisting"
- "cat", "cat"
- "/bin/cat", "cat"
- "cat", "/bin/cat"
- "/bin/cat", "/bin/cat"
- "ls -l", "wc -l"
- "grep a1", "wc -w"
- "notexisting", "ls -l"
- "ls -la", "notexisting"
- "/bin/ls", "bin/notexisting"
- "ls -l /root", "wc -l"
- "grep", "wc"
- "true", "false"
- "cat /dev/null", "cat"
- "cat", "od -c"
- "yes", "head -n 10"
- "               cat              ", "                 wc                -l"
- "ls -la --color=always --group-directories-first --time-style=full-iso", "grep .txt"

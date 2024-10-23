Petit tester pour pipex, très simple.

Tests :
- norminette
- " " "ls -l"
- "" "ls -l"
- "cat" "grep Now"
- "cat" "wc -l"
- "cat" "ls"
- "echo Hello" "cat"
- "" ""
- " " " "
- "" " "
- " " ""
- "" "ls"
- " " "ls"
- "cat" "head -1"
- " cat" "     head -1   "
- " " "notexisting"
- "cat" "cat"
- "/bin/cat" "cat"
- "cat" "/bin/cat"
- "/bin/cat" "/bin/cat"

Si du texte est renvoyé par le programme et qu'il n'est pas écrit dans le stderr, un OK jaune sera écrit si les tests sont bons.

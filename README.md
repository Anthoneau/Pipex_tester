<a id="readme-top"></a>

# Little tester for pipex.

<p>Check the norm, the compilation and different commands.</p>
<p>Also check the program's error messages. If they're in stdout and the tests work, an OK will be written in yellow.</p>

<p><b>DOES NOT CHECK THE LEAKS !</b></p>

## Installation

1. Clone the repo
   ```sh
   git clone https://github.com/Anthoneau/pipex_tester
   ```
2. Enter in it
   ```sh
   cd pipex_tester/
   ```
4. Launch the tester
   ```sh
   python3 test.py
   ```

## Important note ⚠️

<p>This tester is provided to help you avoid redundancy when writing tests every time you modify the Pipex project.</p>
<p>However, it is crucial to create and validate your own specific tests to ensure full coverage of your code.</p>
<p>This tester is a support tool and does not replace the personal consideration required to design appropriate test cases for your project.</p>
<p>Be sure to adapt your tests according to your specific needs.</p>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## List of the infiles :

<ul>
  <li>infile.txt</li>
  <li>non existant file</li>
  <li>/dev/null</li>
  <p>- which does not contain any information</p>
  <li>file_without_perm</li>
  <p>- which is a created file from the program with 0 permission</p>
</ul>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## List of the environment tested :
<ul>
  <li>Default</li>
  <li>None</li>
  <li>PATH': ''</li>
  <li>PATH': '/bin:/usr/bin'</li>
</ul>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## List of the commands tested :
<ul>
  <li>" ", "ls -l"</li>
  <li>"", "ls -l"</li>
  <li>"cat", "grep Now"</li>
  <li>"cat", "wc -l"</li>
  <li>"cat", "ls"</li>
  <li>"echo Hello", "cat"</li>
  <li>"", "</li>
  <li>" ", " "</li>
  <li>"", " "</li>
  <li>" ", ""</li>
  <li>"", "ls"</li>
  <li>" ", "ls"</li>
  <li>"cat", "head -1"</li>
  <li>" cat", "     head -1   "</li>
  <li>" ", "notexisting"</li>
  <li>"cat", "cat"</li>
  <li>"/bin/cat", "cat"</li>
  <li>"cat", "/bin/cat"</li>
  <li>"/bin/cat", "/bin/cat"</li>
  <li>"ls -l", "wc -l"</li>
  <li>"grep a1", "wc -w"</li>
  <li>"notexisting", "ls -l"</li>
  <li>"ls -la", "notexisting"</li>
  <li>"/bin/ls", "bin/notexisting"</li>
  <li>"ls -l /root", "wc -l"</li>
  <li>"grep", "wc"</li>
  <li>"true", "false"</li>
  <li>"cat /dev/null", "cat"</li>
  <li>"cat", "od -c"</li>
  <li>"yes", "head -n 10"</li>
  <li>"               cat              ", "                 wc                -l"</li>
  <li>"ls -la --color=always --group-directories-first --time-style=full-iso", "grep .txt"</li>
</ul>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

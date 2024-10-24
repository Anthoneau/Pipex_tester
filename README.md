<a id="readme-top"></a>

# Little tester for pipex.

<p>Check the norm, the compilation and different commands.</p>
<p>Also check the program's error messages. If they're in stdout and the tests work, an OK will be written in yellow.</p>

<p><b>DOES NOT CHECK THE LEAKS !</b></p>

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="Installation">Installation</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

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
  <p><li>infile.txt</li></p>
  <p><li>non existant file</li></p>
  <li>/dev/null</li>
  <p>- which does not contain any information</p>
  <li>file_without_perm</li>
  <p>- which is a created file from the program with 0 permission</p>
</ul>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## List of the environment tested :
<ul>
  <p><li>Default</li></p>
  <p><li>None</li></p>
  <p><li>PATH: ""</li></p>
  <p><li>PATH: /bin:/usr/bin</li></p>
</ul>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## List of the commands tested :
<ul>
  <p><li>" " | ls -l</li></p>
  <p><li>"" | ls -l</li></p>
  <p><li>cat | grep Now</li></p>
  <p><li>cat | wc -l</li></p>
  <p><li>cat | ls</li></p>
  <p><li>echo Hello | cat</li></p>
  <p><li>"" | ""</li></p>
  <p><li>" " | " "</li></p>
  <p><li>"" | " "</li></p>
  <p><li>" " | ""</li></p>
  <p><li>"" | ls</li></p>
  <p><li>" " | ls</li></p>
  <p><li>cat | head -1</li></p>
  <p><li>" cat" | "     head -1   "</li></p>
  <p><li>" " | notexisting</li></p>
  <p><li>cat | cat</li></p>
  <p><li>/bin/cat | cat</li></p>
  <p><li>cat | /bin/cat</li></p>
  <p><li>/bin/cat | /bin/cat</li></p>
  <p><li>ls -l | wc -l</li></p>
  <p><li>grep a1 | wc -w</li></p>
  <p><li>notexisting | ls -l</li></p>
  <p><li>ls -la | notexisting</li></p>
  <p><li>/bin/ls | bin/notexisting</li></p>
  <p><li>ls -l /root | wc -l</li></p>
  <p><li>grep | wc</li></p>
  <p><li>true | false</li></p>
  <p><li>cat /dev/null | cat</li></p>
  <p><li>cat | od -c</li></p>
  <p><li>yes | head -n 10</li></p>
  <p><li>"               cat              " | "                 wc                -l"</li></p>
  <p><li>ls -la --color=always --group-directories-first --time-style=full-iso | grep .txt</li></p>
</ul>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

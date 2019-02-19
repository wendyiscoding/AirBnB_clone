# :shell: 0x00. AirBnB clone - The console :shell:

In this project, we will be developing the console for our airbnb project. This console will be written in Python3 and will be used for communication between our webapp, static content, databases, and filesystem.

## :running: Getting Started

* [Ubuntu 14.04 LTS](http://releases.ubuntu.com/14.04/) - Operating system reqd.

* [GCC 4.8.4](https://gcc.gnu.org/gcc-4.8/) - Compiler used


## :warning: Prerequisites

* Must have `git` installed

* Must have repository cloned

* Must have `python` installed

```
$ sudo apt-get install git
```
```
$ sudo apt-get install python3-pep8
```
To run the command interpreter:
```
$ ./console.py
```

## Example
Interactive mode:
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb)
(hbnb) help EOF
EOF command to exit the program
(hbnb)
(hbnb) help all
Prints list of strings of all instances, regardless of class
(hbnb)
(hbnb) help create
Create command to create and store objects
(hbnb)
(hbnb) help destroy
Destroy command to delete an instance
(hbnb)
(hbnb) help help
List available commands with "help" or detailed help with "help cmd".
(hbnb)
(hbnb) help quit
Quit command to exit the program
(hbnb)
(hbnb) help show
Show command to print string representation of an instance
(hbnb)
(hbnb) help update
Update instance based on cls name & id by adding or updating attr
(hbnb) 
(hbnb)
(hbnb) quit
$
```
Non-interactive mode
```
$ echo "help" | ./console.py
(hbnb)


Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update
(hbnb) 
$
```

## :blue_book: Authors
* **Bennett Dixon** - [@BennettDixon](https://github.com/BennettDixon)
* **Wendy Leung** - [@wendyiscoding](https://github.com/wendyiscoding)

## :mag: License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/BennettDixon/holbertonschool-lower_level_programming/blob/master/LICENSE.md) file for details



## :mega: Acknowledgments

* Holberton School (providing guidance)

#!/usr/bin/python3
"""console module
"""
import cmd
import re
import shlex

class HBNBCommand(cmd.Cmd):
    """class HBNBCommand
    """
    prompt = '(hbnb) '

    def do_EOF(self, args):
        """EOF command to exit the program
        """
        return True

    def do_quit(self, args):
        """Quit command to exit the program
        """
        return True

    def emptyline(self):
        pass

    def postloop(self):
        print()

if __name__ == '__main__':
    HBNBCommand().cmdloop()

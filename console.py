#!/usr/bin/python3
"""
command line console
"""
import cmd

class HBNBCommand(cmd.Cmd):
    """
    class for console
    """
    intro = 'Welcome to the jason shell. Type help or ? to list commands.\n'
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """quit the console"""
        exit()

    def do_EOF(self, arg):
        """at eof, quit console"""
        exit()

if __name__ == '__main__':
    HBNBCommand().cmdloop()

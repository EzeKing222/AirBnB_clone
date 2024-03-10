#!/usr/bin/python3
"""
A simple line-oriented command interpreter
"""
import cmd


class HBNBCommand(cmd.Cmd):

    '''
    A simple line-oriented command interpreter.
    '''
    def __init__(self, completekey: str = "tab"):
        '''
        Instantiate a line-oriented interpreter.

        Args:
        completekey: is the readline name of a completion key
        it defaults to the Tab key. If completekey is not None and
        the readline module is available,
        command completion is done automatically.
        '''
        super().__init__(completekey)

    def do_quit(self, line):
        '''
        Quit command to exit the program
        '''
        return True

    def do_EOF(self, line):
        '''
        End Of File
        '''
        return True

    prompt = '(hbnb) '


if __name__ == '__main__':
    HBNBCommand().cmdloop()

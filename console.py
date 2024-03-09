#!/usr/bin/python3


import cmd
from typing import IO

class Commands(cmd.Cmd):
        '''
        A simple line-oriented command interpreter.
        '''
        def __init__(self, completekey: str = "tab", stdin: IO[str] | None = None, stdout: IO[str] | None = None) -> None:
                '''
                Instantiate a line-oriented interpreter.

                Args:
                completekey: is the readline name of a completion key
                        it defaults to the Tab key. If completekey is not None and the readline module is available,
                        command completion is done automatically.
                stdin and stdout: specify alternate input and output file objects; if not specified,
                        sys.stdin and sys.stdout are used.
                '''
                super().__init__(completekey, stdin, stdout)

        def do_exit(self, line):
                '''
                provides the exit command to abort the interpreter.
                '''
                return True

        def do_EOF(self, line):
                '''
                End Of File
                '''
                return True

        def postloop(self) -> None:
                print()
        #aliasing
        do_quit = do_exit

        prompt = '(hbnb) '

Commands().cmdloop()
#print (Commands.__doc__)
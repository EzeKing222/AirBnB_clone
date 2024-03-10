#!/usr/bin/python3
"""
A simple line-oriented commands interpreter
"""
import cmd
import shlex
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):

    '''
    A simple line-oriented commands interpreter.
    '''
    def __init__(self, completekey: str = "tab"):
        '''
        Instantiate a line-oriented interpreter.

        Args:
        completekey: is the readline name of a completion key
        it defaults to the Tab key. If completekey is not None and
        the readline module is available,
        commands completion is done automatically.
        '''
        super().__init__(completekey)

    prompt = '(hbnb) '
    valid_classes = ['BaseModel']

    def do_quit(self, line):
        '''
        Quit commands to exit the program
        '''
        return True

    def do_EOF(self, line):
        '''
        Handle End-Of-File (Ctrl-D) to exit the program
        '''

        print()
        return True

    def help_quit(self):
        '''
        Quit commands to exit the program
        '''
        print('Quit commands to exit the program')

    def empty_line(self):
        """
        Do nothing
        """

        pass

    def do_create(self, line):
        """
        create a new instanse of BaseModel
        Usage: create <class_name>
        """

        commands = shlex.split(line)

        if len(commands) == 0:
            print('** class name missing **')
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, line):
        """
        Show the string representation of an instance
        Usage: show <class_name> <id>
        """

        commands = shlex.split(line)

        if len(commands) == 0:
            print('** class name missing **')
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print('** instance id missing **')
        else:
            objects = storage.all()

        key = f'{commands[0]}.{commands[1]}'

        if key in objects:
            print(objects[key])
        else:
            print('** no instance found **')

    def do_destroy(self, line):
        """
        destroy an instance
        Usage: destroy <class_name> <id>
        """

        commands = shlex.split(line)

        if len(commands) == 0:
            print('** class name missing **')
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print('** instance id missing **')
        else:
            objects = storage.all()

        key = f'{commands[0]}.{commands[1]}'

        if key in objects:
            del objects[key]
            storage.save()
        else:
            print('** no instance found **')

    def do_all(self, line):
        """
        print the string representation of all instance
        Usage: all [class_name]
        """

        objects = storage.all()

        commands = shlex.split(line)

        if len(commands) == 0:
            for key, value in object.items():
                print(str(value))
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            for key, value in object.items():
                if key.split('.')[0] == commands[0]:
                    print(str(value))

    def do_update(self, line):
        """
        update an instance by adding or udating an attribute
        Usage: update <class_name> <id> <attribute_name> "<attribute_value>
        """

        commands = shlex.split(line)

        if len(commands) == 0:
            print('** class name missing **')
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print('** instance id missing **')
        else:
            objects = storage.all()

            key = f'{commands[0]}.{commands[1]}'

            if key not in objects:
                print('** no instance found **')
            elif len(commands) < 3:
                print('** attribute name missing **')
            elif len(commands) < 4:
                print('** value missing **')
            else:
                obj = objects[key]

                attribute_name = commands[2]
                attribute_value = commands[3]

                try:
                    attribute_value = eval(attribute_value)
                except Exception:
                    pass
                setattr(obj, attribute_name, attribute_value)

                obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()

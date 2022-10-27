#!/usr/bin/python3
"""
command line console
"""
import cmd
import json
import sys
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage

class HBNBCommand(cmd.Cmd):
    """
    class for console
    """
    intro = 'Welcome to the jason shell. Type help or ? to list commands.\n'
    prompt = '(hbnb) '

    arg_classes = ['BaseModel']

    def do_quit(self, arg):
        """quit the console"""
        exit()

    def do_EOF(self, arg):
        """at eof, quit console"""
        return True

    def do_create(self, class_arg):
        """
        creates an instance
        :param class_arg: argument which is usually
        a class name
        """
        if class_arg:
            if class_arg in self.arg_classes:
                new_model = BaseModel()
                new_model.save()
                print(new_model.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, arg):
        """
        shows what a str representation of the id
        """
        arg_list = arg.split()
        if arg_list[0] not in self.arg_classes:
            print("** class doesn't exist **")
        elif len(arg_list) < 0:
            print("** class name missing **")
        elif len(arg_list) < 2:
            print("** instance id missing **")
        else:
            try:
                obj_dictionary = storage.all()
                #return file storage objects dictionary
                key_name = arg_list[0] + "." + arg_list[1]
                print(obj_dictionary[key_name])
            except KeyError:
                print("** no instance found **")

    def do_destroy(self, arg):
        """
        deletes an instance
        """
        arg_list = arg.split()
        if arg_list[0] not in self.arg_classes:
            print("** class doesn't exist **")
        elif len(arg_list) < 0:
            print("** class name missing **")
        elif len(arg_list) < 2:
            print("** instance id missing **")
        else:
            try:
                obj_dictionary = storage.all()
                #return file storage objects dictionary
                key_name = arg_list[0] + "." + arg_list[1]
                del obj_dictionary[key_name]
                storage.save()
            except KeyError:
                print("** no instance found **")

    def do_all(self, args):
        """prints all """
        arg_list = args.split()
        if len(arg_list) == 0:
            obj_dict = storage.all()
            for k, v in obj_dict.items():
                print(obj_dict[k])
        if len(arg_list) > 0:
            if arg_list[0] not in self.arg_classes:
                print("** class doesn't exist **")
            else:
                obj_dict = storage.all()
                for k, v in obj_dict.items():
                    print(obj_dict[k])



if __name__ == '__main__':
    HBNBCommand().cmdloop()
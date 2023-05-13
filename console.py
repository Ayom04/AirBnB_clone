#!/usr/bin/python3
""" Defining the console """

import cmd
import re
import sys
import models
from models.base_model import BaseModel
from models.__init__ import storage
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
import shlex


class HBNBCommand(cmd.Cmd):
    """ Contains the command for the HBNB console"""

    prompt = '(hbnb) ' if sys.__stdin__.isatty() else ''

    classes = {
               'BaseModel': BaseModel, 'User': User, 'Place': Place,
               'State': State, 'City': City, 'Amenity': Amenity,
               'Review': Review
              }
    dot_cmds = ['all', 'count', 'show', 'destroy', 'update']
    types = {
             'number_rooms': int, 'number_bathrooms': int,
             'max_guest': int, 'price_by_night': int,
             'latitude': float, 'longitude': float
            }

    def preloop(self):
        """Prints if isatty is false"""
        if not sys.__stdin__.isatty():
            print('(hbnb)')

    def precmd(self, line):
        """Reformat command line for advanced command syntax."""

        __cmd = _cls = _id = _args = ''

        # scanning for general formating - i.e '.', '(', ')'
        if not ('.' in line and '(' in line and ')' in line):
            return line

        try:
            _pline = line[:]

            _cls = _pline[:_pline.find('.')]

            __cmd = _pline[_pline.find('.') + 1:_pline.find('(')]
            if __cmd not in HBNBCommand.dot_cmds:
                raise Exception

            _pline = _pline[_pline.find('(') + 1:_pline.find(')')]
            if _pline:
                _pline = _pline.partition(', ')
                _id = _pline[0].replace('\"', '')

                _pline = _pline[2].strip()
                if _pline:
                    if _pline[0] == '{' and _pline[-1] == '}'\
                            and type(eval(_pline)) is dict:
                        _args = _pline
                    else:
                        _args = _pline.replace(',', '')
            line = ' '.join([__cmd, _cls, _id, _args])

        except Exception as mess:
            pass
        finally:
            return line

    def postcmd(self, stop, line):
        """Prints if isatty is false"""
        if not sys.__stdin__.isatty():
            print('(hbnb) ', end='')
        return stop

    def do_quit(self, arg):
        """ Method to exit the HBNB console"""
        exit()

    def help_quit(self):
        """ Prints the help docs for quit  """
        print("Exit the program with formatting\n")

    def do_EOF(self, arg):
        """ Handles EOF to exit program """
        print()
        exit()

    def help_EOF(self):
        """ Prints the help docs for EOF """
        print("Exits the program without formatting\n")

    def emptyline(self):
        """ Overrides the emptyline method of CMD """
        pass

    def do_create(self, args):
        """ Create an object of any class"""
        if not args:
            print("** class name missing **")
            return
        elif args not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        new_instance = HBNBCommand.classes[args]()
        storage.save()
        print(new_instance.id)
        storage.save()

    def help_create(self):
        """ Help information for the create method """
        print("Creates a class of any type")
        print("[Usage]: create <className>\n")

    def do_show(self, args):
        """ Method to show an individual object """
        new = args.partition(" ")
        class_name = new[0]
        class_id = new[2]

        if class_id and ' ' in class_id:
            c_id = class_id.partition(' ')[0]

        if not class_name:
            print("** class name missing **")
            return

        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if not class_id:
            print("** instance id missing **")
            return

            key = class_name + "." + class_id
            try:
                print(storage._FileStorage__objects[key])
            except KeyError:
                print("** no instance found **")

    def help_show(self):
        """ Help information for the show command """
        print("Shows an individual instance of a class")
        print("[Usage]: show <className> <objectId>\n")


if __name__ == "__main__":
    HBNBCommand().cmdloop()

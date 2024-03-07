#!/usr/bin/env python3
"""
This module implements a command interpreter using the cmd module.
"""
import pdb
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.review import Review
from models.place import Place


class HBNBCommand(cmd.Cmd):
    """ define prompt"""

    prompt = '(hbnb) '
    class_list = [
        'BaseModel', 'FileStorage', 'User', 'State', 'Review',
        'Amenity', 'Place', 'City'
    ]

    storage = FileStorage()
    storage.reload()

    def do_quit(self, arg):
        """quit cmd"""
        return True

    def do_EOF(self, arg):
        """ EOF end """
        print()
        return True

    def emptyline(self):
        """ do nothing"""
        pass

    def do_create(self, arg):

        if len(arg) == 0:
            print("** class name missing **")
        elif arg not in HBNBCommand.class_list:
            print("** class doesn't exist **")
        else:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """ show """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")

        elif args[0] not in HBNBCommand.class_list:
            print("** class doesn't exist **")

        elif len(args) == 1:
            print("** instance id missing **")

        else:
            try:
                show_obj = HBNBCommand.storage.all()[args[0] + '.' + args[1]]

            except KeyError:
                print("** no instance found **")
            else:
                print(show_obj)

    def do_destroy(self, arg):
        """Destroy instance"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.class_list:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            try:
                objects = storage.all()
                string = "{}.{}".format(args[0], args[1])
                del objects[string]
                storage.save()
            except KeyError:
                print("** no instance found **")

    def do_all(self, arg):
        """Print all instances"""
        objects = self.storage.all()
        if arg not in HBNBCommand.class_list and len(arg) > 0:
            print("** class doesn't exist **")
            return

        if len(arg) == 0:
            obj_list = list(objects.values())
        else:
            obj_list = [valu for valu in objects.values()
                        if valu.__class__.__name__ == arg]

        for obj in obj_list:
            obj_str = "[{}] ({}) {}".format(
                obj.__class__.__name__,
                obj.id,
                obj.to_dict()
            )
            print(obj_str)

    def do_update(self, arg):
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.class_list:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            try:
                obj = HBNBCommand.storage.all()[args[0] + '.' + args[1]]
            except KeyError:
                print("** no instance found **")
                return
            if len(args) == 2:
                print("** attribute name missing **")
            elif len(args) == 3:
                print("** value missing **")
            else:
                setattr(obj, args[2], args[3])
                storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()

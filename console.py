#!/usr/bin/python3
"""console module
"""
import cmd
import models
import shlex
from models.base_model import BaseModel
from models.city import City
from models.state import State
from models.user import User


class HBNBCommand(cmd.Cmd):
    """class HBNBCommand
    """
    prompt = '(hbnb) '
    class_list = ['BaseModel', 'User', 'State', 'City']

    def do_EOF(self, args):
        """EOF command to exit the program
        """
        return True

    def do_quit(self, args):
        """Quit command to exit the program
        """
        return True

    def do_create(self, line):
        """create command to create and store objects
        """
        args = line.split()
        if not self.verify_class(args):
            return
        inst = eval(str(args[0]) + '()')
        if not isinstance(inst, BaseModel):
            return
        inst.save()
        print(inst.id)

    def do_show(self, line):
        """show command to print string representation of an instance
        """
        args = line.split()
        if not self.verify_class(args):
            return
        if not self.verify_id(args):
            return
        string_key = str(args[0]) + '.' + str(args[1])
        objects = models.storage.all()
        print(objects[string_key])

    def do_destroy(self, line):
        """destroy command to delete an instance
        """
        args = line.split()
        if not self.verify_class(args):
            return
        if not self.verify_id(args):
            return
        string_key = str(args[0]) + '.' + str(args[1])
        objects = models.storage.all()
        models.storage.delete(objects[string_key])
        models.storage.save()

    def do_all(self, line):
        """prints all string rep of all instances based or not on class name"""
        args = line.split()
        objects = models.storage.all()
        print_list = []
        if len(args) == 0:
            # print all classes
            for value in objects.values():
                print_list.append(str(value))
        elif args[0] in self.class_list:
            # print just arg[0] class instances
            for (key, value) in objects.items():
                if args[0] in key:
                    print_list.append(str(value))
        else:
            print("** class doesn't exist **")
            return False
        print(print_list)

    def do_update(self, line):
        """update instance based on cls name & id by adding or updating attr
        """
        args = shlex.split(line)
        if not self.verify_class(args):
            return
        if not self.verify_id(args):
            return
        if not self.verify_attribute(args):
            return
        string_key = str(args[0]) + '.' + str(args[1])
        objects = models.storage.all()
        my_dict = objects[string_key].to_dict()
        attr_name = args[2]
        attr_value = args[3]
        for (key, value) in my_dict.items():
            if attr_name is key:
                attr_value = eval('({}){}'.format(type(value), attr_value))
        setattr(objects[string_key], attr_name, attr_value)
        objects[string_key].save()

    @classmethod
    def verify_class(cls, args):
        """verify class
        """
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] not in cls.class_list:
            print("** class doesn't exist **")
            return False
        return True

    @staticmethod
    def verify_id(args):
        """verify id
        """
        if len(args) < 2:
            print("** instance id missing **")
            return False
        objects = models.storage.all()
        string_key = str(args[0]) + '.' + str(args[1])
        if string_key not in objects.keys():
            print("** no instance found **")
            return False
        return True

    @staticmethod
    def verify_attribute(args):
        """verify attribute
        """
        if len(args) < 3:
            print("** attribute name missing **")
            return False
        if len(args) < 4:
            print("** value missing **")
            return False
        return True

    def emptyline(self):
        pass

    def postloop(self):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()

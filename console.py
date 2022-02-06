#!/usr/bin/python3
"""Doc stuff"""
import cmd

from models.engine.file_storage import FileStorage
from models.__init__ import storage
from models import *
import sys


class HBNBCommand(cmd.Cmd):
    """Shell for AirBnB"""

    if not sys.__stdin__.isatty():
            prompt = '(hbnb) ' + '\n'
    else:
        prompt = '(hbnb) '

    def emptyline(self):
        pass

    def do_quit(self, inp):
        "Exits the shell"
        return True

    def do_create(self, inp):
        "Creates a new instance of a class and saves it \
(to the JSON file) and prints the id. Ex: $ create BaseModel"

        if inp == "":
            print("** class name missing **")
        else:
            try:
                class_model = globals()[inp]
                obj = class_model()
                obj.save()
                print(obj.id)
            except:
                print("** class doesn't exist **")

    def do_show(self, inp):
        "Prints the string representation of an instance based \
on the class name and id. Ex: $ show BaseModel 1234-1234-1234"

        flag = 1
        if inp == "":
            print("** class name missing **")
            flag = 0
        else:
            inp = inp.split(" ")

        if flag == 1:
            if inp[0] not in ("BaseModel", "User", "State",
                              "Review", "Place", "City", "Amenity"):
                print("** class doesn't exist **")
            else:
                if len(inp) == 1:
                    print("** instance id missing **")
                else:
                    key = ".".join(inp)
                    objects = storage.all()
                    try:
                        print(objects[key])
                    except:
                        print("** no instance found **")

    def do_destroy(self, inp):
        "Deletes an instance based on the class name and id"

        flag = 1
        if inp == "":
            print("** class name missing **")
            flag = 0
        else:
            inp = inp.split(" ")

        if flag == 1:
            if inp[0] not in ("BaseModel", "User", "State",
                              "Review", "Place", "City", "Amenity"):
                print("** class doesn't exist **")
            else:
                if len(inp) == 1:
                    print("** instance id missing **")
                else:
                    key = ".".join(inp)
                    objects = storage.all()
                    try:
                        del(objects[key])
                        storage.save()
                    except:
                        print("** no instance found **")

    def do_all(self, inp):
        "Prints all string representation of all \
instances based or not on the class name."
        objects = storage.all()
        my_list = []
        flag = 0
        if len(inp) != 0:
            flag = 1
        if flag == 1 and inp not in ("BaseModel", "User", "State",
                                     "Review", "Place", "City", "Amenity"):
                print("** class doesn't exist **")
        else:
            for obj_id in objects.keys():
                if inp:
                    tmp = obj_id.split(".")
                    if tmp[0] == inp:
                        obj = objects[obj_id]
                        my_list.append(str(obj))
                else:
                    obj = objects[obj_id]
                    my_list.append(str(obj))
            if len(my_list) != 0:
                print(my_list)

    def do_update(self, inp):
        "Updates an instance based on the class \
name and id by adding or updating attribute"

        flag = 1

        if inp == "":
            print("** class name missing **")
            flag = 0
        else:
            inp = inp.split(" ")

        if flag == 1:
            if inp[0] not in ("BaseModel", "User", "State",
                              "Review", "Place", "City", "Amenity"):
                print("** class doesn't exist **")
            else:
                if len(inp) == 1:
                    print("** instance id missing **")
                else:
                    key = inp[0] + "." + inp[1]
                    objects = storage.all()
                    try:
                        new_dict = objects[key]
                        if len(inp) < 3:
                            print("** attribute name missing **")
                        else:
                            if len(inp) < 4:
                                print("** value missing **")
                            else:
                                value = \
                                    inp[3].replace("\"", "").replace("\'", "")
                                setattr(new_dict, inp[2], value)
                                storage.save()
                    except:
                        print("** no instance found **")

    do_EOF = do_quit
    """ctrl + d"""

if __name__ == '__main__':
    HBNBCommand().cmdloop()

#!/usr/bin/python3
"""Doc stuff"""
import cmd, sys


class HBNBCommand(cmd.Cmd):
    """Shell"""
    prompt = '(hbnb) '

    def emptyline(self):
        pass

    def do_quit(self, inp):
        "Exits the shell"
        return True

    def do_create(self, inp):
        "Creates a new instance of BaseModel, saves it \
(to the JSON file) and prints the id. Ex: $ create BaseModel"
        print("Hello")

    def do_show(self, inp):
        "Prints the string representation of an instance based \
on the class name and id. Ex: $ show BaseModel 1234-1234-1234"
        print("Hello")

    def do_destroy(self, inp):
        "Deletes an instance based on the class name and id"
        pass

    def do_all(self, inp):
        "Prints all string representation of all \
instances based or not on the class name."
        pass

    def do_update(self, inp):
        "Updates an instance based on the class \
name and id by adding or updating attribute"
        pass

    do_EOF = do_quit

if __name__ == '__main__':
    HBNBCommand().cmdloop()
"""
    Author:Jarvis Lu
    Date: 2/27/2020

    This file is created to test the program. Commands are passed in directly
since voice recongization haven't been implemented

"""
from project_management import command_central
import file_io
import time
import fileinput
from os.path import expanduser
import platform
from file_io import listen

command = command_central.CommandCentral(platform.system())
command.create_new_project(["Desktop", "test"])

# test = listen.Listen()
# print(test.auto_correct("ab"))
# print(test.auto_correct("mudifa"))
# print(test.auto_fill("del"))

command.add_file("hello_world.c")

command.add_include("stdio.h")
command.add_include("string.h")
command.add_func("main", "int", "definition")
command.add_to_func_body("add,call,printf,add,call,printf,modify,add, \"Hello world! %d\\n\"")
# command.add_to_func_body("add", "call", value= "printf")





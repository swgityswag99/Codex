
""""
    Author:Jarvis Lu
    Date: 2/27/2020

    This file is created as a method to test the program. Use this file on a windows
platform

""""
from project_management import command_central
import time
import fileinput
from os.path import expanduser

home = expanduser("~")
print(home)
command = command_central.CommandCentral()
command.create_new_project(home + "/Desktop/test")
command.add_file("hello_world.c")
# command.add_include("stdio.h")
# command.add_func("main", "int", "definition")
# # time.sleep(1)
# command.add_to_func_body("add", "call", value= "printf")
# # time.sleep(1)
# command.add_to_func_body("modify", "add", value= "\"Hello world! %d\\n\"")
# # time.sleep(1)
# command.add_to_func_body("add", "call", value= "printf")
# # time.sleep(1)
# command.add_to_func_body("modify", "add", value= "\"testing!!\\n\"")
# # time.sleep(1)
# command.add_to_func_body("add", "call", value= "printf")
# # time.sleep(1)
# command.add_to_func_body("modify", "add", value= "\"One more\\n\"")
# # time.sleep(1)
# command.add_to_func_body("add", "variable", value= "yes")
# # time.sleep(1)
# command.add_to_func_body("modify", "type", value= "int")
# # time.sleep(1)
# command.add_to_func_body("modify", "value", value= 10)
# # time.sleep(1)
# command.add_to_func_body("add", "variable", value= "no")
# # time.sleep(1)
# command.add_to_func_body("modify", "type", value="int")
# command.add_to_func_body("add", "variable", value= "test")
# # time.sleep(1)
# command.add_to_func_body("modify", "type", value="int")
# # time.sleep(1)
# command.add_to_func_body("modify", "value", value= 20)
# command.add_to_func_body("add", "call", value="printf")
# command.add_to_func_body("modify", "add", value= "\"one and one more\\n\"")
# command.add_to_func_body("modify", "add", line= 5, value="yes")
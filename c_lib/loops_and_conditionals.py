from . import calls

"""
    Author:Nicolas Stefanelli, Jarvis Lu, and Rylee Bers
    Last modified 6/14/20

    This file contains the IfElse class. This class can be used to implement 
if else statements within the file.

"""
class loops_and_conditionals_parent:
    def __init__(self):
        self.variable_dict = {}
        self.argument_list = []
        self.tracker = []
        self.current_action = None

    def generate_output(self):
        pass

    """ 
        Return the function that contains the given line. 
        @param line The line requested by the user. 
    """ 
    def return_action_at_line(self, line):
        #Current line starts at 1 because for functions and loops and conditions
        #the first line is always taken up
        current_line = 1
        last_line = 0
        if self.tracker:
            for token in self.tracker:
                current_line = current_line + token.return_num_lines()
                if line < current_line and line >= last_line:
                    self.current_action = token
                    return last_line
                last_line = current_line
        
    def return_num_lines(self):
        num_line = 0
        for token in self.tracker:
            num_line = num_line + token.return_num_lines()
        return num_line + 2

    """ 
        Add content to the body of a function
        @param action_type can be either add or modify 
        @param name can be add for adding content to a line inside a function
            or modify for change the content of an existing line inside a function
            or Variable to add a variable inside the function
            or call to add a call inside the function
        @param line Use this parameter if a specific item at a line needs to be modified
        @param value this paramter can be used to change a function by its name 
    """      
    def add_to_body(self, command_block):
        if command_block.line != None:
            command_block.line = command_block.line - self.return_action_at_line(command_block.line)
        if isinstance(self.current_action, loops_and_conditionals_parent):
            self.current_action.add_to_body(command_block)
        else: 
            if command_block.action_type == "add":
                self.set_current_action(command_block)
            elif command_block.action_type == "modify":
                if self.variable_dict.get(command_block.value) != None:
                    self.current_action.handle_command(command_block)
                else:
                    self.current_action.handle_command(command_block)
            elif command_block.action_type == "remove":
                self.previous.tracker.remove(self)
                # self.previous.current_action = self.current_action

    """ 
        This function can be used to add classes such as the calls class or
    variable class or if else or loop etc.
        @param name when used in this function, it should only be the name of one of 
            the classes stated above
        @param value in this case would be the name that you wish to give to the
            class 
    """ 
    def set_current_action(self, command_block):
        if command_block.name == "call":
            self.current_action = calls.Calls(self)
        elif command_block.name == "variable":
            self.current_action = variable.Variable(self)
            self.variable_dict.update({command_block.value:self.current_action})
        elif command_block.name == "if":
            self.current_action = If(self)
        elif command_block.name == "elif":
            self.current_action = Elif(self)
        elif command_block.name == "else":
            self.current_action = Else(self)
        elif command_block.name == "while":
            self.current_action = While(self)
        elif command_block.name == "for":
            self.current_action = For(self)
        elif command_block.name == "do_while":
            self.current_action = Do_while(self)      
        self.current_action.name = command_block.value
        self.tracker.append(self.current_action)

class If(loops_and_conditionals_parent):
    def __init__(self, master):
        super().__init__()
        self.previous = master

    def generate_output(self,output,indent_level):
        temp_out = ""
        indent = ""
        count_indents = 0
        while(count_indents < indent_level):
            indent += "\t"
            count_indents += 1
        temp_out += "if("
        for token in self.argument_list:
            temp_out += token + " "
        temp_out += "){"
        output.append(indent + temp_out)
        for token in self.tracker:
            token.generate_output(output, indent_level + 1)
        output.append(indent + "}")
        

class Elif(loops_and_conditionals_parent):
    def __init__(self, master):
        super().__init__()
        self.previous = master
    
    def generate_output(self,output,indent_level):
        temp_out = ""
        indent = ""
        count_indents = 0
        while(count_indents < indent_level):
            indent += "\t"
            count_indents += 1
        temp_out += "else if("
        for token in self.argument_list:
            temp_out += token + " "
        temp_out += "){"
        output.append(indent + temp_out)
        for token in self.tracker:
            token.generate_output(output, indent_level + 1)
        output.append(indent + "}")
    

class Else(loops_and_conditionals_parent):
    def __init__(self, master):
        super().__init__()
        self.previous = master

    def generate_output(self, output, indent_level):
        temp_out = ""
        indent = ""
        count_indents = 0
        while(count_indents < indent_level):
            indent += "\t"
            count_indents += 1
        temp_out += "else{"
        output.append(indent + temp_out)
        for token in self.tracker:
            token.generate_output(output, indent_level + 1)
        output.append(indent + "}")

class While(loops_and_conditionals_parent):
    def __init__(self, master):
        super().__init__()
        self.previous = master
    
    def generate_output(self,output,indent_level):
        temp_out = ""
        indent = ""
        count_indents = 0
        while(count_indents < indent_level):
            indent += "\t"
            count_indents += 1
        temp_out += "while("
        for token in self.argument_list:
            temp_out += token + " "
        temp_out += "){"
        output.append(indent + temp_out)
        for token in self.tracker:
            token.generate_output(output, indent_level + 1)
        output.append(indent + "}")

class For(loops_and_conditionals_parent):
    def __init__(self, master):
        super().__init__()
        self.previous = master

    def generate_output(self,output,indent_level):
        temp_out = ""
        indent = ""
        count_indents = 0
        while(count_indents < indent_level):
            indent += "\t"
            count_indents += 1
        temp_out += "for("
        for token in self.argument_list:
            temp_out += token + " "
        temp_out += "){"
        output.append(indent + temp_out)
        for token in self.tracker:
            token.generate_output(output, indent_level + 1)
        output.append(indent + "}")

class Do_while(loops_and_conditionals_parent):
    def __init__(self, master):
        super().__init__()
        self.previous = master

    def generate_output(self,output,indent_level):
        temp_out = ""
        indent = ""
        count_indents = 0
        while(count_indents < indent_level):
            indent += "\t"
            count_indents += 1
        temp_out += "do{"
        output.append(indent + temp_out)
        for token in self.tracker:
            token.generate_output(output, indent_level + 1)
        temp_out = ""
        for token in self.argument_list:
            temp_out += token + " "
        output.append(indent + "}while(" + temp_out + ");")
    
    

    



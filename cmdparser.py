import unittest
import re

from abc import ABCMeta, abstractmethod

class AbstractCommand:
    __metaclass__ = ABCMeta
    
    def __init__(self):
        self.name = None
    
    @abstractmethod
    def execute(self):
        pass

class AddStreetCommand(AbstractCommand):

    def __init__(self):
       self.name = 'add street' 

    def execute(self):
        return (True, 'OK', self.name)        

class UpdateStreetCommand(AbstractCommand):

    def __init__(self):
        self.name = 'update street'
    
    def execute(self):
        return (True, 'OK', self.name)

class RemoveStreetCommand(AbstractCommand):
    
    def __init__(self):
        self.name = 'remove street'

    def execute(self):
        return (True, 'OK', self.name)

class GenerateCommand(AbstractCommand):

    def __init__(self):
        self.name = 'generate graph' 

    def execute(self):
        return (True, 'OK', self.name)

class CmdParser:
    def __init__(self):
        self.re_add_update = re.compile("^(a|c) \"([A-Za-z ]+)\" ((?:[ \t]*\([ \t]*-?[1-9][0-9]*[ \t]*,[ \t]*-?[ \t]*[1-9][0-9]*[ \t]*\))+)$", re.IGNORECASE)
	self.re_remove = re.compile("^(r) \"([A-Za-z ]+)\"$", re.IGNORECASE)
        self.re_generate = re.compile("^(g)$", re.IGNORECASE)
    
    def parse_add_update(self, match):
        if match.group(1) == 'a':
            return AddStreetCommand()
        elif match.group(1) == 'c':
            return UpdateStreetCommand()
        else:
           raise Exception("Unexpected parse error. Command should be 'a' or 'c'")
    
    def parse_remove(self, match):
        return RemoveStreetCommand()

    def parse_generate(self, match):
        return GenerateCommand()

    def parse(self, cmd_str):
        m = filter(lambda m: m != None, 
                [regex.match(cmd_str) for regex in [self.re_add_update, self.re_remove, self.re_generate]])
        if m:
            m = m[0]
            command = {
                'a': lambda m: self.parse_add_update(m),
                'c': lambda m: self.parse_add_update(m),
                'r': lambda m: self.parse_remove(m),
                'g': lambda m: self.parse_generate(m)
            }[m.group(1)](m)
            return command;
        else:
            return (False, "Error: Incorrect command format", None)


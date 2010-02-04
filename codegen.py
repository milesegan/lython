#!/usr/bin/env python
# $Id: codegen.py 60 2002-12-19 06:35:28Z miles $

import compiler
import dis
import operator
from parser import ParserError

class MyCodeGenerator(compiler.pycodegen.ModuleCodeGenerator):
    def visitDiscard(self, node):
        self.visit(node.expr)
        self.emit('RETURN_VALUE') # instead of printing :-)

def get_code(string):
    """ determine whether string is an expression or a statement """
    try: tree = compiler.pycodegen.parse(string,'exec')
    except ParserError,e:
        print "no valid statement:",string
        raise
    print tree
    tree.filename='<string>'
    return MyCodeGenerator(tree).getCode()

def othercode(string):
    tree = compiler.pycodegen.Module(string, "<string>")
    print tree._get_tree()
    tree.compile()
    return tree.code

def lispplus(*args):
    return reduce(lambda x,y: x + y, args)

def run_code(string, mathstuff={'lispplus': lispplus}):
   codeobj = othercode(string)
   return eval(codeobj,mathstuff)

code = \
'''
print 1 or 2
'''
run_code(code)

import sys
import os
def RunReady(Path):
    source = open(Path, 'rb')
    program = source.read().decode()
    output = open('primsoutput.py', 'wb')

    program = program.replace('False', 'False')
    program = program.replace('$use', 'import')
    program = program.replace('++', '+=')
    program = program.replace('--', '-=')
    program = program.replace('True', 'True')
    program = program.replace('return', 'return')
    program = program.replace('runfor', 'in range')
    program = program.replace('if', 'if')
    program = program.replace('+', '+')
    program = program.replace('func', 'def ')
    program = program.replace('else', 'else')
    program = program.replace('||', 'or ')
    program = program.replace('*', '*')
    program = program.replace('$=', '=')
    program = program.replace('e=', '==')
    program = program.replace('|=', '!=')
    program = program.replace('else if', 'elif')
    program = program.replace('$biuse ', 'import ')
    program = program.replace('&&', 'and')
    program = program.replace('term.log', 'print')
    program = program.replace('userAsk', 'input')
    program = program.replace('<<', '<')
    program = program.replace('>>', '>')
    program = program.replace('<=', '<=')
    program = program.replace('>=', '>=')
    program = program.replace('/', '/')
    program = program.replace('//', '#')
    output.write(program.encode('utf-8'))
    output.close()
    source.close()

print("Compiling")
current_file = 'Prismscript.psc'
RunReady(current_file)
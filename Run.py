from SymbolTable import SymbolTable
from Lexer import Lexer
from Interpreter import Interpreter
from Context import Context
from Parser import Parser

def run(fn, text):
    # Generate tokens
    lexer = Lexer(fn, text)
    tokens, error = lexer.make_tokens()
    if error: return None, error
    
    # Generate AST
    parser = Parser(tokens)
    ast = parser.parse()
    if ast.error: return None, ast.error

    # Run program
    interpreter = Interpreter()
    context = Context('<program>')
    context.symbol_table = SymbolTable()
    result = interpreter.visit(ast.node, context)

    return result.value, result.error
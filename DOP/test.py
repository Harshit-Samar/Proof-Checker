from sly import Lexer
from sly import Parser
class BoolLexer(Lexer):
    tokens = { ID, LPAREN, RPAREN, AND, OR }
    ignore = ' \t\n'

    ID      = r'[a-zA-Z_\.][a-zA-Z0-9_\.]*'
    LPAREN  = r'\('
    RPAREN  = r'\)'

    ID['AND'] = AND
    ID['OR'] = OR

class BoolParser(Parser):
    tokens = BoolLexer.tokens

    @_('expr AND term')
    def expr(self, p):
        return ('AND', p.expr, p.term)

    @_('expr OR term')
    def expr(self, p):
        return ('OR', p.expr, p.term)

    @_('term')
    def expr(self, p):
        return p.term

    @_('ID')
    def term(self, p):
        return p.ID

    @_('LPAREN expr RPAREN')
    def term(self, p):
        return p.expr

class BasicExecute:

    def __init__(self, tree, env):
        self.env = env
        result = self.walkTree(tree)
        if result is not None and isinstance(result, int):
            print(result)
        if isinstance(result, str) and result[0] == '"':
            print(result)

    def walkTree(self, node):

        

       

        

        
        

        if node[0] == 'OR':
        
            return self.walkTree(node[1]) 
        elif node[0] == 'AND':
            return self.walkTree(node[1]) 
      

        


if __name__ == '__main__':
    lexer = BoolLexer()
    parser = BoolParser()
    env = {}
    while True:
        try:
            text = input('basic > ')
        except EOFError:
            break
        if text:
            tree = parser.parse(lexer.tokenize(text))
            BasicExecute(tree, env)
from sly import Parser
from lexer import CalcLexer
import pickle, sys

class CalcParser(Parser):

    cnt = 1
    
    tokens = CalcLexer.tokens
    g_scp = 0
    t_scp = 0

@_('stmt_list stmt')
def stmt_list(self,p):
        return p

@_('stmt')
def stmt_list(self, p):
		return p

@_('SCOPE stmt')
def stmt(self,p):
        t_scp += 1
    
# @_('expr SQUARE_OPEN reason SQUARE_CLOSE')
# def stmt(self,p):


@_('EOL')
def eol(self,p):
		self.cnt += 1
		return p
	
@_('COMMENT')
def expr(self,p):
    	return p

    #########################
@_('expr SQUARE_OPEN reason SQUARE_CLOSE')
def stmt(self,p):
        # for c in p.expr:
        #     if c!='-':
        #         break
        #     stmt_scope += 1
        if abs(stmt_scope-g_scp)>1:
            print("\nMore than 1 scope changed in a single statement")
            raise Exception("Scope Error")
        t_scp = 0
        evltd = p.expr[stmt_scope:]

if __name__ == '__main__':
    lexer = CalcLexer()
    parser = CalcParser()
    while True:
        try:
            text = input('calc > ')
        except EOFError:
            break
        if text:
            parser.parse(lexer.tokenize(text))

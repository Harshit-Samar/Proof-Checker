from sly import Lexer

class CalcLexer(Lexer):
    # Set of token names.   This is always required
    tokens = {EOS, COMMA, NUM, VAR, COMMENT, EOL, ROUND_OPEN, ROUND_CLOSE, CURLY_OPEN, CURLY_CLOSE, SQUARE_OPEN, SQUARE_CLOSE, NOT, OR, AND, THEN, IFF, SCOPE, RULE,ID,BY,USING,CANCEL,ASSN,HYPO}

    # String containing ignored characters between tokens
    ignore = ' \t'

    # Regular expression rules for tokens
    EOS = r';'
    COMMA = r','
    NUM = r'[0-9]+'
    VAR = r'[a-zA-Z][a-zA-Z0-9_]*'
    COMMENT = r'//.*'
    EOL = r'\n'
    ROUND_OPEN = r'\('
    ROUND_CLOSE = r'\)'
    CURLY_OPEN = r'\{'
    CURLY_CLOSE = r'\}'
    SQUARE_OPEN = r'\['
    SQUARE_CLOSE = r'\]'
    NOT = r'(\~|\!)'
    OR = r'\|'
    AND = r'\&'
    THEN = r'\>'
    IFF = r'\<\>'
    SCOPE = r'-'
    RULE = r'(~E|~I|&E|&I|\|E|\|I|>E|>I|<>E|<>I)'
     # Base ID rule
    
    ID = r'[a-zA-Z_][a-zA-Z0-9_]*'

    # Special cases
    ID['by'] = BY
    ID['using'] = USING
    ID['cancel'] = CANCEL
    ID['Assumption'] = ASSN
    ID['Hypothesis'] = HYPO

    

if __name__ == '__main__':
    data = '~(p>q) by  [reason]'
    lexer = CalcLexer()
    for tok in lexer.tokenize(data):
        print('type=%r, value=%r' % (tok.type, tok.value))
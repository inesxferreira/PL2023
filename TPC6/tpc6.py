import ply.lex as lex

# Definir as expressões regulares, palavras e simbolos da linguagem
tokens = (
    'INT', 'ID', 'LPAREN', 'RPAREN', 'LBRACKET', 'RBRACKET', 'EQUALS',
    'COMMA', 'COLON', 'DOT', 'SEMI', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'MOD', 'LT', 'LE', 'GT', 'GE', 'EQ', 'NE', 'AND', 'OR', 'NOT',
    'IF', 'ELSE', 'WHILE', 'FOR', 'FUNCTION', 'PROGRAM', 'PRINT',
    'LBRACE', 'RBRACE', 'INTLIT', 'RANGELIT', 'COMMENT', 'IF'
)

# Expressões regulares para tokens simples
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_COMMA = r','
t_COLON = r':'
t_DOT = r'\.'
t_SEMI = r';'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_MOD = r'%'
t_LT = r'<'
t_LE = r'<='
t_GT = r'>'
t_GE = r'>='
t_EQ = r'=='
t_NE = r'!='
t_AND = r'&&'
t_OR = r'\|\|'
t_NOT = r'!'
t_IF = r'if'


# Expressões regulares para palavras-chave
reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'for': 'FOR',
    'function': 'FUNCTION',
    'program': 'PROGRAM',
    'print': 'PRINT'
}

# Expressões regulares para tokens compostos


def t_INTLIT(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_RANGELIT(t):
    r'\[[\d]+\.\.[\d]+\]'
    t.value = t.value[1:-1].split('..')
    t.value = [int(i) for i in t.value]
    return t


def t_COMMENT(t):
    r'(/\*(.|\n)*?\*/)|(//.*)'
    pass

# Expressão regular para ID (identificadores)


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')
    return t


# Expressão regular para espaços em branco
t_ignore = ' \t\r'

# Expressão regular para quebra de linha


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Lidar com erros de caracteres inválidos


def t_error(t):
    print(f"Caractere inválido: {t.value[0]}")
    t.lexer.skip(1)


data = '''
/* factorial.p
-- 2023-03-20 
-- by jcr
*/
/**/
/*
*/
int i;
// Função que calcula o factorial dum número n
function fact(n){
  int res = 1;
  while res > 1 {
    res = res * n;
    res = res - 1;
  }
}
// Programa principal
program myFact{
  for i in [1..10]{
    print(i, fact(i));
  }
}
/* max.p: calcula o maior inteiro duma lista desordenada
-- 2023-03-20 
-- by jcr
*/
int i = 10, a[10] = {1,2,3,4,5,6,7,8,9,10};
// Programa principal
program myMax{
  int max = a[0];
  for i in [1..9]{
    if max < a[i] {
      max = a[i];
    }
  }
  print(max);
}'''


lexer = lex.lex()  # cria uma instância do analisador léxico
lexer.input(data)
while tok := lexer.token():
    print(tok)

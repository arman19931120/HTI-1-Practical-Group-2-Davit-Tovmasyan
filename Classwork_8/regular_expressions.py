import re


identifiers = [
    'A',
    'naAme',
    '_name',
    '__name__',
    'name2',
    '2naAme',
    'աբց',
    'name____',
    'name___ա',
    'AAname&',
    '    ',
]


expression = '[_a-zA-Z][_a-zA-Z0-9]*'
# expression_lower = '[_a-z][_a-z0-9]*'

# re.search(expression, '')
# re.match(expression, '')
# for identifier in identifiers:
#     if re.fullmatch(expression, identifier):
#         print(identifier, ' -> this is valid identifier')
#     else:
#         print(identifier, ' -> this is invalid identifier!!!')


message = 'Բարև ձեզ, սա(01 XC 001) իմ համարն է 111PP99  17AA896, խնդրում եմ ստուգել։'

print(re.findall('((?:(?:[0][1-9])|(?:[1-9][0-9]))(?:[ ]{0,1}[A-Z]{2}[ ]{0,1}(?:(?:[0][1-9]{2})|(?:[1-9][0-9]{2}))))', message))

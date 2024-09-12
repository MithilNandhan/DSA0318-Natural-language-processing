import re
class FOPCParser:
    def __init__(self):
        self.operators = {'AND': '&&', 'OR': '||', 'NOT': '!'}
    def parse(self, expression):
        expression = re.sub(r'\s+', '', expression)
        tokens = self.tokenize(expression)
        return self.parse_expression(tokens)
    def tokenize(self, expression):
        token_patterns = {
            'variable': r'[a-zA-Z_][a-zA-Z0-9_]*',
            'predicate': r'[A-Z][a-zA-Z0-9_]*',
            'operator': r'(AND|OR|NOT)',
            'parenthesis': r'[\(\)]'
        }
        token_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_patterns.items())
        token_re = re.compile(token_regex)
        tokens = []
        for match in token_re.finditer(expression):
            for name, value in match.groupdict().items():
                if value:
                    tokens.append((name, value))
                    break
        return tokens
    def parse_expression(self, tokens):
        if not tokens:
            return None
        def parse_primary(tokens):
            if not tokens:
                return None
            token_type, token_value = tokens.pop(0)
            if token_type == 'variable':
                return f"Variable({token_value})"
            elif token_type == 'predicate':
                return f"Predicate({token_value})"
            elif token_type == 'parenthesis':
                if token_value == '(':
                    expr = self.parse_expression(tokens)
                    if tokens and tokens[0][1] == ')':
                        tokens.pop(0)  # Remove the ')'
                        return expr
                    else:
                        raise ValueError("Mismatched parentheses")
                elif token_value == ')':
                    raise ValueError("Unexpected closing parenthesis")
        def parse_operator(tokens):
            if tokens and tokens[0][0] == 'operator':
                return tokens.pop(0)[1]
            return None
        def parse_logic(tokens):
            expr = parse_primary(tokens)
            while tokens:
                operator = parse_operator(tokens)
                if not operator:
                    break
                right_expr = parse_primary(tokens)
                expr = f"({expr} {self.operators[operator]} {right_expr})"
            return expr
        return parse_logic(tokens)
parser = FOPCParser()
expression = "(A AND B) OR (NOT C)"
parsed_expression = parser.parse(expression)
print("Parsed Expression:", parsed_expression)

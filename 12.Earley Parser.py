class State:
    """Represents an Earley state"""
    def __init__(self, rule, dot, start, end):
        self.rule = rule 
        self.dot = dot  
        self.start = start 
        self.end = end  
    def __repr__(self):
        """String representation of the state"""
        return f"{self.rule[0]} -> {' '.join(self.rule[1][:self.dot])} . {' '.join(self.rule[1][self.dot:])} [{self.start}, {self.end}]"
    def is_complete(self):
        """Check if this state is complete (i.e., the dot has reached the end of the rule)"""
        return self.dot >= len(self.rule[1])

class EarleyParser:
    def __init__(self, grammar, input_string):
        self.grammar = grammar  # The context-free grammar
        self.input = input_string.split()  # Input sentence
        self.chart = [[] for _ in range(len(self.input) + 1)]  # Chart (one entry per input position)
        
    def parse(self):
        """Main parsing function"""
        start_rule = ('GAMMA', [self.grammar['start']])
        self.chart[0].append(State(start_rule, 0, 0, 0))

        for i in range(len(self.input) + 1):
            self.process_chart(i)

        for state in self.chart[-1]:
            if state.rule[0] == 'GAMMA' and state.is_complete() and state.start == 0:
                return True
        return False

    def process_chart(self, i):
        """Process the chart at position i"""
        states = self.chart[i]
        for state in states:
            if not state.is_complete():
                next_symbol = state.rule[1][state.dot]
                if next_symbol in self.grammar['non-terminals']:
                    self.predictor(state, i)
                else:
                    self.scanner(state, i)
            else:
                self.completer(state, i)

    def predictor(self, state, i):
        """Predictor step: add rules for non-terminal expansions"""
        next_symbol = state.rule[1][state.dot]
        for rule in self.grammar['rules'][next_symbol]:
            new_state = State((next_symbol, rule), 0, i, i)
            if new_state not in self.chart[i]:
                self.chart[i].append(new_state)

    def scanner(self, state, i):
        """Scanner step: match terminal symbols with the input"""
        if i < len(self.input):
            next_symbol = state.rule[1][state.dot]
            if next_symbol == self.input[i]:
                new_state = State(state.rule, state.dot + 1, state.start, i + 1)
                self.chart[i + 1].append(new_state)

    def completer(self, state, i):
        """Completer step: complete a rule and move the dot in parent states"""
        for prev_state in self.chart[state.start]:
            if not prev_state.is_complete() and prev_state.rule[1][prev_state.dot] == state.rule[0]:
                new_state = State(prev_state.rule, prev_state.dot + 1, prev_state.start, i)
                if new_state not in self.chart[i]:
                    self.chart[i].append(new_state)
if __name__ == "__main__":
    grammar = {
        'start': 'S',
        'non-terminals': ['S', 'NP', 'VP', 'V', 'Det', 'N'],
        'rules': {
            'S': [['NP', 'VP']],
            'NP': [['Det', 'N']],
            'VP': [['V', 'NP']],
            'V': [['saw']],
            'Det': [['the']],
            'N': [['dog'], ['cat']]
        }
    }
    input_string = "the dog saw the cat"
    parser = EarleyParser(grammar, input_string)
    if parser.parse():
        print("The input string is valid according to the grammar.")
    else:
        print("The input string is not valid according to the grammar.")

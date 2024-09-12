# Define the grammar
grammar = {
    'S': [['NP', 'VP']],
    'NP': [['Det', 'N']],
    'VP': [['V', 'NP'], ['V']],
    'Det': [['the']],
    'N': [['cat'], ['dog']],
    'V': [['chases'], ['sees']]
}
def parse(symbol, tokens):
    if not tokens:
        return False, tokens
    if symbol not in grammar:
        if tokens and tokens[0] == symbol:
            return True, tokens[1:] 
        else:
            return False, tokens

    for production in grammar[symbol]:
        remaining_tokens = tokens
        match = True
        for part in production:
            success, remaining_tokens = parse(part, remaining_tokens)
            if not success:
                match = False
                break
        
        if match:
            return True, remaining_tokens
    
    return False, tokens
sentence = "the cat chases the dog".split()
success, remaining_tokens = parse('S', sentence)
if success and not remaining_tokens:
    print("The sentence is valid")
else:
    print("The sentence is invalid")

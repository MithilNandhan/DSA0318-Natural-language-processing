def pluralize(noun):
    state = "START"
    for i in range(len(noun)):
        char = noun[i]
        
        if state == "START":
            if char in "sxz" or noun.endswith("sh") or noun.endswith("ch"):
                state = "ADD_ES"
            elif noun.endswith("y") and noun[-2] not in "aeiou":
                state = "Y_TO_IES"
            else:
                state = "ADD_S"
    if state == "ADD_ES":
        return noun + "es"
    elif state == "Y_TO_IES":
        return noun[:-1] + "ies"
    elif state == "ADD_S":
        return noun + "s"
    else:
        return noun
nouns = ["cat", "dog", "bus", "fox", "buzz", "baby", "church", "dish"]
for noun in nouns:
    plural = pluralize(noun)
    print(f"Singular: {noun}, Plural: {plural}")

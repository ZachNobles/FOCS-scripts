##########################################
# change code in this box

# add variables to the grammar
# use "" for λ
grammar = {
    "S": ["aS", "bS", "aA"],
    "A": ["aB"],
    "B": ["aC"],
    "C": ["a"]
}

# usually grammars allow for an infinite number of strings, 
# so specify a max length for the strings
max_length = 8

# whether to print the list of strings
print_strings = True

##########################################



def generate_strings(start_symbol, max_length):
    strings = set()
    queue = [start_symbol]

    while queue:
        current_string = queue.pop(0)

        # If the current string is terminal (contains no variables)
        if all(char not in grammar for char in current_string):
            if len(current_string) <= max_length:
                strings.add(current_string)
            continue

        # If the string contains variables, replace them with all of their productions
        for i, char in enumerate(current_string):
            if char in grammar:
                for production in grammar[char]:
                    new_string = current_string[:i] + production + current_string[i + 1:]
                    if len(new_string) <= max_length + max([len(x) for x in grammar[char]]):
                        queue.append(new_string)

    return strings



strings = generate_strings("S", max_length)

# Print the resulting strings
print(f"Generated {len(strings)} strings")
if print_strings:
    print(",\n".join([", ".join(sorted(strings, key=len)[i:i + 10]) for i in range(0, len(strings), 10)]))
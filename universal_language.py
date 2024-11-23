##########################################
# change code in this box

# Language
# Example: let L = {"ab", "aa", "baa"}
L = {"0", "1"}

# Strings you want to check the possibility of
# Example: w = ["abaabaaabaa", "aaaabaaaa"]
w = []

# Max length of string in universal language
# Technically, the UL is infinite, so you have to cap the length somewhere
# to set it to the minimum length you need, use: max([len(string) for string in w])
max_length = 10

#whether to print the whole universal language
print_UL = True
##########################################



def UL_helper(L, U, max_length):
    new_elements = []
    for substring in U: # for every current string that has been created
        for symbol in L: # add every symbol from the language
            new_string = substring + symbol
            if len(new_string) <= max_length and new_string not in U:
                new_elements.append(new_string)
    
    # If new_elements is not empty, extend U and recur
    if new_elements:
        U.extend(new_elements)
        return UL_helper(L, U, max_length)

    return U

def universal_language(L, max_length):
    return UL_helper(L, [""], max_length)




UL = universal_language(L, max_length)


if print_UL:
    print("Universal language:")
    print(UL)

print("\n\nTest cases:")

for string in w:
    print(string + ": ", end = "")
    if len(string) > max_length:
        print("max length is too short.")
    elif string in UL:
        print("string can be made.")
    else:
        print("string can NOT be made")
        
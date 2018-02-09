#!/usr/bin/env python3.6

def import_text():
    with open('substitution.txt', 'r') as docstring:
        docstringlist = []
        while True:
            char = docstring.read(1)
            if not char:
                break

            else:
                docstringlist.append(char)


        if not docstring.closed:
            docstring.close()

    return docstringlist


def remove_space(text):
    fixed_string = []
    for char in text:
        if char == ' ':
            pass
        else:
            fixed_string.append(char)

    return fixed_string



# code to do frequency analisys
def codebreaker(text):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for letter in alphabet:
        score = 0
        for char in text:
            if letter == char:
                score += 1
            else:
                pass
           

        result = (score / len(text)) * 100
        print(letter, ':', round(result,5), '% ', letter, '=')


if __name__ == '__main__':

    text = import_text()
    textstring = remove_space(text) 
    codebreaker(textstring)


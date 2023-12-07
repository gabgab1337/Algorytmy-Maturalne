import os.path
import re

'''
KONWERTER WZOROWANY NA KONWERTERZE AUTOSTWA @BlueNexus
DOSTOSOWANY DO WYMAGAŃ CKE
https://gist.github.com/BlueNexus/599962d03a1b52a8d5f595dabd51dc34
'''

python_file = 'Algorytmy/NWD&NWW.py'

basic_conversion_rules = {"=": "←", 
                          "if": "jeżeli", 
                          "==": "=",
                          "%": "mod",
                          "//": "div", 
                          "!=": "≠",
                          "while": "dopóki", 
                          "for": "dla",
                          "def": "funkcja", 
                          "else:": "w przewciwnym wypadku",
                          "elif": "w przewciwnym wypadku jeżeli", 
                          "and:": "i", 
                          "or:": "lub", 
                          "pass": "opuść", 
                          "in": "W"}

prefix_conversion_rules = {"#F": "CALL "}
advanced_conversion_rules = {"print": "wypisz", "return": "zwróć", "input": "wprowadź"}


def l2pseudo(to_pseudo):
    for line in to_pseudo:
        line_index = to_pseudo.index(line)
        line = str(line)
        line = re.split(r'(\s+)', line)
        for key, value in prefix_conversion_rules.items():
            if key in line:
                if not str(line[0]) == '':
                    line[0] = value + line[0]
                else:
                    line[2] = value + line[2]
        for key, value in basic_conversion_rules.items():
            for word in line:
                if key == str(word):
                    line[line.index(word)] = value
        for key, value in advanced_conversion_rules.items():
            for word in line:
                line[line.index(word)] = word.replace(key, value)
        for key, value in prefix_conversion_rules.items():
            for word in line:
                if word == key:
                    del line[line.index(word)]
        to_pseudo[line_index] = "".join(line)
    return to_pseudo


def p2file(to_file):
    py_file = os.path.splitext(os.path.basename(python_file))[0]
    with open('converter.txt', 'w') as writer:
        writer.write("\n".join(to_file))


def main():
    with open(python_file, 'r+') as py_file_reader:
        file_lines = py_file_reader.readlines()
        work_file = l2pseudo(file_lines)
        p2file(work_file)


if __name__ == '__main__':
    main()
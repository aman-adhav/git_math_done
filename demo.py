import speech_recognition as sr
from typing import List
import itertools
import operator
# obtain path to "english.wav" in the same folder as this script

#from os import path
#AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "yes.wav")

# AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "french.aiff")
# AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "chinese.flac")

# use the audio file as the audio source

'''
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)  # read the entire audio file
'''

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

# recognize speech using Microsoft Bing Voice Recognition
BING_KEY = "244de28d34e24ab586fdfda8920fe8e7"  # Microsoft Bing Voice Recognition API keys 32-character lowercase hexadecimal strings
print('Processing Data: ')
FUNCTIONS = ['limit', 'graph','function','delta','over','epsilon','minus','plus','equal','square','squared','cubed','absolute','less','zero','one','two','three','four','five','six','seven','eight','nine','ten']

def initialize(BING_KEY)-> List[str]:
    line_arr = []
    line = r.recognize_bing(audio, key=BING_KEY)
    lines = line.split()

    for space in lines:
        line_arr.append(str(space))

    return line_arr


from typing import List
import itertools
import operator

FUNCTIONS = ['limit', 'graph', 'function', 'delta', 'over', 'epsilon', 'minus', 'plus', 'equal', 'square', 'squared',
             'cubed', 'absolute', 'less', 'zero', 'one', 'two', 'three', 'graph']


def check_function(nindex: int) -> bool:
    function = ""
    array[nindex + 2] = '='
    if array[nindex].isupper():
        if array[nindex - 1] == 'of':
            if array[nindex - 2] == 'prime':
                function = array[nindex - 4].lower() + "'(" + array[nindex] + ")" + array[nindex + 2] + array[
                    nindex + 4]
                array[nindex + 2] = "$" + function + "$"
            else:
                function = array[nindex - 2].lower() + "(" + array[nindex] + ")" + array[nindex + 4]
                array[nindex + 2] = "$" + function + "$"
        else:
            function = array[nindex].lower() + array[nindex + 2] + array[nindex + 4]
            array[nindex + 2] = "$" + function + "$"
            array[nindex] = array[nindex + 1] = array[nindex + 3] = array[nindex + 4] = ""
    else:
        function = array[nindex] + array[nindex + 2] + array[nindex + 4]
        array[nindex + 2] = "$" + function + "$"
        array[nindex + 1] = array[nindex] = array[nindex + 3] = array[nindex + 4] = ""
        # print(array)


def equals(index: int) -> None:
    if array[index + 1] == 'to' and array[index - 1] == 'is':
        check_function(index - 2)
    elif array[index] == 'equals':
        array[index] = '='


def limit(index: int):
    temp = ""
    if (array[index + 4]).lower() == 'infinity':
        array[index + 4] = 'infty'
    else:
        array[index + 4]
    if (array[index + 1] == 'of'):
        temp = "$\lim_{" + array[index + 2].lower() + '\\' + "to" + '\\\n' + array[index + 4] + '}'
        array[index] = temp
        for i in range(1, 5):
            array[index + i] = ""
    else:
        temp = "$\lim$"
    print(temp)


def find_key():
    for i in range(len(array)):
        if array[i] in FUNCTIONS:
            if array[i] == "squared" or array[i] == "square":
                array[i] = "^2"
            if array[i] == "cubed":
                array[i] = "^3"
            if array[i] == 'over':
                array[i] = "/"
            if array[i] == 'plus':
                array[i] = "+"
            if array[i] == 'minus':
                array[i] = "-"


def most_common():
    # get an iterable of (item, iterable) pairs
    SL = sorted((x, i) for i, x in enumerate(array))
    # print 'SL:', SL
    groups = itertools.groupby(SL, key=operator.itemgetter(0))

    # auxiliary function to get "quality" for an item
    def _auxfun(g):
        item, iterable = g
        count = 0
        min_index = len(array)
        for _, where in iterable:
            count += 1
            min_index = min(min_index, where)
        # print 'item %r, count %r, minind %r' % (item, count, min_index)
        return count, -min_index

    # pick the highest-count/earliest item
    return max(groups, key=_auxfun)[0]


def create_function(value_func: int):
    count = value_func + 5
    if_true = True
    f_of = array[value_func] + "(" + array[value_func + 2] + ")"
    mini_list = []
    mini_list.append(f_of)
    if array[value_func + 4] == 'equal':
        mini_list.append("=")
        while if_true:
            count += 1;
            print(array[count])
            if array[count] == 'there':
                if_true = False
            else:
                mini_list.append(array[count])
    return (mini_list)


def change_str(funci: str, index: int, string: List[str]):
    array[index] = funci
    for i in range(index + 1, len(array)):
        if array[i] != string[len(string) - 1]:
            array[i] = ""
        else:
            array[i] = "$"
            break


def identify():
    for i in range(len(array)):
        if array[i] == 'of':
            if array[i - 1].lower() == 'limit':
                limit(i - 1)
            elif array[i - 1].isupper() and array[i + 1].isupper() and array[i + 1] == variable:
                a = create_function(i - 1)
                funci = "".join(str(x) for x in a)
                change_str(funci, i - 1, a)
                return funci


# ['As', 'the', 'limit', 'of', 'X', 'approaches', 'Infinity', 'F', 'of', 'X', 'is', 'equal', 'to', 'X', 'cubed', 'plus', 'X', 'squared', '+5', 'over', 'X', '-6.']
def clean_data(arr: str):
    space = ''
    is_true = True
    while is_true:
        if space in arr:
            arr.remove(space)
        else:
            is_true = False
    return arr

def graph(variable: str):
    string = '\\documentclass[tikz]{standalone}\n\\usepackage{tikz}\n\\begin{document}\n\\begin{tikzpicture}\n\t\\draw[->] (-3,0) -- (4.2,0) node[right] {$x$};\n\t\\draw[->] (0,-3) -- (0,4.2) node[above] {$y$};\n\t\\draw[scale=0.5,domain=-3:3,smooth,variable=\\x,blue] plot ({\\x},'

    varia = variable
    funct = func
    functi = ''
    if '=' in funct:
      functi = funct[funct.index('=')+1:]
      #print(functi)
      if '^2' in functi:
        functi = functi.replace('^2','*X')
      if '^3' in functi:
        functi = functi.replace('^3','*X*X')
      #print(functi)

    for varia in functi:
      functi = functi.replace('X', '\\x')

    functi = "{"+functi+"});"
    string = string+functi+'\n\t\\end{tikzpicture}\n\\end{document}'
    print(string)

array = initialize(BING_KEY)
print(array)

variable = most_common()
print(variable)

find_key()
func = identify()

print(func)
array = clean_data(array)
line = " ".join(str(x) for x in array)
if 'graph' in array:
    if 'function' in line:
        graph(variable)



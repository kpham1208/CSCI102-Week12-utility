# GITHUB URL
#  Kenny Pham
# CSCI 102 - Section E
#  Week 12 - Part B

def PrintOutput(String_Input):
    print(String_Input)
    
def LoadFile(File_Name):
    with open(File_Name, 'r') as f:
        return [line.strip('\n') for line in f]

def UpdateString(string, character, position):
    string = list(string)
    string[position] = character
    result = ''.join(string)
    print(result)

def FindWordCount(a, string):
        wordcount = 0
        j = 0
        k = j + len(string)
        for line in a:
            if line[j:k] == string:
                wordcount += 1
        return wordcount


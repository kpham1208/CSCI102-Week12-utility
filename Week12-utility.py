# https://github.com/kpham1208/CSCI102-Week12-utility
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

def ScoreFinder(players, scores, player):
    if player in players:
        x = players.index(player)
        for z in scores:
            if x == scores.index(z):
                points = z
        print('OUTPUT ', player, 'got a score of', points)
    else:
        print('OUTPUT player not found')
    
def Union(scores, players2):
    result = ', '.join(str(scores) for x in players2)
    return result

def Intersection(players, players2):
    result = []
    for i in players:
        if players[i] == players2[i]:
            result.append(players[i])
            print('OUTPUT ', result)

def Notin(players, players2):
    result = []
    for i in players:
        if players[i] != players2[i]:
            result.append(players[i])
            print('OUTPUT ', result)

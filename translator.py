import re
import bbylist

vowels = "[aeiou]"
consonances = "[bcdfghjklmnpqrstvwxyz]"


def pagpapantig(word):
    new = ''
    for index, i in enumerate(word):
        if i == ' ':
            new += f'{i}-'
        # LAST LETTER
        if index == len(word) - 1:
            new += f'{i}'
        else:
            # VOWELS// Rule 1
            if re.search(vowels, i):
                new += f'{i}-'
            # CONSONANCE 
            elif re.search(consonances, i):
                # CONSONANCE AND NG+VOWEL // Special Case 
                if i == 'n' or i == 'N':
                    # // Special Case 2
                    if word[index:index + 3] == 'nga':
                        new += f'{i}'
                        continue
                    # // Special Case 1
                    elif word[index:index + 2] == 'ng':
                        new += f'{i}'
                        continue
                # CONSONANCE STANDALONE // Rule 2
                if re.search(consonances, word[index + 1]) or word[index + 1] == ' ':
                    new += f'{i}-'
                # CONSONANCE PRECEDING VOWEL // Rule 3
                elif re.search(vowels, word[index + 1]):
                    new += f'{i}'

    return new


def stringToArray(new):

    final = new.split('-')

    pattern = ''
    #Syllable Determination
    for i in final:
        for j in i:
            if re.search(consonances, j):
                pattern += 'C'
            elif re.search(vowels, j):
                pattern += 'V'
            else:
                pattern +=' '
                
        if i != final[-1]:
            pattern += '-'
        
    print(pattern)
    pfinal = pattern.split('-')

    print("Syllable Determination")

    for index, i in enumerate(pfinal):
        print(f'{final[index].upper()} \t {pfinal[index]}')

    return final

#Baybayin equivalence
def fetchbaybayinchars(final):
    
    baybayinchars = []
    
    for i in final:
        value = bbylist.mapping.get(i)
        baybayinchars.append(value)
    
    return baybayinchars

def isVowel(c):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    return 1 if c in vowels else 0

def wyraz(s1, s2):
    firstAsciiSum = 0
    firstVowelsCount = 0

    for i in range(len(s1)):
        firstAsciiSum += ord(s1[i])
        firstVowelsCount += isVowel(s1[i])
    
    def rek(i, asciiSum, counter):
        if i == len(s2):
            return asciiSum == firstAsciiSum and counter == firstVowelsCount
        return rek(i+1, asciiSum, counter) or rek(i+1, asciiSum+ord(s2[i]), counter+isVowel(s2[i]))

    return rek(0,0,0)

print(wyraz("ula", "exre"))
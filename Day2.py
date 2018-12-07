from collections import Counter

def checksum():
    twice = 0
    thrice = 0

    with open('InputData/Day2Input.txt', 'r') as f:
        for line in f:
            # create a dictionary that stores the letter as 
            # the key and number of times that letter shows up as the value
            letter_dict = {}
            for char in line:
                if (char not in letter_dict):
                    letter_dict[char] = 1
                else:
                    letter_dict[char] = letter_dict[char] + 1

            # iterate through the dictionary
            # to find the value of 2 and 3
            for ch, num in letter_dict.items():
                if num == 2:
                    twice = twice + 1
                    break
            
            for ch, num in letter_dict.items():
                if num == 3:
                    thrice = thrice + 1
                    break

        print "Twice: ", twice
        print "Thrice: ", thrice
        print "Checksum: ", twice*thrice

            
def correctBoxes():
    f = open('InputData/Day2Input.txt')
    lines = f.readlines()
    
    for i in range(0, len(lines)-1):
        for j in range(1, len(lines)):
            u = zip(lines[i].rstrip("\n"), lines[j].rstrip("\n"))

            # count the number of mismatching characters
            count = 0
            for m, k in u:
                if m != k:
                    count = count + 1
            
            # strings have exactly 1 character that is not common
            if count == 1:
                dict1 = Counter(lines[i]) 
                dict2 = Counter(lines[j])

                commonDict = dict1 & dict2
                commonChars = commonDict.elements()
                strChars = ''.join(commonChars)
                print "Similar characters are:", strChars


if __name__ == '__main__':
    import sys
    checksum()
    correctBoxes()
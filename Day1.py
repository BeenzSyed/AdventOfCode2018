
def frequency():
    freq = 0
    with open('Day1Input.txt', 'r') as f:
        for line in f:
            x = int(line)
            freq = freq + x
        print freq

def frequency2():
    freq = 0
    freq_dict = {}
    breakout = True
    while breakout:
        with open('Day1Input.txt', 'r') as f:
            for line in f:
                x = int(line)
                freq = freq + x
                
                if (freq not in freq_dict):
                    freq_dict[freq] = 1
                else:
                    print "Dup is: ", freq
                    breakout = False
    print freq

if __name__ == '__main__':
    import sys
    frequency()
    frequency2()
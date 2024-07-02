# there are at least two easy watys to output to a text file

def printToFile(t):
    '''print some text to a file'''
    # we need a file access object
    fout = open('my_file.txt', 'at') # 'at' will append text
    print(t, file=fout) # send the print output to our file access object

def writeToFile(t):
    '''write some text to a file'''

if __name__ == '__main__':
    words = 'here is some text to be written to a file'
    printToFile(words)
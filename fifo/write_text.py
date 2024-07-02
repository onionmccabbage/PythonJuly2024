# there are at least two easy ways to output to a text file

def printToFile(t):
    '''print some text to a file'''
    # we need a file access object
    fout = open('my_file.txt', 'at') # 'at' will append text
    # NB every time we use print, it will add a new line character
    print(t, file=fout) # send the print output to our file access object
    # it is a good idea to tidy up
    fout.close()

def writeToFile(t):
    '''write some text to a file'''
    fout = open('my_file.txt', 'at')
    # when we use write, there is no additional new-line character
    fout.write(t)
    fout.close()

def elegantOutput(t):
    '''often we use with to output to files'''
    # whenever we deal with external assets we should consider exception handling
    try:
        # 'wt' will (over)write text
        # 'xt' is for exclusive access (fails if the file already exists)
        with open('my_file.txt', 'xt') as fout:
            fout.write(t)
        # when the with block ends it will automatically close the file
    except FileExistsError as fe:
        print(f'The file already exists {fe}')

if __name__ == '__main__':
    words = 'here is some text to be written with a file'
    # printToFile(words)
    # writeToFile(words)
    elegantOutput(words)
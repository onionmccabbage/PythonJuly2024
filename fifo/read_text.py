def readText():
    '''read text back from a file'''
    fin = open('my_file.txt', 'rt') # 'rt' will read text
    r = fin.read() # retrieve all the content
    fin.close() # pr use 'with' as before
    return r


if __name__ == '__main__':
    retrieved = readText()
    print(retrieved)
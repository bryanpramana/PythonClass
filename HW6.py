def main():

    sourceFileName = input('Enter source file name (include the extension): ')
    sourceFile = open(sourceFileName, 'r')
    filedata = sourceFile.read()

    lines=1           #we start with one because the first line has to be counted without using iteration function
    words=1           #we start with one because the first word has to be counted.
    characters=0
    nonwhitespace=0
    y=' '

    for x in (filedata):
        if(x=='\n' ):
            lines+=1
#i am using variable y to check whether there is doouble spaces or not, to avoid double counting of word
        if(x==' ' or x=='\n' or x=='\t'):
            if(y==' '):
                words+=0
            else:
                words+=1
        y=x
        if(x==',' or x=='.'):
            characters+=0
        else:
            characters+=1
        nonwhitespace+=1
        if(x==' ' or x==',' or x=='.'):
            nonwhitespace-=1
    print('The number of lines in the file is                           : ',lines)
    print('The number of words in the file is                           : ',words)
    print('The total number of characters in the file is                : ',characters)
    print('the total number of non-whitespace characters in the file is : ',nonwhitespace)
    sourceFile.close()

main()

#!/usr/bin/env python

'''
Transform *.txt data file obtained from Beijing Synchrotron Radiation soft 
X-ray station to support Athena software
'''  

__author__ = "LI Kezhi" 
__date__ = "$2016-11-15$"
__version__ = "1.0"

import os
import time

def main():
    while(True):
        file = raw_input('Enter a file name, \'q\' for exit:')
        if file == 'q' or file == 'Q':
            break
        if '.txt' not in file:
            file += '.txt'
        path = os.getcwd()
        completePath = path + file
        ISOTIMEFORMAT = '%Y-%m-%d %H:%M'
        fileTime = os.path.getctime(file)
        fileTime = time.localtime(fileTime)
        fileTime = time.strftime(ISOTIMEFORMAT, fileTime)
        with open(file, 'r') as f:
            lineNum = 0
            content = []
            for line in f:
                content.append(line.split()[0:6])
                lineNum += 1
        output = open(file.split('.')[0], 'w')
        output.writelines('#' + completePath + '\n')
        output.writelines(fileTime + '\n')
        output.writelines('#comment :\n')
        output.writelines('#0\n')
        output.writelines(str(lineNum)+'#\n')
        for line in content:
            text = str(line[0]) + ' ' 
            text += str(line[1]) + ' ' 
            text += str(line[2]) + ' ' 
            text += str(line[3]) + ' ' 
            text += str(line[4]) + ' ' 
            text += str(line[5]) + '\n'
            output.writelines(text)
        print('Converted successfully.\n')

if __name__ == '__main__':
    main()
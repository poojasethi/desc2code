'''
Created on Oct 17, 2012

@author: anuvrat
'''
import sys

def is_palin( num ):
    return num == num[::-1]

def main():
    for _ in xrange( int( sys.stdin.readline() ) ):
        for n in xrange( int( sys.stdin.readline() ) + 1, 100000 ):
            if is_palin( str( n ) ):
                print n
                break

main()

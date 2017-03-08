import sys
import re

def valUser(user):
    # print("vaidate",user)
    if(len(user)>16 or len(user)<1):
        return 0
    user = re.sub(r'[a-zA-Z\d_]', '',user)
    if(len(user)>0):
        return 0
    return 1

# sys.stdin = open("B.in", "r")


def solve():
    test = raw_input().split("/")
    if(len(test)>2):
        print("NO")
        return
        
    first = test[0].split("@")
    # print(first)
    if(len(first)!=2):
        print("NO")
        return

    user = test[0].split("@")[0]
    hostname = test[0].split("@")[1]
    # user = re.sub(r'[a-zA-Z\d_]|@', '',user)

    # print(user)
    if(valUser(user)==0):
        print ("NO")
        return
    # print(user,hostname)

    if(len(hostname)>32 or len(hostname)<1):
        print ("NO")
        return

    users = hostname.split(".")

    found = 0
    for x in xrange(0,len(users)):
        if(valUser(users[x])==0):
            print("NO")
            return

    # print("passed")

    found=0
    for x in xrange(1,len(test)):
        if(valUser(test[x])==0):
            print("NO")
            return

    print("YES")


# N = int(raw_input())

# while(N>0):

solve();
#     N -= 1
    
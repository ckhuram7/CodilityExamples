# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python 2.7
    binaryString = str(bin(N))[2:]
    count = 0
    prev = 0
    flag = 0
    for character in binaryString:
        if flag == 0:
            if character == '0':
                count = count+1
                flag = 1
                continue
            else:
                prev = count
                count = 0
        if flag == 1:
            if character == '0':
                count = count+1
            else:
                if prev < count:
                    prev = count
                    count = 0
    return prev
	
Second Attempt
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python 2.7
    binaryString = str(bin(N))[2:]
    count = 0
    prev = 0
    for character in binaryString:
        if character == '0':
            count = count + 1
        else:
            if prev < count:
                prev = count
            count = 0
    return prev
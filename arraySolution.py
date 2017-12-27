def solution(A):
    # write your code in Python 2.7
	A.sort()
	if int(A[len(A) -1]) < 1:
		return 1
	else:
		return int(A[len(A) -1]) + 1
	
print solution([-1,-2,-3,-4,-5,49])
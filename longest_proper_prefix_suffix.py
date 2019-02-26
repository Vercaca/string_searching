'''
------------------------------
 Longest Proper prefix-suffix
------------------------------
一個字串,
「最長的相同前綴後綴」就是原字串
「最短的相同前綴後綴」就是空字串
「次長的相同前綴後綴」就是第二長的相同前綴後綴 <--目標
Example:
'abc' --> ''
'abcaa' --> 'a'
'ababa' --> 'aba'

'''
import sys

# failure function (prefix function)
# Dynamic Programming
def failure(p):
    failure_list = [-1] * len(p)

    # iterative, bottom-up DP
    j = -1
    for i in range(1, len(p)):
        while j >= 0 and p[j+1] != p[i]:
            # print('-'*60)
            # print('i = {}'.format(i))
            # print('original j = {}, failure_list = {}'.format(j, failure_list))
            j = failure_list[j]
            # print('new j = {}'.format(j))


        # found the p[i] which is same as p[j+1]
        if p[j+1] == p[i]:
            j+=1

        # get the value of failure[i]
        failure_list[i] = j
    return failure_list

if __name__ == '__main__':
    p = 'abccabc'
    if len(sys.argv) > 1:
        p = sys.argv[1]

    print('p = "{}"'.format(p))
    print(failure(p))

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
'ababa' --> 'abc'

'''

# failure function (prefix function)
# Dynamic Programming
def failure(p):
    failure_list = [-1] * len(p)

    # iterative, bottom-up DP
    j = -1
    for i in range(1, len(p)):
        # print('i = {}, try: {}'.format(i, p[:j+2]))
        while j >= 0 and p[j+1] != p[i]:
            # print('j = {}, failure_list = {}'.format(j, failure_list))
            j = failure_list[j]

        # found the p[i] which is same as p[j+1]
        if p[j+1] == p[i]:
            # print('found "{}", ans = "{}"'.format(p[i], p[:j+2]))
            j+=1

        # get the value of failure[i]
        failure_list[i] = j
    return failure_list

if __name__ == '__main__':
    p = 'abcabbaabc'
    print('p = "{}"'.format(p))
    print(failure(p))

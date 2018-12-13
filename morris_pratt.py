import sys
from longest_proper_prefix_suffix import failure

def Morris_Pratt(t, p):
    if len(p) > len(t):
        return None

    # 預先計算Pattern p的failure function, O(P)
    failure_list = failure(p)
    print('failure_list = {}'.format(failure_list))

    # 進行字串搜尋, O(T)
    j = -1
    for i in range(len(t)):
        while j >= 0 and p[j+1] != t[i]:
            j = failure_list[j]

        # t[i] is useful
        if p[j+1] == t[i]:
            j+=1

        # 搜尋到p
        if j == len(p) -1:
            print('-'*60)
            print('i = {}'.format(i))
            print('Found p at position {}'.format(i-len(p)+1))
            # 如果字串結尾不是'\0'就必須挪動
            # 如果字串結尾是'\0'就能省略這一行
            print('original j = {}'.format(j))
            j = failure_list[j]
            print('new j = {}'.format(j))


if __name__ == '__main__':
    t = 'bbbaccdabababccc'
    p = 'ababc'
    if len(sys.argv) > 2:
        t = sys.argv[1]
        p = sys.argv[2]

    print('>> t = "{}", p = "{}"'.format(t, p))

    print(Morris_Pratt(t,p))

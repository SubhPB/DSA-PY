'''
--- Byimaan ---

# --> print all the possible permutations of "abc"

'''

def permutation(string):

    perms = []

    def backTrack(start,_str):

        if start == len(_str) - 1:
            perms.append(''.join(_str))
            return

        for i in range(start, len(_str)):

            _str[i], _str[start] = _str[start], _str[i]

            backTrack(start+1,_str)

    backTrack(0,[*string])        

    return perms        

if __name__ == '__main__':
    print(permutation('abc'))
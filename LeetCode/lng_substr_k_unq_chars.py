'''
Input:
S = "aabacbebebe", K = 3
Output: 
7
Explanation: 
"cbebebe" is the longest substring with 3 distinct characters
'''

def lng_substr_with_k_unq_chars(string,k):

    start, lng_len = 0, 0 
    tracker = {}
    i, j = 0, 0

    while (j < len(string)):

        tracker[string[j]] = tracker.get(string[j], 0) + 1

        while len(tracker) > k:

            tracker[string[i]] -= 1

            if tracker[string[i]] == 0:     
                del tracker[string[i]]

            i += 1  

        if (len(string[start: start + lng_len]) < j - i + 1 ) and len(tracker) == k:
            start = i
            lng_len = j - i + 1

        j += 1
    return string[start: start + lng_len]              

if __name__ == '__main__':
    S = "aabacbebebe"; K = 3
    
    print(lng_substr_with_k_unq_chars(S,K))
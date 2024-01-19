'''

/* -- Byimaan --

    Input: s = "barfoothefoobarman", words = ["foo","bar"]
    Output: [0,9]

    Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
    Output: [6,9,12]
    Explanation: Since words.length == 3 and words[i].length == 3, the concatenated substring has to be of length 9.
    The substring starting at 6 is "foobarthe". It is the concatenation of ["foo","bar","the"] which is a permutation of words.
    The substring starting at 9 is "barthefoo". It is the concatenation of ["bar","the","foo"] which is a permutation of words.
    The substring starting at 12 is "thefoobar". It is the concatenation of ["the","foo","bar"] which is a permutation of words.

    Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
    Output: [6,9,12]
    Explanation: Since words.length == 3 and words[i].length == 3, the concatenated substring has to be of length 9.
    The substring starting at 6 is "foobarthe". It is the concatenation of ["foo","bar","the"] which is a permutation of words.
    The substring starting at 9 is "barthefoo". It is the concatenation of ["bar","the","foo"] which is a permutation of words.
    The substring starting at 12 is "thefoobar". It is the concatenation of ["the","foo","bar"] which is a permutation of words.

*/

'''

def split_list(string, step):
    _list = []

    for i in range(0,len(string),step):
       temp_str = string[i: i+step]
       _list.append(temp_str)
    
    return _list

def are_same(list1,list2):

    if not( len(list1) == len(list2)):
        return False
    
    else:

        def exists(vals):
            index, val = vals
            
            if val in list2:
                list2[list2.index(val)] = ""
                return True
            else:
                return False

        bools = map(exists,enumerate(list1))
        return all(bools)
    

def concat_sub_str(s,words):

    word_len =  len(''.join(words))
    answers = []
    
    for i in range(len(s) - word_len):

        sub_str = s[i:i+word_len]
        split_sub_str = split_list(sub_str,len(words[0]))
        is_it_same = are_same(split_sub_str,[*words])

        if is_it_same:
            answers.append(i)


    return answers


if __name__ == '__main__':

    s = "barfoofoobarthefoobarman"
    words = ["foo","bar","the"]

    print({'a':1,'d':2} == {'d':2,'a':1})
    

    # print(concat_sub_str(s,words))
    ...
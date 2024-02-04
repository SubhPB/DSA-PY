'''
    A list of all subsets of arr[] where the sum of elements in each subset is equal to target_sum. Each subset should be presented as a list of integers.
    Examples:

    Input: arr[] = [3, 34, 4, 12, 5], target_sum = 9
    Output: [[4, 5]]
    Explanation: Only one subset [4, 5] sums up to 9.

    Input: arr[] = [1, 2, 3, 4], target_sum = 5
    Output: [[1, 4], [2, 3]]
    Explanation: There are two subsets [1, 4] and [2, 3] that sum up to 5.
'''

def sum_subsets(array, target_sum):

    subsets = []

    def backTrack(start, remaining, path):

        if remaining == 0:
            subsets.append([*path])
            return

        for i in range(len(array)):

            if remaining - array[i] >= 0:
                path.append(array[i])
                backTrack(start+1,remaining - array[i], path)
                path.pop()

    backTrack(0,target_sum, [])
    return subsets

if __name__ == "__main__":
    arr= [3, 34, 4, 12, 5]; target_sum= 9

    print(sum_subsets(arr,target_sum))
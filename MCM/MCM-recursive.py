''' -- Byimaan -- 

 ---> Problem Statement:
 
    Given the dimension of a sequence of matrices in an array arr[], where the dimension of the ith matrix is (arr[i-1] * arr[i]),
     the task is to find the most efficient way to multiply these matrices together such that the total number of element multiplications is minimum.

    Examples:

    Input: arr[] = {40, 20, 30, 10, 30}
    Output: 26000
    Explanation:There are 4 matrices of dimensions 40×20, 20×30, 30×10, 10×30.
    Let the input 4 matrices be A, B, C and D.
    The minimum number of  multiplications (cost) are obtained by 
    putting parenthesis in following way (A(BC))D.
    The minimum is 20*30*10 + 40*20*10 + 40*10*30

    Input: arr[] = {1, 2, 3, 4, 3}
    Output: 30
    Explanation: There are 4 matrices of dimensions 1×2, 2×3, 3×4, 4×3. 
    Let the input 4 matrices be A, B, C and D.  
    The minimum number of multiplications are obtained by 
    putting parenthesis in following way ((AB)C)D.
    The minimum number is 1*2*3 + 1*3*4 + 1*4*3 = 30

'''

import math

def MCM_recursive(array):

    initial_i , initial_j = 1, len(array) - 1

    def solve_by_rec(arr: list, i: int, j: int):
        '''
            # multiplication cost of 2 matrixs = M1.m * (M1.n or M2.m) * (M2.n)
            # i and j will lie between the given array or list. 
            # i and j represents some position at the arr.
            # initially i is supposed to be assgined with 1 and j to the (length - 1) of the arr...

            --> 
            # arr[i-1] and arr[i] represents the dimesion ( m and n ) of a matrix.
            # arr[j-1] and arr[j] represents the dimesion ( m and n ) of a another matrix. 
        '''

        if i >= j:
            return 0
            
        # Now, let's introduce k: int, who works like a parenthesis in the set of matrices.
        # what's the limit of k, (mathematically) --> i <= k <= j - 1
        # just to explain the point --> 
        # suppose arr = {40, 20, 30, 10, 30}, if k = 1 then one set = {40,20} & second set = {30, 10, 30}
        # means one set = arr.slice(0,k+1) and another set = arr.slice(k+1, arr.length) ...

        min_cost = math.inf

        for k in range(i,j):
            # this will go from i to j-1...

            first_set_cost = solve_by_rec(arr,i,k)
            second_set_cost = solve_by_rec(arr,k+1,j)

            # total cost = Ist set cost + 2nd set cost + extra cost or ( hidden cost ).
            # what do i mean by extra cost. 
            # After evaluation, -> Ist set came from one matrix and 2nd set came from second matrix. 
            # the extra cost is the multiplication cost of these final matrices
            extra_cost = arr[i-1]*arr[k]*arr[j]

            temp_ans = first_set_cost + second_set_cost + extra_cost
            print(f' temp ans = {temp_ans}, at {i,j}')

            if temp_ans < min_cost:
                min_cost = temp_ans   

        # have to return something...
        return min_cost       

    return solve_by_rec(array,initial_i,initial_j)     

if __name__ == '__main__':

    arr = [40, 20, 30, 10, 30]
    print(MCM_recursive(arr))
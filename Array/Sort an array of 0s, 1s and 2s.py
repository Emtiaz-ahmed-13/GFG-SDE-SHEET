
#problem Link:
# https://www.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s4231/1?utm_source=youtube&utm_medium=courseteam_practice_desc&utm_campaign=sde_sheet_anvita

#intinution

# we use 3 counter for 0,1,2 and then we swap the element with the counter and the mid element
# this alogrithm named is dutch national falg.



class Solution:
    def sort012(self, arr, n):
        # code here
        mid = 0
        left = 0
        right = n - 1  # Set the index of the last element
        while mid <= right:
            if arr[mid] == 0:
            # this a swap with left and mid...
                arr[left], arr[mid] = arr[mid], arr[left]
                left += 1
                mid += 1
            elif arr[mid] == 1:
                mid += 1
            else:  # arr[mid] == 2
                arr[mid], arr[right] = arr[right], arr[mid]
                right -= 1
        return arr
    
#time complexity is O(n)
#space complexity is O(1)
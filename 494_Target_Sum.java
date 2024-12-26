// You are given an integer array nums and an integer target.

// You want to build an expression out of nums by adding one of the symbols '+' and '-' before 
// each integer in nums and then concatenate all the integers.

// For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate 
// them to build the expression "+2-1".
// Return the number of different expressions that you can build, which evaluates to target

class Solution {
    public int findTargetSumWays(int[] nums, int target) {
        return func(nums,target,0,0);
    }
    static int func(int[] arr,int target,int i,int sum){
        if(i>=arr.length){
            return (sum==target)?1:0;
        }
        int sub=func(arr,target,i+1,sum-arr[i]);
        int add=func(arr,target,i+1,sum+arr[i]);
        return sub+add;
    }
}
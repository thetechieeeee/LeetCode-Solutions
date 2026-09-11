import java.util.*;
class Solution {
    public int findDuplicate(int[] nums) {
       int n = nums.length;
       int[] f = new int[n+1];
       for (int i=0;i<n;i++){
        if (f[nums[i]]==0){
            f[nums[i]]+=1;
        }
        else{
            return nums[i];
        }
       }
    return 0;
    }
}
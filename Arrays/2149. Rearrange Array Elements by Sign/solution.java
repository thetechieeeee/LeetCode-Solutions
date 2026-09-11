import java.util.*;
class Solution {
    public int[] rearrangeArray(int[] nums) {
        int n = nums.length;
        int[] ans  = new int[n];
        int p_ind =0,n_ind =1;
        for (int i=0;i<n;i++){
            if (nums[i]<0){
                ans[n_ind] =nums[i];
                n_ind +=2;
            }
            else{
                ans[p_ind]= nums[i];
                p_ind+=2;
            }
        }
        return ans;
    }
}

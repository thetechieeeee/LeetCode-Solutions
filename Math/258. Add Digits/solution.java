class Solution {
    public int addDigits(int num) {
       while (num>=10){
         int dig_sum = 0;
        while (num>0){
           int dig = num%10;
           dig_sum+=dig;
           num/=10;
         
        }
        num = dig_sum;
       } 
       return num;
    }
}
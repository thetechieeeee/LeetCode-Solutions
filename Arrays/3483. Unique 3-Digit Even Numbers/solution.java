import java.util.Set;
import java.util.HashSet;
class Solution {
    public int totalNumbers(int[] digit) {
        Set<Integer> res = new HashSet<>();
        for (int i=0;i<digit.length;i++){
            for (int j=0;j<digit.length;j++){
                for ( int k =0;k<digit.length;k++){
                    if (i==j||j==k||i==k){
                        continue;
                    }
                    if (digit[i] ==0){
                        continue;
                    }
                    if (digit[k]%2!=0){
                        continue;
                    }
                    int num = digit[i]*100+digit[j]*10+digit[k];
                    res.add(num);
                }
            }
        }
    return res.size(); 
    }
}


// pascal's triangle
// https://leetcode.com/problems/pascals-triangle/

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        for i in range(1,numRows):
            temp = [0 for i in range(i+1)]
            for j in range(len(temp)):
                if j == 0 or j == len(temp)-1:
                    temp[j] = 1
                else:
                    temp[j] = ans[i-1][j] + ans[i-1][j-1]
            ans.append(temp)
        return ans
        
        
        
    
// kadane'e algo
// https://leetcode.com/problems/maximum-subarray/

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int prefsum = nums[0];
        int ans = prefsum;
        for (int i=1;i<nums.size();i++){
        	if (prefsum<0){
        		prefsum =0;
        	}
        	prefsum += nums[i];
        	ans = max(prefsum,ans);
        }
        return ans;
    }
};



// sort colors 0 1 2 , dutch national flag 
// https://leetcode.com/problems/sort-colors/

class Solution {
public:
    void sortColors(vector<int>& nums) {
        int mid = 0;
        int i = 0;
        int j = nums.size()-1;
        while(mid<=j){
            if (nums[mid] == 0){
                swap(nums[i],nums[mid]);
                i++;
                mid++;
            }       
            else if(nums[mid] == 2){
                swap(nums[mid],nums[j]);
                j--;
            } 
            else{
                mid++;
            }
        }
        return ;
    }
};
        
                


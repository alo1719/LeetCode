import java.util.Arrays;


// TC: O(nlogn)  SC: O(1)
public class FindPerfectPairs {
    public static int findPerfectPairs(int[] nums) {
        int n = nums.length;

        for (int i = 0; i < n; i++) {
            nums[i] = Math.abs(nums[i]);
        }

        Arrays.sort(nums);

        int ans = 0;
        int right = -1;

        for (int left = 0; left < n; left++) {
            while (right+1 < n && nums[right+1] <= 2*nums[left]) {
                right++;
            }
            ans += right-left;
        }

        return ans;
    }

    public static void main(String[] args) {
        System.out.println(findPerfectPairs(new int[]{2, 5, -3}));  // 2
        System.out.println(findPerfectPairs(new int[]{-9, 6, -2, 1}));  // 2
    }
}

public class BeautyOfArray {
    public static int beautyOfArray(int[] nums) {
        int n = nums.length;
        int[][] dp = new int[n+1][n+1];

        for (int i = 1; i <= n; i++) {
            for (int j = 0; j <= i; j++) {
                int not_del = dp[i-1][j];
                not_del += (nums[i-1] == i-j) ? 1 : 0;
                int del = j == 0 ? 0 : dp[i-1][j-1];
                dp[i][j] = Math.max(not_del, del);
            }
        }

        int maxBeauty = 0;
        for (int j = 0; j <= n; j++) {
            maxBeauty = Math.max(maxBeauty, dp[n][j]);
        }

        return maxBeauty;
    }

    public static void main(String[] args) {
        System.out.println(beautyOfArray(new int[]{1, 3, 2, 5, 4, 5, 3}));  // 4
    }
}

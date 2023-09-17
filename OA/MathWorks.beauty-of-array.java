// TC: O(n^2)  SC: O(n^2)
public class BeautyOfArray {
    public static int beautyOfArray(int[] nums) {
        // f[i][j] = max(f[i-1][j-1], f[i-1][j]+(1 if nums[i-1] == i-j))
        int n = nums.length;
        int[][] f = new int[n+1][n+1];

        for (int i = 1; i <= n; i++) {
            for (int j = 0; j <= i; j++) {
                int not_del = f[i-1][j];
                not_del += (nums[i-1] == i-j) ? 1 : 0;
                int del = j == 0 ? 0 : f[i-1][j-1];
                f[i][j] = Math.max(not_del, del);
            }
        }

        int maxBeauty = 0;
        for (int j = 0; j <= n; j++) {
            maxBeauty = Math.max(maxBeauty, f[n][j]);
        }

        return maxBeauty;
    }

    public static void main(String[] args) {
        System.out.println(beautyOfArray(new int[]{1, 3, 2, 5, 4, 5, 3}));  // 4
    }
}

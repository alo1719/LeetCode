import java.util.Arrays;

public class LC1723 {
    public static int lc1723(int[] jobs, int k) {
        int n = jobs.length;
        int[] acc = new int[1<<n];  // total time for each subset mask
        for (int i = 1; i < (1<<n); i++) {
            int x = Integer.numberOfTrailingZeros(i);
            int y = i-(1<<x);
            acc[i] = acc[y]+jobs[x];
        }

        // dp[i][mask] = min(max(dp[i-1][mask^subset], acc[subset]))
        int[][] dp = new int[k][1<<n];
        for (int i = 0; i < (1<<n); i++) {
            dp[0][i] = acc[i];
        }

        for (int i = 1; i < k; i++) {
            for (int j = 0; j < (1<<n); j++) {
                int minn = Integer.MAX_VALUE;
                for (int x = j; x != 0; x = (x-1)&j) {
                    minn = Math.min(minn, Math.max(dp[i-1][j^x], acc[x]));
                }
                dp[i][j] = minn;
            }
        }
        return dp[k-1][(1<<n)-1];
    }

    public static void main(String[] args) {
        System.out.println(lc1723(new int[]{3,2,3}, 3));  // 3
        System.out.println(lc1723(new int[]{1,2,4,7,8}, 2));  // 11
    }
}

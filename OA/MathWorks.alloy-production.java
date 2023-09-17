import java.util.Arrays;

// TC: O(nlog(max(stock)+budget))  SC: O(1)
public class AlloyProduction {
    public static int alloyProduction(int[] composition, int[] stock, int[] cost, int budget) {
        int left = 0;
        int right = budget+Arrays.stream(stock).max().getAsInt();
        int n = composition.length;

        while (left < right) {
            int mid = (left+right+1)/2;
            int cur = budget;
            boolean can = true;

            for (int i = 0; i < n; i++) {
                if (composition[i]*mid > stock[i]) {
                    cur -= (composition[i]*mid-stock[i])*cost[i];
                    if (cur < 0) {
                        can = false;
                        break;
                    }
                }
            }

            if (can) {
                left = mid;
            } else {
                right = mid-1;
            }
        }

        return left;
    }

    public static void main(String[] args) {
        System.out.println(alloyProduction(new int[]{1, 2}, new int[]{0, 1}, new int[]{1, 1}, 3));  // 1
        System.out.println(alloyProduction(new int[]{2, 1, 2}, new int[]{1, 0, 0}, new int[]{2, 2, 1}, 14));  // 2
    }
}

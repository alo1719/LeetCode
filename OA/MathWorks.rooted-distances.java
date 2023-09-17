import java.util.*;

// TC: O(n)  SC: O(n)
public class RootedDistances {
    private static List<List<Integer>> g;
    private static int[] sum;
    private static int[] dp;
    private static int ans;

    public static int rootedDistances(int tree_nodes, int[] tree_from, int[] tree_to, int[] a) {
        g = new ArrayList<>();
        for (int i = 0; i <= tree_nodes; i++) {
            g.add(new ArrayList<>());
        }

        for (int i = 0; i < tree_nodes-1; ++i) {
            int x = tree_from[i];
            int y = tree_to[i];
            g.get(x).add(y);
            g.get(y).add(x);
        }

        sum = new int[tree_nodes+1];
        dp = new int[tree_nodes+1];
        ans = 0;

        dfs(1, 0, a);
        reroot(1, 0);

        return ans;
    }

    // sum[node] = sum(sum[child])+a[node-1]
    // dp[node] = sum(dp[child])+sum[child]
    private static void dfs(int node, int parent, int[] a) {
        sum[node] = a[node-1];
        for (int child : g.get(node)) {
            if (child == parent) continue;
            dfs(child, node, a);
            sum[node] += sum[child];
            dp[node] += dp[child]+sum[child];  // dp now is indirect sum in the subtree rooted at 1, indirect sum meaning 'should have value - sum[child]'
        }
    }

    // dp[child] += dp[node]-dp[child]-sum[child]
    // dp[child] += sum[1]-sum[child]
    private static void reroot(int node, int parent) {
        ans = Math.max(ans, dp[node]);
        for (int child : g.get(node)) {
            if (child == parent) continue;
            dp[child] += dp[node]-dp[child]-sum[child];  // indirect sum outside child subtree
            dp[child] += sum[1]-sum[child];  // sum outside child subtree
            reroot(child, node);
        }
    }

    public static void main(String[] args) {
        System.out.println(rootedDistances(3, new int[]{1, 2}, new int[]{2, 3}, new int[]{3, 2, 1}));  // 8
        System.out.println(rootedDistances(4, new int[]{1, 3, 3}, new int[]{3, 4, 2}, new int[]{1, 1, 4, 3}));  // 12
    }
}

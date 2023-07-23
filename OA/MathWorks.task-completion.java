import java.util.*;

public class Main {
    public static void main(String[] args) {
        System.out.println(taskCompletion(new int[]{5,4,3,2,1}, new int[]{1,2,3,4,5}, 3));  // 21
        System.out.println(taskCompletion(new int[]{1,2,3,2}, new int[]{1,2,3,2}, 3));  // 8
        System.out.println(taskCompletion(new int[]{2,3,4,2}, new int[]{1,1,1,1}, 2));  // 9
    }

    public static int taskCompletion(int[] reward_1, int[] reward_2, int k) {
        int n = reward_1.length;
        List<Pair> diff = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            diff.add(new Pair(reward_1[i]-reward_2[i], i));
        }
        Collections.sort(diff, Collections.reverseOrder());

        Set<Integer> sett = new HashSet<>();
        for (int i = 0; i < k; i++) {
            sett.add(diff.get(i).index);
        }

        int ans = 0;
        for (int i = 0; i < n; i++) {
            if (sett.contains(i)) ans += reward_1[i];
            else ans += reward_2[i];
        }
        return ans;
    }

    static class Pair implements Comparable<Pair> {
        int diff;
        int index;

        Pair(int diff, int index) {
            this.diff = diff;
            this.index = index;
        }

        @Override
        public int compareTo(Pair other) {
            return Integer.compare(this.diff, other.diff);
        }
    }
}

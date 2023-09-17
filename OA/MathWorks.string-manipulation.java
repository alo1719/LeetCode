import java.util.Arrays;

// TC: O(n^2)  SC: O(n)
public class StringManipulation {
    public static int stringManipulation(String s) {
        StringBuilder sb = new StringBuilder(s).reverse();
        int n = sb.length();
        int ans = 0;
        Character ch = null;
        int j = 0;
        for (int i = 0; i < n-1; i++) {
            if (sb.charAt(i) == sb.charAt(i+1)) {
                if (ch != null && sb.charAt(i) != ch) ans += j;
                while (j < i+2) {
                    if (sb.charAt(j) != sb.charAt(i)) ans += 1;
                    j++;
                }
                ch = sb.charAt(i);
            }
        }
        return ans;
    }

    public static void main(String[] args) {
        System.out.println(stringManipulation("aabaab"));  // 2
        System.out.println(stringManipulation("aabba"));  // 4
        System.out.println(stringManipulation("aabbaba"));  // 7
        System.out.println(stringManipulation("aabbacc"));  // 8
        System.out.println(stringManipulation("acbdacc"));  // 0
        System.out.println(stringManipulation("aabdacc"));  // 4
    }
}

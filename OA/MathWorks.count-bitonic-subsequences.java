import java.util.*;

public class BitonicSubsequences {
    public static int countBitonicSubsequences(int[] arr) {
        int MOD = 1000000007;
        int n = arr.length;
        int maxx = Integer.MIN_VALUE;
        for (int num : arr) {
            maxx = Math.max(maxx, num);
        }
        int[] bucket = new int[maxx+1];
        int[] times = new int[maxx+1];
        for (int i = 0; i < maxx+1; i++) {
            bucket[i] = -1;
            times[i] = 0;
        }
        int[] f = new int[n];
        int[] rf = new int[n];
        
        // f[i] = sum(bucket[j]+times[j]) for j in [0, i-1]
        // bucket[j] = sum(f[k] for arr[k] == j)
        // times[j] = sum(1 for arr[k] == j), bucket and times are updated dynamically
        for (int i = 0; i < n; i++) {
            if (bucket[arr[i]] == -1) {
                bucket[arr[i]] = 0;
            }
            times[arr[i]]++;
            for (int j = 1; j < arr[i]; j++) {
                if (bucket[j] != -1) {
                    f[i] = (f[i]+bucket[j]+times[j])%MOD;
                }
            }
            bucket[arr[i]] = (bucket[arr[i]]+f[i])%MOD;
        }
        
        for (int i = 0; i < maxx+1; i++) {
            bucket[i] = -1;
            times[i] = 0;
        }
        for (int i = n-1; i >= 0; i--) {
            if (bucket[arr[i]] == -1) {
                bucket[arr[i]] = 0;
            }
            times[arr[i]]++;
            for (int j = 1; j < arr[i]; j++) {
                if (bucket[j] != -1) {
                    rf[i] = (rf[i]+bucket[j]+times[j])%MOD;
                }
            }
            bucket[arr[i]] = (bucket[arr[i]]+rf[i])%MOD;
        }
        
        int ans = 0;
        for (int i = 0; i < n; i++) {
            ans = (ans+(f[i]*rf[i]%MOD))%MOD;
        }
        
        return ans;
    }
    
    public static void main(String[] args) {
        int[] arr1 = {1,2,3,2,1};
        int[] arr2 = {1,2,3,1};
        int[] arr3 = {100,5,5,100};
        int[] arr4 = {1,2,4,8,3,2,5,10,2};
        int[] arr5 = {1,2,4,8,3,2,5,2};
        int[] arr6 = {1,2,4,8,3,5,2,3};
        int[] arr7 = {1,2,4,3,5,2,3,6};
        int[] arr8 = {1,2,4,3,5,2,3,2};

        System.out.println(countBitonicSubsequences(arr1));  // 11
        System.out.println(countBitonicSubsequences(arr2));  // 4
        System.out.println(countBitonicSubsequences(arr3));  // 0
        System.out.println(countBitonicSubsequences(arr4));  // 118
        System.out.println(countBitonicSubsequences(arr5));  // 83
        System.out.println(countBitonicSubsequences(arr6));  // 86
        System.out.println(countBitonicSubsequences(arr7));  // 37
        System.out.println(countBitonicSubsequences(arr8));  // 76
    }
}

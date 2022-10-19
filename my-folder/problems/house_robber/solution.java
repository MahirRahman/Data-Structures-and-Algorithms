/*******************************************************
 * Copyright 2022 Mahir Rahman
 * Name: Mahir Rahman
 * Class: CSE374 C
 * Date: 10/19/2022
 * Description: A dyanmic programming approach to determine the maximum amount of money you can rob tonight without alerting the police
*******************************************************/
import java.util.*;

public class Solution {
	// We are using a top down memoization approach
	// Memo holds the already computed values for a particular house or 
	// -1
	int[] memo;
    int rob(int[] houses) {
    	memo = new int[houses.length];
    	Arrays.fill(memo, -1);
        return rob_recurse(houses, houses.length - 1);
    }
    
    int rob_recurse(int[] houses, int i) {
    	// We recurse until each house is visited
    	if (i < 0) {
    		return 0;
    	}
    	// memo helps us reduce time complexity by providing us already computed values
    	if (memo[i] != -1) {
    		return memo[i];
    	}
    	// Takes max from total stolen from prev house
    	// and from this house plus amount obtainable from the houses before the previous one.

    	int res = Math.max(rob_recurse(houses, i-2)+houses[i], rob_recurse(houses,i-1));
    	memo[i] = res;
    	return res;
    }
}
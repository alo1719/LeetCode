#
# @lc app=leetcode.cn id=2115 lang=python3
#
# [2115] Find All Possible Recipes from Given Supplies
#
# https://leetcode.cn/problems/find-all-possible-recipes-from-given-supplies/description/
#
# algorithms
# Medium (41.76%)
# Likes:    31
# Dislikes: 0
# Total Accepted:    5.7K
# Total Submissions: 13.6K
# Testcase Example:  '["bread"]\n[["yeast","flour"]]\n["yeast","flour","corn"]'
#
# You have information about n different recipes. You are given a string array
# recipes and a 2D string array ingredients. The i^th recipe has the name
# recipes[i], and you can create it if you have all the needed ingredients from
# ingredients[i]. Ingredients to a recipe may need to be created from other
# recipes, i.e., ingredients[i] may contain a string that is in recipes.
# 
# You are also given a string array supplies containing all the ingredients
# that you initially have, and you have an infinite supply of all of them.
# 
# Return a list of all the recipes that you can create. You may return the
# answer in any order.
# 
# Note that two recipes may contain each other in their ingredients.
# 
# 
# Example 1:
# 
# 
# Input: recipes = ["bread"], ingredients = [["yeast","flour"]], supplies =
# ["yeast","flour","corn"]
# Output: ["bread"]
# Explanation:
# We can create "bread" since we have the ingredients "yeast" and "flour".
# 
# 
# Example 2:
# 
# 
# Input: recipes = ["bread","sandwich"], ingredients =
# [["yeast","flour"],["bread","meat"]], supplies = ["yeast","flour","meat"]
# Output: ["bread","sandwich"]
# Explanation:
# We can create "bread" since we have the ingredients "yeast" and "flour".
# We can create "sandwich" since we have the ingredient "meat" and can create
# the ingredient "bread".
# 
# 
# Example 3:
# 
# 
# Input: recipes = ["bread","sandwich","burger"], ingredients =
# [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]], supplies =
# ["yeast","flour","meat"]
# Output: ["bread","sandwich","burger"]
# Explanation:
# We can create "bread" since we have the ingredients "yeast" and "flour".
# We can create "sandwich" since we have the ingredient "meat" and can create
# the ingredient "bread".
# We can create "burger" since we have the ingredient "meat" and can create the
# ingredients "bread" and "sandwich".
# 
# 
# 
# Constraints:
# 
# 
# n == recipes.length == ingredients.length
# 1 <= n <= 100
# 1 <= ingredients[i].length, supplies.length <= 100
# 1 <= recipes[i].length, ingredients[i][j].length, supplies[k].length <=
# 10
# recipes[i], ingredients[i][j], and supplies[k] consist only of lowercase
# English letters.
# All the values of recipes and supplies combined are unique.
# Each ingredients[i] does not contain any duplicate values.
# 
# 
#

# @lc code=start
# TC: O(v+e)  SC: O(v+e)
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        ans = set()
        graph = defaultdict(list)
        in_degree = defaultdict(int)
        for i, ingredient in enumerate(ingredients):
            all_in_supplies = True
            for supply in ingredient:
                if supply not in supplies:
                    all_in_supplies = False
                    graph[supply].append(recipes[i])
                    in_degree[recipes[i]] += 1
            if all_in_supplies: ans.add(recipes[i])
        dq = deque()
        dq.extend(ans)
        while dq:
            node = dq.popleft()
            if node not in ans: ans.add(node)
            for to_node in graph[node]:
                in_degree[to_node] -= 1
                if in_degree[to_node] == 0:
                    dq.append(to_node)
        return list(ans)
# @lc code=end


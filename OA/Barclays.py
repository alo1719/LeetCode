"""
str1 is first string.
str2 is second string.
"""
def strConvert(str1, str2):
	dp = [{} for _ in range(31)]
	dp[1][str1] = ""

	for i in range(2, len(str1) + 1):
		for s in dp[i - 1].keys():
			for j in range(len(str1) - i + 1):
				newstr = s
				newstr = newstr[:j] + newstr[j:j+i][::-1] + newstr[j+i:]
				if newstr != s:
					dp[i][newstr] = s
		if str2 in dp[i]:
			return i - 1
	return -1

def main():
	#input for str1
	str1 = str(input())
	
	#input for str2
	str2 = str(input())
	
	
	result = strConvert(str1, str2)
	print(result)	

if __name__ == "__main__":
	main()
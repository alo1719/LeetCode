# TC: O(n)
# SC: O(n)
# total number of subdomains: n
from collections import defaultdict


def countDomain(domains):
    count = defaultdict(int)
    for domain in domains:
        n, url = domain.split()
        n = int(n)
        url_split = url.split(".")
        for i in range(len(url_split)):
            now = ".".join(url_split[i:])
            count[now] += n
    print("[")
    for k, v in count.items():
        print(v, k+',')
    print("]")

domains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
countDomain(domains)
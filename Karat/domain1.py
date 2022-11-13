# TC: O(n)
# SC: O(n)
# total number of subdomains: n
def countDomain(domains):
    count = {}
    for domain in domains:
        n, url = domain.split()
        n = int(n)
        u = url.split(".")
        for i in range(len(u)):
            now = ".".join(u[i:])
            count[now] = count.get(now, 0) + n
    print("[")
    for k, v in count.items():
        print(v, k+',')
    print("]")

domains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
countDomain(domains)
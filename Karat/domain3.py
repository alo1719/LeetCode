# TC: O(n^3)
# SC: O(n)
from collections import defaultdict


def domain3(completed_purchase_user_ids, ad_clicks, all_user_ips):
    dict = defaultdict(int)
    purchased = defaultdict(int)
    for ad_click in ad_clicks:
        ip, _, text = ad_click.split(",")
        dict[text] += 1
        for all_user_ip in all_user_ips:
            user_id, user_ip = all_user_ip.split(",")
            if ip == user_ip:
                if user_id in completed_purchase_user_ids:
                    purchased[text] += 1
    for k, v in dict.items():
        print(purchased[k], "of", v, k)


completed_purchase_user_ids = ["3123122444", "234111110", "8321125440", "99911063"]
ad_clicks = [
    # "IP_Address,Time,Ad_Text",
    "122.121.0.1,2016-11-03 11:41:19,Buy wool coats for your pets",
    "96.3.199.11,2016-10-15 20:18:31,2017 Pet Mittens",
    "122.121.0.250,2016-11-01 06:13:13,The Best Hollywood Coats",
    "82.1.106.8,2016-11-12 23:05:14,Buy wool coats for your pets",
    "92.130.6.144,2017-01-01 03:18:55,Buy wool coats for your pets",
    "92.130.6.145,2017-01-01 03:18:55,2017 Pet Mittens",
]
all_user_ips = [
    # "User_ID,IP_Address",
    "2339985511,122.121.0.155",
    "234111110,122.121.0.1",
    "3123122444,92.130.6.145",
    "39471289472,2001:0db8:ac10:fe01:0000:0000:0000:0000",
    "8321125440,82.1.106.8",
    "99911063,92.130.6.144"
]
# 3 of 3 Buy wool coats for your pets
# 1 of 2 2017 Pet Mittens
# 0 of 1 The Best Hollywood Coats
domain3(completed_purchase_user_ids, ad_clicks, all_user_ips)
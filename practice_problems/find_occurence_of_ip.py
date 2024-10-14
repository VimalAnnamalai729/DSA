logs = [
    "10.0.0.1 - - [10/Oct/2020:13:55:36] GET /index.html 200",
    "10.0.0.2 - - [10/Oct/2020:13:56:36] GET /about.html 200",
    "10.0.0.1 - - [10/Oct/2020:13:57:36] GET /contact.html 200",
    "10.0.0.3 - - [10/Oct/2020:13:58:36] GET /index.html 200",
    "10.0.0.2 - - [10/Oct/2020:13:59:36] GET /home.html 200",
    "10.0.0.2 - - [10/Oct/2020:14:00:36] GET /about.html 200"
]

import re
from collections import Counter


def most_common_ip():
    var = ["10.0.0.1 - GET 2020-08-24", "10.0.0.1 - GET 2020-08-24", "10.0.0.2 - GET 2020-08-20",
           "10.0.0.3 - GET 2020-08-24",
           "10.0.0.3 - GET 2020-08-24", "10.0.0.3 - GET 2020-08-24", "10.0.0.4 - GET 2020-08-24"]

    ip_matches = re.findall(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s', str(var))

    # Solution with Counter
    count_data = Counter(ip_matches)
    result = count_data.most_common()[0]
    print(result)

    # Brute Force Solution
    result_dict = {}
    for ip in ip_matches:
        if result_dict.get(ip):
            result_dict[ip] += 1
        else:
            result_dict.setdefault(ip, 1)
    print(result_dict)
    print(sorted(result_dict.items(), key=lambda item: item[1], reverse=True)[0])


most_common_ip()

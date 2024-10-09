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

results = re.findall(r'\s*(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s', str(logs))
counter_results = Counter(results)

print(counter_results.most_common()[0])
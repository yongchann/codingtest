from collections import Counter
import math
n = Counter(list(input().replace('6','9')))

n['9'] = math.ceil(n['9'] / 2)

print(n.most_common(1)[0][1])
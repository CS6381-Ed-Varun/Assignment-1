import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
import pandas as pd

data = pd.read_csv('./results/latency_AAPL.csv', na_values='.')

# plt.figure(figsize=(4, 3))
plt.boxplot(data)
plt.xticks((1,), ('AAPL',))
plt.title('Simple Broker Approach')
plt.xlabel('Broker Topic(s)')
plt.ylabel('Time (ms)')
plt.ylim((0, 1))
plt.savefig('simplebrokerapproach.png')
plt.show()
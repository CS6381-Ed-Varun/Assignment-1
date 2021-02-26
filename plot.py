import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('./results/latency_AAPL.csv', na_values='.')

# plt.figure(figsize=(4, 3))
plt.boxplot(data)
plt.xticks((1,), ('AAPL',))
plt.title('Simple Broker Approach')
plt.xlabel('Broker Topic(s)')
plt.ylabel('Time (ms)')
plt.ylim((0, 1))
plt.savefig('./results/simple_broker.png')
plt.show()
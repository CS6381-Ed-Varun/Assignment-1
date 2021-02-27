import matplotlib.pyplot as plt
import pandas as pd
import glob

path = './results'                     # use your path
all_files = glob.glob(path + "/*.csv")

data_AAPL = pd.read_csv('./results/latency_AAPL.csv', na_values='.')
data_MSFT = pd.read_csv('./results/latency_MSFT.csv', na_values='.')
data_NFLX = pd.read_csv('./results/latency_NFLX.csv', na_values='.')

"""
data = []

for filename in all_files:
    df = pd.read_csv(filename)
    data.append([data, df])
"""
data = [data_AAPL, data_MSFT, data_NFLX]
print(data)
labels = ['AAPL','MSFT', 'NFLX']
#plt.xticks((1,), ('AAPL','MSFT', 'NFLX'))
plt.figure(figsize=(4, 3))
plt.boxplot(data, labels=labels)
#plt.xticks([0], labels)
plt.title('Complex Flood Approach')
plt.xlabel('Subscriber Topic(s)')
plt.ylabel('Time (ms)')
plt.ylim((0, 1.5))
plt.savefig('./results/complex_flooding.png')
plt.show()
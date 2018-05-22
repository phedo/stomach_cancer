import pandas as pd
import seaborn as sns; sns.set()

import matplotlib.pyplot as plt

df = pd.read_csv('/media/valentin/Data/SR/data/input4heatmap_right.csv')
sns.heatmap(df, vmin=0, vmax=70000)
plt.show()

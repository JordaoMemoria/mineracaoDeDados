import numpy as np
import matplotlib.pyplot as plt



n_groups = 5

means_men = (77.35, 13.02, 5.3, 0.8, 3.5)

means_women = (70.42, 13.09, 6.84, 1.88, 7.75)

fig, ax = plt.subplots()

index = np.arange(n_groups)
bar_width = 0.35

opacity = 0.5
error_config = {'ecolor': '0.3'}

rects1 = ax.bar(index, means_men, bar_width,
                alpha=opacity, color='b', error_kw=error_config,
                label='Male')

rects2 = ax.bar(index + bar_width, means_women, bar_width,
                alpha=opacity, color='r', error_kw=error_config,
                label='Female')

ax.set_xlabel('Range of books read last 12 months')
ax.set_ylabel('Number of samples')
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels(('0 a 20', '21 a 40', '41 a 60', '61 a 80', '81 a 100'))
ax.legend()

fig.tight_layout()
plt.show()
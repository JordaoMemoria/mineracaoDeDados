import numpy as np
import matplotlib.pyplot as plt



n_groups = 5

w = (73.41, 12.85, 7.21, 0.88, 5.63)
naai = (78.73, 10.15, 4.59, 2.10, 4.40)
r = (80.0, 9.75, 5.85, 0.48, 3.90)
mr = (72.02, 13.98, 6.04, 0.86, 7.08)
api = (67.01, 16.49, 7.01, 2.26, 7.21)
baa = (71.42, 14.28, 6.12, 2.04, 6.12)
dk = (80, 16.66, 3.33, 0, 0)
o = (100, 0, 0, 0, 0)


fig, ax = plt.subplots()

index = np.arange(n_groups)
bar_width = 0.1

opacity = 0.8
error_config = {'ecolor': '0.3'}

rects1 = ax.bar(index, w, bar_width,
                alpha=opacity, error_kw=error_config,
                label='College graduate')

rects2 = ax.bar(index + bar_width, naai, bar_width,
                alpha=opacity, error_kw=error_config,
                label='High school graduate')

rects3 = ax.bar(index + bar_width*2, r, bar_width,
                alpha=opacity, error_kw=error_config,
                label='High school incomplete')

rects4 = ax.bar(index + bar_width*3, mr, bar_width,
                alpha=opacity, error_kw=error_config,
                label='Some college, no 4-year degree')

rects5 = ax.bar(index + bar_width*4, api, bar_width,
                alpha=opacity, error_kw=error_config,
                label='Post-graduate after college')

rects6 = ax.bar(index + bar_width*5, baa, bar_width,
                alpha=opacity, error_kw=error_config,
                label='Technical AFTER high school')

rects7 = ax.bar(index + bar_width*6, dk, bar_width,
                alpha=opacity, error_kw=error_config,
                label='None')

rects8 = ax.bar(index + bar_width*7, o, bar_width,
                alpha=opacity, error_kw=error_config,
                label='Don’t know')

ax.set_xlabel('Range of books read last 12 months')
ax.set_ylabel('Number of samples')
ax.set_xticks(index + bar_width*3.4)
ax.set_xticklabels(('0 a 20', '21 a 40', '41 a 60', '61 a 80', '81 a 100'))
ax.legend()

fig.tight_layout()
plt.show()
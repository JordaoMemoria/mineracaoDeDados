import numpy as np
import matplotlib.pyplot as plt



n_groups = 5

w = (72.95, 12.75, 4.08, 1.02, 9.18)
naai = (73.14, 13.12, 6.52, 1.27, 5.92)
r = (75.55, 13.51, 5.18, 1.29, 4.44)
mr = (66.66, 13.72, 8.49, 2.61, 8.49)
api = (60, 26.66, 6.66, 0, 6.66)
baa = (80.16, 9.09, 6.61, 0.82, 3.30)
dk = (77.08, 8.33, 4.16, 4.16, 6.25)
o = (72.22, 16.66, 8.33, 2.77, 0)


fig, ax = plt.subplots()

index = np.arange(n_groups)
bar_width = 0.1

opacity = 0.8
error_config = {'ecolor': '0.3'}

rects1 = ax.bar(index, w, bar_width,
                alpha=opacity, error_kw=error_config,
                label='Divorced')

rects2 = ax.bar(index + bar_width, naai, bar_width,
                alpha=opacity, error_kw=error_config,
                label='Married')

rects3 = ax.bar(index + bar_width*2, r, bar_width,
                alpha=opacity, error_kw=error_config,
                label='Never been married')

rects4 = ax.bar(index + bar_width*3, mr, bar_width,
                alpha=opacity, error_kw=error_config,
                label='Widowed')

rects5 = ax.bar(index + bar_width*4, api, bar_width,
                alpha=opacity, error_kw=error_config,
                label='Don’t know')

rects6 = ax.bar(index + bar_width*5, baa, bar_width,
                alpha=opacity, error_kw=error_config,
                label='Living with a partner')

rects7 = ax.bar(index + bar_width*6, dk, bar_width,
                alpha=opacity, error_kw=error_config,
                label='Single')

rects8 = ax.bar(index + bar_width*7, o, bar_width,
                alpha=opacity, error_kw=error_config,
                label='Separated')

ax.set_xlabel('Range of books read last 12 months')
ax.set_ylabel('Number of samples')
ax.set_xticks(index + bar_width*3.4)
ax.set_xticklabels(('0 a 20', '21 a 40', '41 a 60', '61 a 80', '81 a 100'))
ax.legend()

fig.tight_layout()
plt.show()
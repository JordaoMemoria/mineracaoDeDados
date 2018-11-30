import numpy as np
import matplotlib.pyplot as plt



n_groups = 5

w = (65.46, 14.97, 8.18, 1.79, 9.58)
naai = (77.50, 11.38, 5.69, 1.28, 4.13)
r = (71.73, 15.52, 5.59, 0.93, 6.21)
mr = (74.46, 6.38, 6.38, 0, 12.76)
api = (86.36, 9.09, 0, 0, 4.54)
baa = (69.23, 7.692, 7.69, 7.69, 0.0)
dk = (74.62, 13.68, 4.97, 1.74, 4.97)
o = (67.39, 19.56, 10.86, 2.17, 0)

fig, ax = plt.subplots()

index = np.arange(n_groups)
bar_width = 0.1

opacity = 0.8
error_config = {'ecolor': '0.3'}

rects1 = ax.bar(index, w, bar_width,
                alpha=opacity, error_kw=error_config,
                label='Retired')

rects2 = ax.bar(index + bar_width, naai, bar_width,
                alpha=opacity, error_kw=error_config,
                label='Employed full-time')

rects3 = ax.bar(index + bar_width*2, r, bar_width,
                alpha=opacity, error_kw=error_config,
                label='Employed part-time')

rects4 = ax.bar(index + bar_width*3, mr, bar_width,
                alpha=opacity, error_kw=error_config,
                label='Have own business/self-employed')

rects5 = ax.bar(index + bar_width*4, api, bar_width,
                alpha=opacity, error_kw=error_config,
                label='Student')

rects6 = ax.bar(index + bar_width*5, baa, bar_width,
                alpha=opacity, error_kw=error_config,
                label='Other')

rects7 = ax.bar(index + bar_width*6, dk, bar_width,
                alpha=opacity, error_kw=error_config,
                label='Not employed for pay')

rects8 = ax.bar(index + bar_width*7, o, bar_width,
                alpha=opacity, error_kw=error_config,
                label='Disabled')

ax.set_xlabel('Range of books read last 12 months')
ax.set_ylabel('Number of samples')
ax.set_xticks(index + bar_width*3.4)
ax.set_xticklabels(('0 a 20', '21 a 40', '41 a 60', '61 a 80', '81 a 100'))
ax.legend()

fig.tight_layout()
plt.show()
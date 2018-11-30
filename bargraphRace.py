import numpy as np
import matplotlib.pyplot as plt



n_groups = 5

w = (71.3, 13.9, 6.64, 1.55, 6.59)

naai = (66.66, 16.66, 8.33, 0, 8.33)

r = (65.71, 20, 11.42, 0, 2.85)

mr = (80, 10.9, 1.81, 1.81, 5.45)

api = (91.93, 4.83, 1.61, 0, 1.61)

baa = (83.33, 9.21, 3.54, 1.06, 2.83)

dk = (88.88, 0, 11.12, 0, 0)

o = (83.33, 10.41, 6.25, 0, 0)


fig, ax = plt.subplots()

index = np.arange(n_groups)
bar_width = 0.1

opacity = 0.8
error_config = {'ecolor': '0.3'}

rects1 = ax.bar(index, w, bar_width,
                alpha=opacity, error_kw=error_config,
                label='White')

rects2 = ax.bar(index + bar_width, naai, bar_width,
                alpha=opacity, error_kw=error_config,
                label='Native American/American Indian')

rects3 = ax.bar(index + bar_width*2, r, bar_width,
                alpha=opacity, error_kw=error_config,
                label='Refused')

rects4 = ax.bar(index + bar_width*3, mr, bar_width,
                alpha=opacity, error_kw=error_config,
                label='Mixed Race')

rects5 = ax.bar(index + bar_width*4, api, bar_width,
                alpha=opacity, error_kw=error_config,
                label='Asian or Pacific Islander')

rects6 = ax.bar(index + bar_width*5, baa, bar_width,
                alpha=opacity, error_kw=error_config,
                label='Black or African-American')

rects7 = ax.bar(index + bar_width*6, dk, bar_width,
                alpha=opacity, error_kw=error_config,
                label='Don’t know')

rects8 = ax.bar(index + bar_width*7, o, bar_width,
                alpha=opacity, error_kw=error_config,
                label='Other')

ax.set_xlabel('Range of books read last 12 months')
ax.set_ylabel('Number of samples')
ax.set_xticks(index + bar_width*3.4)
ax.set_xticklabels(('0 a 20', '21 a 40', '41 a 60', '61 a 80', '81 a 100'))
ax.legend()

fig.tight_layout()
plt.show()
from matplotlib import pyplot
import matplotlib.patches as patches
import numpy
import numpy as np

width = 0.2
x = numpy.array(range(20)) 
y1 = [0.121661,0.281750,0.048088,0.128121,0.072397,0.076839,0.087690,0.084153,0.100844,0.124112,0.099711,0.086286,0.106006,0.121070,0.063659,0.144329,0.007514,0.068230,0.142278,0.121074]
y2 = [0.129811,3.953035,0.056121,0.129713,0.085275,0.081876,0.130998,0.114261,0.136584,0.124467,0.102354,0.088917,0.105671,0.132146,0.066593,0.146494,0.008421,0.071322,0.143981,0.161953]
fig = pyplot.figure()
ax = fig.add_subplot(111)
ax.get_xaxis().set_ticks(np.arange(2, 21, 2))
for tick in ax.xaxis.get_major_ticks():
    tick.label.set_horizontalalignment('right')
#ax.get_xaxis().set_ticklabels(['MAP','P@5','P@10', 'P@20','bpref'])
locs, labels = pyplot.xticks()
pyplot.setp(labels, rotation=45)
pyplot.setp(labels, fontsize=15)
bars1 = ax.bar(x,y1, width, color='white') 
bars2 = ax.bar(x + width,y2, width, color='white') 
bars2[1].set_edgecolor('red')
for bar in bars2:
    bar.set_hatch('//')
ax.legend( (bars1[0], bars2[0]), ('baseline', 'similarity search') )

ax.add_patch(
    patches.FancyArrowPatch(
        (2.4, 0.29),
        (1.6, 0.32),
        color='red',
        mutation_scale=20,
        arrowstyle='->'
    )
)
ax.text(2.5, 0.27, 'to 3.95', color='red', weight='bold')

pyplot.grid()
pyplot.xlim(-0.5, 20)
pyplot.ylim(0, 0.32)
pyplot.xlabel('query ID')
pyplot.ylabel('avg query look-up time (sec)')
pyplot.show()

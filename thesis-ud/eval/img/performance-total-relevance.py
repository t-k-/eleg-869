from matplotlib import pyplot
import numpy

width = 0.2
x = numpy.array(range(5)) 
y1 = [0.5315,0.4444,0.4667,0.4944,0.3529]
y2 = [0.8838,0.8000,0.7722,0.7000,0.7644]
fig = pyplot.figure()
ax = fig.add_subplot(111)
ax.get_xaxis().set_ticks(x + .25)
ax.get_xaxis().set_ticklabels(['MAP','P@5','P@10', 'P@20','bpref'])
locs, labels = pyplot.xticks()
pyplot.setp(labels, rotation=45)
pyplot.setp(labels, fontsize=15)
bars1 = ax.bar(x,y1, width, color='white') 
bars2 = ax.bar(x + width,y2, width, color='white') 
for bar in bars2:
    bar.set_hatch('//')
ax.legend( (bars1[0], bars2[0]), ('baseline', 'similarity search') )
pyplot.grid()
pyplot.xlim(-0.5, 5)
pyplot.ylim(0, 1.0)
pyplot.xlabel('x label')
pyplot.ylabel('avg performance')
pyplot.show()

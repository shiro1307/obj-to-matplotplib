import matplotlib.pyplot as plt
import pandas as pd

file = open("test.obj", "r")
content = file.read()
file.close()

vertxt = content[ content.index("v") : content.index("vn") ]
vertslist = [ [ float(x) for x in v.split(' ') ] for v in vertxt.split("v ")[1:] ]

vdf = pd.DataFrame(vertslist)
vdf.columns = ['x','y','z']

faceidxs = content[content.index("f"):].split("f")[1:]
faceidxlist = [ [ int(x[:x.index('/')])-1 for x in f.split(' ')[1:] ] for f in faceidxs ]

projdf = pd.DataFrame()
projdf['x'] = -vdf['x']*0.7 - vdf['z']*0.7
projdf['y'] = vdf['y'] + vdf['x']*0.23 - vdf['z']*0.23

plt.gca().set_aspect(1.0)
plt.scatter(projdf['x'],projdf['y'],2)

for f in faceidxlist:
    plt.fill( projdf['x'][f] , projdf['y'][f] , color='skyblue' , alpha = 0.1, edgecolor='black')

plt.show()
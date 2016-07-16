import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

'''
diq3c.py: main code. Generates data.csv, which is used by 3g and 3d (whence 3e-f). Plots original graph as well as charter school data.
Source data from pubschls.csv 14avgdb.csv (CA DoE) CA zip codes.csv (Zillow, diq3.py)
'''

schools = pd.read_csv('pubschls.csv', index_col=0)
schoolAPIs = pd.read_csv('14avgdb.csv', index_col=0)
schooldata = pd.concat([schools, schoolAPIs], axis=1, join='inner')
schooldata.to_csv('schooldata.csv')
schooldata = schooldata.reset_index()
schooldata['Zip'] = schooldata['Zip'].apply(lambda x: x[0:5])

zillow = pd.read_csv('CA zip codes.csv')
zillow['Zip'] = zillow.Zip.apply(lambda x: str(x))

data = pd.merge(zillow, schooldata, how='left', on='Zip')
data.to_csv('data.csv')

w = data.loc[:,['Zip', 'zindex','avg_w']]
w = w.dropna(how='any')
z = w.groupby('Zip').mean()
z.to_csv('zindex-api.csv')
zmod = z[z.zindex < 1000000]

f, (ax1, ax2) = plt.subplots(1, 2, sharey=True, figsize=(18,6))
ax1.scatter(z.zindex,z.avg_w, color='red', marker='^', alpha=0.2)
ax2.scatter(zmod.zindex,zmod.avg_w, color='red', marker='^', alpha=0.3)
ax1.set_title("Figure 1: Zillow Home Value Index versus school API score at each CA ZIP", loc='left')
ax1.set_xlabel("Zillow Home Value Index ($)")
ax2.set_xlabel("Zillow Home Value Index ($)")
ax1.set_ylabel("Average school API score")
ax1.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
ax2.ticklabel_format(style='sci', axis='x', scilimits=(0,0))

zlinex = np.linspace(0,1000000)
m = 0.000166546 # from excel
b = 724.3871119
zliney = zlinex * m + b
ax2.plot(zlinex, zliney)

f.savefig("zindex-api.png")


u = data[data.Charter == 'Y']
v = u.loc[:,['Zip','zindex','avg_w']]
v = v.dropna(how='any')
t = v.groupby('Zip').mean()
t.to_csv('zindex-api-charter.csv')
tmod = t[t.zindex < 1000000]

g, (ax3, ax4) = plt.subplots(1, 2, sharey=True, figsize=(18,6))
ax3.scatter(t.zindex,t.avg_w, color='red', marker='^', alpha=0.2)
ax4.scatter(tmod.zindex,tmod.avg_w, color='red', marker='^', alpha=0.3)
ax3.set_title("Figure 2: Zillow Home Value Index versus charter school API at each CA ZIP", loc='left')
ax3.set_xlabel("Zillow Home Value Index ($)")
ax4.set_xlabel("Zillow Home Value Index ($)")
ax3.set_ylabel("Average charter school API score")
ax3.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
ax4.ticklabel_format(style='sci', axis='x', scilimits=(0,0))

tlinex = np.linspace(0,1000000)
tm = 0.000102684 # from excel
tb = 744.9811074
tliney = tlinex * tm + tb
ax4.plot(tlinex, tliney)

g.savefig("zindex-api-charter.png")


uu = data[data.Charter == 'N']
vv = uu.loc[:,['Zip','zindex','avg_w']]
vv = vv.dropna(how='any')
tt = vv.groupby('Zip').mean()
tt.to_csv('zindex-api-noncharter.csv')
ttmod = tt[tt.zindex < 1000000]

h, (ax5, ax6) = plt.subplots(1, 2, sharey=True, figsize=(18,6))
ax5.scatter(tt.zindex,tt.avg_w, color='red', marker='^', alpha=0.2)
ax6.scatter(ttmod.zindex,ttmod.avg_w, color='red', marker='^', alpha=0.3)
ax5.set_title("Figure 3: Zillow Home Value Index versus non-charter school API at each CA ZIP", loc='left')
ax5.set_xlabel("Zillow Home Value Index ($)")
ax6.set_xlabel("Zillow Home Value Index ($)")
ax5.set_ylabel("Average non-charter school API score")
ax5.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
ax6.ticklabel_format(style='sci', axis='x', scilimits=(0,0))

ttlinex = np.linspace(0,1000000)
ttm = 0.000166639 # from excel
ttb = 722.7609
ttliney = ttlinex * ttm + ttb
ax6.plot(ttlinex, ttliney)

h.savefig("zindex-api-non-charter.png")
"""
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(1,1,1)
ax.scatter(z.zindex, z.avg_w, color='red', marker='^', alpha=0.2)
ax.set_title("Zillow Home Value Index versus school API score at each CA ZIP code")
ax.set_xlabel("Zillow Home Value Index ($)")
ax.set_ylabel("Average school API score")
fig.savefig("zindex-api.png")
plt.xlim([0,1000000])
fig.savefig("zindex-api2.png")


fig2 = plt.figure(figsize=(8,6))
ax2 = fig2.add_subplot(1,1,1)
ax2.scatter(t.zindex,u.avg_w,color='blue',alpha=0.2)
ax2.set_title("Zindex vs charter school API score at each CA ZIP code")
ax2.set_xlabel("Zillow Home Value Index ($)")
ax2.set_ylabel("Average charter schol API score")
fig2.savefig("zindex-api-charter.png")
plt.xlim([0,1000000])
fig2.savefig("zindex-api-charter2.png")
"""

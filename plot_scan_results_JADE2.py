import numpy as np
import matplotlib.pyplot as plt
import sys

basename= sys.argv[1]
wd= 4
ht= 4

mn= 10.0
idx= np.outer(np.arange(90,1000,100),np.ones(10))+np.outer(np.ones(10),np.arange(10))
print(idx)
idx= np.array(idx.flatten(), dtype= int)
final_cor= np.zeros((ht,wd))
final_cor_e= np.zeros((ht,wd))
fig, ax= plt.subplots(ht,wd,sharex= True, sharey= True)
for i in range(ht):
    for j in range(wd):
        fname= basename+"_"+str(i*wd+j)+"_results.txt"
        try:
            with open(fname, "r") as f:
                d= np.loadtxt(f)
        except:
            print("error trying to load {}".format(fname))
        else:
            if len(d) > 0:
                ax[i,j].plot(1-d[:,1])
                ax[i,j].plot(1-d[:,3])
                mn= np.min([mn,np.amin(1-d[:,3])])
                final_cor[i,j]= np.mean(d[idx,1])
                final_cor_e[i,j]= np.mean(d[idx,3])
            ax[i,j].set_title("scan_"+str(i)+"_"+str(j))
print(mn)
plt.yscale("log")
fig.savefig(basename+"_accuracy.png")

fig, ax= plt.subplots(1,2,sharey=True)
for i in range(ht):
    for j in range(wd):
        fname= basename+"_"+str(i*wd+j)+"_results.txt"
        try:
            with open(fname, "r") as f:
                d= np.loadtxt(f)
        except:
            print("error trying to load {}".format(fname))
        else:
            if len(d) > 0:
                ax[0].plot(1-d[:,1])
                ax[1].plot(1-d[:,3])
#plt.yscale("log")
fig.savefig(basename+"_accuracy_2.png")

final_loss= np.zeros((ht,wd))
final_loss_e= np.zeros((ht,wd))
fig, ax= plt.subplots(ht,wd,sharex= True, sharey= True)
mn= 10.0
for i in range(ht):
    for j in range(wd):
        fname= basename+"_"+str(i*wd+j)+"_results.txt"
        try:
            with open(fname, "r") as f:
                d= np.loadtxt(f)
        except:
            print("error trying to load {}".format(fname))
        else:
            if len(d) > 0:
                ax[i,j].plot(d[:,2])
                ax[i,j].plot(d[:,4])
                mn= np.min([mn,np.amin(d[:,4])])
                final_loss[i,j]= np.mean(d[idx,2])
                final_loss_e[i,j]= np.mean(d[idx,4])
            ax[i,j].set_title("scan_"+str(i)+"_"+str(j))
#plt.yscale("log")
#plt.ylim([0.01,10])
print(mn)
fig.savefig(basename+"_loss.png")
fig, ax= plt.subplots(ht,wd,sharex= True, sharey= True)
for i in range(ht):
    for j in range(wd):
        fname= basename+"_"+str(i*wd+j)+"_results.txt"
        try:
            with open(fname, "r") as f:
                d= np.loadtxt(f)
        except:
            print("error trying to load {}".format(fname))
        else:
            if len(d) > 0:
                ax[i,j].errorbar(d[:,0],d[:,5],yerr=d[:,6])
                ax[i,j].plot(d[:,0],d[:,7])
                ax[i,j].plot(d[:,0],d[:,8])
            ax[i,j].set_title("scan_"+str(i)+"_"+str(j))
fig.savefig(basename+"_activity.png")

print(final_cor)
print(final_cor_e)
print(final_loss)
print(final_loss_e)

fig, ax= plt.subplots(2,2)
im= ax[0,0].imshow(final_cor)
fig.colorbar(im,ax=ax[0,0])
im= ax[0,1].imshow(final_cor_e)
fig.colorbar(im,ax=ax[0,1])
im= ax[1,0].imshow(final_loss)
fig.colorbar(im,ax=ax[1,0])
im= ax[1,1].imshow(final_loss_e)
fig.colorbar(im,ax=ax[1,1])

plt.show()

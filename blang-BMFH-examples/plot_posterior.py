import matplotlib.pyplot as plt
import pandas as pd


# ! ENTER NAME OF RANDOM VARIABLE HERE:
rvar_name = ""
model_name = ""


# Setting up the directory
samples_folder = "/Users/sahand/Desktop/blang/blang-BMFH-examples/"+model_name+"/results/samples/"

# Reads .csv file and plots the histogram
file = pd.read_csv(samples_folder + rvar_name + ".csv")
vals = file['value']


plt.hist(vals, histtype="stepfilled", density=True, alpha=0.85, bins=30, label="posterior distribution",
         color=['cornflowerblue'])
plt.xlim(0, 1)
plt.xlabel("Value of $" + rvar_name + "$")
plt.ylim(0, 5)
plt.ylabel("Density")
plt.title("Posterior distribution of parameter $" + rvar_name + "$")
plt.legend()
fig = plt.gcf()
plt.show()
fig.savefig(model_name+"/plots/posterior_of_"+rvar_name+".png")
fig.savefig(model_name+"/plots/posterior_of_"+rvar_name+".pdf")

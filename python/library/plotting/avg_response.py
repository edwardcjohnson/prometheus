#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats
import seaborn as sns
sns.set(style="white",color_codes=True)
sns.set_palette(sns.cubehelix_palette(8, start=.5, rot=-.75))
titanic = sns.load_dataset("titanic")
tips = sns.load_dataset("tips")


def avg_response(df, x, y_obs, y_est, save=False):

    fig, ax1 = plt.subplots(figsize=(15,15))

    ax2 = ax1.twinx()

    x_name = x
    if df[x].dtype == "int":
        x  = df[x].astype("category")
    elif df[x].dtype == "float":
        x = pd.cut(df[x], bins=10)

    df_grouped = df.groupby([x])[y_obs, y_est].agg({"mean":"mean", "std err":"sem", "count":"count"})
    
    x_vals = range(len(df_grouped))
    y_vals = df_grouped["mean"][y_est]
    ax1.errorbar(x_vals, y_vals,yerr=df_grouped["std err"][y_est], fmt='-',
        marker='o',color="R", mec='black', ms=10, mew=2, linewidth=4, capsize=10, elinewidth=2)

    y_vals = df_grouped["mean"][y_obs]
    ax1.plot(x_vals, y_vals, '-', label=y_obs, marker='o',
        color = "G",mec='black', ms=10, mew=2, linewidth=4)

    y_vals = df_grouped["count"][y_obs]
    ax2.bar(x_vals,y_vals, color='DarkSlateGray', alpha = 0.25)

    ax1.set_xlim(x_vals[0]-0.2,x_vals[-1]+1)
    x_levels = list(y_vals.index)
    plt.xticks(x_vals, x_levels)
    ax1.set_xticklabels(x_levels, rotation=45)
    ax1.grid(False)
    ax2.grid(False)
    font_size = 20
    ax1.set_xlabel(x_name, fontsize=font_size)
    ax1.set_ylabel(y_obs, fontsize=font_size)
    ax2.set_ylabel("count", fontsize=font_size)
    plt.title("Average {y} for groups of {x}".format(x=x_name,y=y_obs),  fontsize=font_size+5)
    ax1.legend([y_obs, y_est], fontsize=font_size-2)
    if save:
        fig.savefig("/home/edward/work/repos/prometheus/python/plots/avg_response/{}.png".format(x_name), bbox_inches='tight')
    plt.show()

# Basic usage and save to png
avg_response(tips, "day", #"day"
"tip",
"total_bill",save=False)


# Loop over all variables in df and save to pdf
from matplotlib.backends.backend_pdf import PdfPages
pp = PdfPages('/home/edward/work/repos/prometheus/python/plots/avg_response/multipage.pdf')
for var in tips.dtypes.index:
    avg_response(tips, var, "tip", "total_bill")
    pp.savefig()
pp.close()




# Other plot types
sns.boxplot(x="sex", y="total_bill", hue="day", data=tips);plt.show()

sns.pointplot(x="sex", y="total_bill", data=tips);plt.show()



tip_grouped = tips.groupby(["day"])["tip", "total_bill"].agg({"mean":"mean", "std err":"sem", "count":"count"})
print(tip_grouped)

print(tip_grouped["mean"]["tip"])

print(tip_grouped["mean"].sort_values(["tip"])["tip"].index)

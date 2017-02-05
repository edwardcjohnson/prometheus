#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats

import seaborn as sns
sns.set(style="whitegrid", color_codes=True)
titanic = sns.load_dataset("titanic")
tips = sns.load_dataset("tips")


def avg_response(df, x, y_obs, y_est):

    fig, ax1 = plt.subplots()

    ax2 = ax1.twinx()
    #ax1.plot(x, y1, 'g-')
    #ax2.plot(x, y2, 'b-')

    ax1.set_xlabel('X data')
    ax1.set_ylabel('Y1 data', color='g')
    ax2.set_ylabel('Y2 data', color='b')


    x_name = x
    if df[x].dtype == "int":
        x  = df[x].astype("category")
    elif df[x].dtype == "float":
        x = pd.cut(df[x], bins=10)

    df_grouped = df.groupby([x])[y_obs, y_est].agg({"mean":"mean", "std err":"sem", "count":"count"})
    #fig = plt.figure()
    x_vals = np.arange(len(df_grouped))
    plt.errorbar(x_vals,df_grouped["mean"][y_est],yerr=df_grouped["std err"][y_est], fmt='-o',marker='s', mfc='red',
             mec='green', ms=2, mew=2)
    ax1.plot(x_vals, df_grouped["mean"][y_obs], 'b-', label=y_obs)
    ax2.bar(x_vals, df_grouped["count"][y_obs], color='DarkSlateGray', alpha = 0.3)
    plt.axis(xmin=x_vals[0]-1,xmax=x_vals[-1]+1)
    x_levels = list(df_grouped.index)
    plt.xticks(x_vals, x_levels, rotation=45)
    ax1.grid(False)
    ax2.grid(False)
    plt.xlabel(x_name, fontsize=14)
    plt.ylabel(y_obs, fontsize=14)
    #fig.savefig("{}.jpeg".format(x))
    plt.title("Average {y} for groups of {x}".format(x=x_name,y=y_obs))
    plt.show()

avg_response(tips, "tip", #"day"
    "total_bill",
    "tip") 









def avg_response(df, x, y_obs, y_est):

    fig, ax1 = plt.subplots()

    ax2 = ax1.twinx()
    # ax1.plot(x, y1, 'g-')
    # ax2.plot(x, y2, 'b-')

    # ax1.set_xlabel('X data')
    # ax1.set_ylabel('Y1 data', color='g')
    # ax2.set_ylabel('Y2 data', color='b')


    x_name = x
    if df[x].dtype == "int":
        x  = df[x].astype("category")
    elif df[x].dtype == "float":
        x = pd.cut(df[x], bins=10)

    df_grouped = df.groupby([x])[y_obs, y_est].agg({"mean":"mean", "std err":"sem", "count":"count"})
    #fig = plt.figure()
    x_vals = np.arange(len(df_grouped))
    ax1.errorbar(x_vals,df_grouped["mean"][y_est],yerr=df_grouped["std err"][y_est], fmt='-o',marker='s', mfc='red',
             mec='green', ms=2, mew=2)
    ax1.plot(x_vals, df_grouped["mean"][y_obs], 'b-', label=y_obs)
    ax2.bar(x_vals, df_grouped["count"][y_obs], color='DarkSlateGray', alpha = 0.3)
    ax1.set_xlim(x_vals[0]-1,x_vals[-1]+1)
    x_levels = list(df_grouped.index)
    ax1.set_xticklabels(x_levels, rotation=90)
    ax1.grid(False)
    ax2.grid(False)
    ax1.set_xlabel(x_name, fontsize=14)

    ax1.set_ylabel(y_obs, fontsize=14)
    ax2.set_ylabel("Count", fontsize=14)
    #fig.savefig("{}.jpeg".format(x))
    plt.title("Average {y} for groups of {x}".format(x=x_name,y=y_obs))
    plt.show()
    #print(x_levels)

avg_response(tips, "tip", #"day"
    "total_bill",
    "tip") 
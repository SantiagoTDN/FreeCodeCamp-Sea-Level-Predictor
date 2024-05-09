import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
pd.set_option("display.precision", 7)
def draw_plot():
    # Read data from file
    df=pd.read_csv("/workspace/boilerplate-sea-level-predictor/epa-sea-level.csv")

    # Create scatter plot
    df.plot(x="Year",y="CSIRO Adjusted Sea Level",kind="scatter")



    # Create first line of best fit
    pd.set_option("display.precision", 7)
    p=pd.DataFrame(pd.Series(range(2014,2051)),columns=["Year"])
    df_p=pd.concat([df,p],ignore_index=True)
    lin1=linregress(x=df["Year"],y=df["CSIRO Adjusted Sea Level"])
    bfl1=lin1.slope*df_p["Year"]+lin1.intercept

    # Create second line of best fit
    df2=df.copy()
    df2=df2.loc[df2["Year"]>=2000]
    df_p2=df_p.copy()
    df_p2=df_p2.loc[df_p2["Year"]>=2000]
    lin2=linregress(x=df2["Year"],y=df2["CSIRO Adjusted Sea Level"])
    bfl2=lin2.slope*df_p2["Year"]+lin2.intercept
    plt.scatter(df_p["Year"],df_p["CSIRO Adjusted Sea Level"])
    plt.plot(df_p["Year"],bfl1)
    plt.plot(df_p2["Year"],bfl2)
    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
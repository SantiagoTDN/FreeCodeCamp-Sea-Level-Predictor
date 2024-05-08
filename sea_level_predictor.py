import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df=pd.read_csv("/workspace/boilerplate-sea-level-predictor/epa-sea-level.csv")

    # Create scatter plot
    df.plot(x="Year",y="CSIRO Adjusted Sea Level",kind="scatter")


    # Create first line of best fit
    lin1=linregress(x=df["Year"],y=df["CSIRO Adjusted Sea Level"])
    bfl1=lin1.slope*df["Year"]+lin1.intercept
    lin1.slope*2050+lin1.intercept
    df2050=df.copy()
    df2050.loc[134] = pd.Series({"Year": 2050,"CSIRO Adjusted Sea Level": lin1.slope*2050+lin1.intercept})
    lin2=linregress(x=df2050["Year"],y=df2050["CSIRO Adjusted Sea Level"])
    bfl2=lin2.slope*df2050["Year"]+lin2.intercept

    # Create second line of best fit
    df_sl=df.loc[df["Year"]>=2000.0]
    lin3=linregress(x=df_sl["Year"],y=df_sl["CSIRO Adjusted Sea Level"])
    bfl3=lin3.slope*df_sl["Year"]+lin3.intercept
    lin3.slope*2050+lin3.intercept
    df_sl2050=df_sl.copy()
    df_sl2050.loc[134] = pd.Series({"Year": 2050,"CSIRO Adjusted Sea Level": lin3.slope*2050+lin3.intercept})
    lin4=linregress(x=df_sl2050["Year"],y=df_sl2050["CSIRO Adjusted Sea Level"])
    bfl4=lin4.slope*df_sl2050["Year"]+lin4.intercept
    plt.scatter(df2050["Year"],df2050["CSIRO Adjusted Sea Level"])
    plt.plot(df_sl2050["Year"],bfl4)
    plt.plot(df2050["Year"],bfl2)

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
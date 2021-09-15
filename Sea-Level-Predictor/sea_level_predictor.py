import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")
    x = df["Year"]  # set x to year
    y = df["CSIRO Adjusted Sea Level"]  # set y to sea level


    # Create scatter plot of x and y (given data)
    fig, ax = plt.subplots()
    plt.scatter(x, y)


    # Create first line of best fit based on all data
    regress = linregress(x, y)
    predict_x = pd.Series([i for i in range(1880, 2051)])
    predict_y = regress.slope * predict_x + regress.intercept
    plt.plot(predict_x, predict_y)


    # Create second line of best fit based on data from 2000 on
    update_df = df.loc[df["Year"] >= 2000]
    update_x = update_df["Year"]
    update_y = update_df["CSIRO Adjusted Sea Level"]
    regress2 = linregress(update_x, update_y)
    predict_x2 = pd.Series([i for i in range(2000, 2051)])
    predict_y2 = regress2.slope * predict_x2 + regress2.intercept
    plt.plot(predict_x2, predict_y2)

    # Add labels and title
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")
    
    # Save plot and return data for testing
    plt.savefig('sea_level_plot.png')
    return plt.gca()
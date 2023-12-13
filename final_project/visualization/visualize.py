# Importing visualization libraries
import matplotlib.pyplot as plt  # For creating plots
import pandas as pd  # For data manipulation
import seaborn as sns  # For high-level data visualization

def covid_time_series(df: pd.DataFrame):
    """
    Plots a time series of COVID-19 cases using data from a DataFrame.
    
    Args:
        df (pd.DataFrame): The DataFrame containing time-series data of COVID-19 cases.
        
    This function creates a line plot with 'date' on the x-axis, 'value' (cases) on the y-axis,
    and differentiates data points by 'country_region' using color hues.
    """
    # Creating the line plot with Seaborn
    sns.lineplot(
        data=df,
        x="date",
        y="value",
        hue="country_region"
    )
    
    # Formatting the plot with proper rotation of x-ticks, labels, and title
    plt.xticks(rotation=15)
    plt.xlabel("Date")
    plt.ylabel("Value")
    plt.title("Latam covid time series")

def top_countries(df: pd.DataFrame, n: int, highlight: list):
    """
    Plots a bar chart of the top n countries with the highest total COVID-19 cases,
    highlighting specific countries.
    
    Args:
        df (pd.DataFrame): The DataFrame containing COVID-19 cases data.
        n (int): The number of top countries to display.
        highlight (list): A list of countries to highlight in the visualization.
    
    The function identifies the top n countries based on total case counts and
    applies a custom color to the highlighted countries for the bar chart.
    """
    # Helper function to apply color based on country being in the highlight list
    def highlight_color(value, highlight_values):
        if value in highlight_values:
            return "red"
        return "lightblue"
    
    # Data processing to get the top n countries and apply the highlight color
    top_countries_df = (
        df
        .select_columns(["country_region", "value"])
        .groupby(["country_region"])
        .aggregate("sum")
        .sort_values("value", ascending=False)
        .reset_index()
        .head(n)
        .transform_column(
            column_name="country_region",
            function=lambda x: highlight_color(x, highlight),
            dest_column_name="color"
        )
    )
    
    # Creating the barplot with Seaborn
    sns.barplot(
        data=top_countries_df,
        x="value",
        y="country_region",
        palette=top_countries_df.color
    )
    
    # Adding labels and title to the bar plot
    plt.xlabel("Value")
    plt.ylabel("Country Region")
    plt.title("Latam countries in a global context");



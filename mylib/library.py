'''
library file
'''
import polars as pl
import matplotlib.pyplot as plt

def load_dataset(data):
    df = pl.read_csv(data)
    return df

def create_histogram(data, col):
    data[col].to_pandas().hist()
    plt.xlabel('Values')
    plt.ylabel('Frequency')
    plt.title('Basic Histogram')
    plt.show()

def grab_stdev(data, col):
    return data[col].std()

def grab_max(data, col):
    return data[col].max()

def grab_mean(data, col):
    return data[col].mean()

def grab_median(data, col):
    return data[col].median()

def histogram_ast(data):
    df = load_dataset(data)
    plt.figure(figsize=(10, 6))
    plt.hist(df["AST"].to_pandas(), bins=20)
    plt.title("Assists in 2023-24 Season-1")
    plt.xlabel("NBA Players")
    plt.ylabel("%")
    plt.savefig("assists.png")
    plt.show()

def bar_chart_points(data):
    df = load_dataset(data)
    plt.figure(figsize=(10, 6))
    plt.bar(df["Pos"].to_pandas(), df["AST"].to_pandas(), color="maroon", width=0.4)
    plt.xlabel("Players Position")
    plt.ylabel("Player Assists")
    plt.title("Assist Counts by Position in NBA")
    plt.savefig("points_by_position1.png")
    plt.show()

    


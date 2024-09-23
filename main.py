import polars as pl
from mylib.library import (
    grab_mean,
    grab_median,
    grab_stdev,
    histogram_ast,
    bar_chart_points,
    load_dataset
)

data1 = "NBA_Data.csv"


def nba_summary(data):
    return data.describe()


def g_describe(data):
    g = load_dataset(data)
    return nba_summary(g)


def stat_update(data, col):
    df = load_dataset(data)
    mean1 = grab_mean(df, col)
    median1 = grab_median(df, col)
    stdev1 = grab_stdev(df, col)
    df1 = pd.DataFrame([mean1, median1, stdev1])
    return df1


histogram_ast(data1)
bar_chart_points(data1)


def save_to_md(data):
    test = g_describe(data)
    test2 = stat_update(data, "AST")
    mkdown = test.write_csv(None)
    mkdown2 = test2.write_csv(None)
    with open("nbastats1.md", "a", encoding="utf-8") as file:
        file.write("Describe:\n")
        file.write(mkdown)
        file.write("Summarize:\n")
        file.write(mkdown2)
        file.write("n\n")
        file.write("![NBA_1](points_by_position.png)\n")
        file.write("n\n")
        file.write("![NBA_2](assists.png)\n")


if __name__ == "__main__":
    save_to_md(data1)
from mylib.library import grab_max,grab_mean,grab_median,grab_stdev
import polars as pl

test_file = "NBA_Data.csv"
df = pl.read_csv(test_file)


def test_library():
    # testing out library functions
    assert grab_max(df,"Age")== 39
    assert grab_mean(df, "MP") == 907.7578231292517
    assert grab_median(df, "3P") == 22
    assert grab_stdev(df, "FGA") == 358.1608549422147


if __name__ == "__main__":
    test_library()

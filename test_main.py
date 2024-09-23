from main import g_describe, grab_mean, grab_median, grab_stdev
import polars as pl

test_file = "NBA_Data.csv"
df = pl.read_csv(test_file)

def test_describe():
    # testing out nba_summary
    test_summary = g_describe(test_file)
    assert test_summary.shape == (8, 27)
    assert grab_mean(df, "AST") == 99.86530612244898
    assert grab_median(df, "AST") == 54.0
    assert grab_stdev(df, "AST") == 124.65415734967988


if __name__ == "__main__":
    test_describe()

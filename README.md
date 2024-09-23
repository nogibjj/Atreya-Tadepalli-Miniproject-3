# Atreya-Tadepalli-Miniproject-3

## Summary
In this project, I have utilized polars to load the 2023-2024 NBA data. Similar to my individual project, I have prepared visualizations and a statistical summary available in markdown. I did not particularly notice the speed, but I imagine in larger projects that polars will help reduce the time taken to process.


The below serves as a summary of the individual project involving the preparation of descriptive statistics and the markdown file. 

Format.yml
[![CI](https://github.com/atreyat12/avt12-Week2Pandas/actions/workflows/format.yml/badge.svg)](https://github.com/atreyat12/avt12-Week2Pandas/actions/workflows/format.yml)

Build.yml
[![CI](https://github.com/atreyat12/avt12-Week2Pandas/actions/workflows/install.yml/badge.svg)](https://github.com/atreyat12/avt12-Week2Pandas/actions/workflows/install.yml)

Test.yml
[![CI](https://github.com/atreyat12/avt12-Week2Pandas/actions/workflows/test.yml/badge.svg)](https://github.com/atreyat12/avt12-Week2Pandas/actions/workflows/test.yml)

Lint.yml
[![CI](https://github.com/atreyat12/avt12-Week2Pandas/actions/workflows/lint.yml/badge.svg)](https://github.com/atreyat12/avt12-Week2Pandas/actions/workflows/lint.yml)

## **Data Source**

For this assignment, I used the records from the recently concluded 2023-2024 NBA season. This data was made available at basketball-reference.com, and I attach the link to the data below. https://www.basketball-reference.com/leagues/NBA_2024_totals.html

## **Functions**

I retain the same functions as I previously used to analyze the NBA dataset using Pandas. As part of the data summary, the library contains several functions intended to highlight the data.

```grab_stdev(data,col)``` - returns the standard deviation of the provided column within the dataset

```grab_max(data,col)``` - returns the maximum value within the provided column within the dataset

```grab_median(data,col)``` - returns the median of the provided column within the dataset

```grab_mean(data,col)``` - returns the mean of all values within the provided column within the dataset

```histogram_ast(data)```  - prepares the graph for assists within the dataset. In this case, it is meant to represent the distribution of player assists.

```bar_chart_points(data)``` - this prepares a bar chart to show the assists based on position played by the player.

```create_histogram(data,col)``` - this function prepares a histogram to represent all the values within a provided column within the dataset.

```load_dataset(data)``` - loads the dataset into a pandas dataframe


## **Example Summary Output**

I include here a snapshot of the descriptive statistics, as applied to all variables present within the dataset.


## **Data Visualizations**

Below showcases the two visualizations produced using the functions called in the main file. These both pertain to the assists distribution within the NBA from last season.

### Data Visualization 1 - Histogram of Assist Totals

![Figure_1](https://github.com/user-attachments/assets/3604d4c0-5e1b-4100-ae11-ce4ac4bf5cdc)

### Data Visualization 2 - Assists by Position

![Figure_2](https://github.com/user-attachments/assets/26724b1a-1fbf-432f-af89-7d68698a0e3d)

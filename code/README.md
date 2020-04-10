# Code

This directory houses our code, which we used to do the following:

- [Exploratory Data Analysis](#exploratory-data-analysis)
- [Data Pre Processing](#data-pre-processing)
  - [Cleaning](#cleaning)
  - [Filtering](#filtering)
  - [Joining](#joining)

To see what data we used, click [here](../data).

## Exploratory Data Analysis

Before we began creating models

## Data Pre Processing

In its original state, the data is mostly unusable; There are a lot of columns that contain information that are not relevant, and rows that are outside the scope of our assignment. This section highlights what we have done to prepare the data for proper analysis.

### Cleaning

Remove null columns.

```
# Which columns have all missing values
null_columns = inspections_df.columns[inspections_df.isna().all()].tolist()

# Drop all the columns that add nothing
inspections_df.drop(columns=null_columns, axis=1, inplace=True)
```

If there are instances of transforming data values, please let me know.

### Filtering

As previously mentioned, there are rows that we discovered that would not have any impact on our study. In some cases, the Yelp reviews are not about a restaurant in the Las Vegas metropolitan area, and in other cases, the Yelp reviews are not about a restaurant at all.

In order to make sure we selected only the data that mattered to us we used the following lines of code:

```
# Only select the cities in the Las Vegas area, including Henderson
cities = ["Las Vegas", "North Las Vegas", "Henderson"]

yelp_df = yelp_df.loc[yelp_df["city"].isin(cities)]

# Only select the categories that are restaurants, only 184 rows are missing values
yelp_df = yelp_df[yelp_df.categories.notna()]
yelp_df = yelp_df[yelp_df.categories.str.contains('Restaurant' or 'food' or 'bar')]
```

There is definitely more filtering to be done and this section can probaly go after joining

### Joining

In order to analyze the relationship between yelp reviews and the potential for a food inspection, we need to join these five tables:

- business.json
- review.json
- restaurant_establishments.csv
- restaurant_inspection_types.csv
- restaurant_inspections_.csv

#### Joining Inspection data

First, join the the inspections data on the look up table (inspection_types) based on the inspection_type_id. This will give us all inspections with a proper labeling of the inspection type.

Next, join the inspection data with types on the the establishments dataset based on the permit_id. Each establishment has a primary key of the permit_id that is listed in each inspection.

#### Joining Yelp Data

Each review has a business id that can easily be joined to the business.json file. This gives us a table of reviews that have detailed business information.

#### Joining the Sets Together

This process is difficult because the text data we would want to use to match the business name to the establishment name is not always the same.

Before joining we tried to normalize the names by making them lowercase and trimming whitespace.

For us, it is only important to find the establishment match for each business. We do not care about the cases where an establishment exists but the matching business does not. We care about matching an existing business to an establishment.

Here is a list of know problems we encountered while trying to join the yelp datasets to the inspection datasets:
- The names of the restaurants are recorded differently.
- The names of the restaurant changed over time.
- The location of the restaurant changes, but the name stays the same.
- Multiple restaurants map to the same longitude and latitude coordinates.
- A restaurant only exits in one of the datasets.

In the end we created an automated script that tried to create a mapping. We used the following metrics to narrow down the mapping to its best possible match:
- Filter based on a longitude and latitude radius
- Calculate the levenshtein distance of the restaurant names
- Calculate the % levenshtein distance --> (levenshtein distance / length of string)
- Find the longest matching substring
- Filter out common restaurant words

We manually validated a small subset (x rows) of these rows and found that in y% of the time, the script gave a correct match.

### Aggregating Yelp Reviews

Not yet

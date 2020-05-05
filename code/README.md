# Code

This directory houses our code, which we used to do the following:

- [Exploratory Data Analysis](#exploratory-data-analysis)
- [Data Pre Processing](#data-pre-processing)
  - [Cleaning](#cleaning)
  - [Filtering](#filtering)
  - [Joining](#joining-the-data)
- [Modeling](#modeling)

To see what data we used, click [here](../data).

## Exploratory Data Analysis

Before we began creating models we wanted to see what we could find out about the data we were working with.

The following graphs were helpful for us to determine what the general trends in our data were.

## Data Pre Processing

In its original state, the data is mostly unusable; There are a lot of columns that contain information that are not relevant, and rows that are outside the scope of our assignment. This section highlights what we have done to prepare the data for proper analysis.

### Cleaning

#### Removing Nulls

If a column is null then it is useless, and if an inpsection is missing it's data then we cannot pass it into a model. We removed those values using this code:

```
# Which columns have all missing values
null_columns = inspections_df.columns[inspections_df.isna().all()].tolist()

# Drop all the columns that add nothing
inspections_df.drop(columns=null_columns, axis=1, inplace=True)
```

#### Text Cleaning

In order for us to properly join the two datasets and to extract information from the reviews, we would like the text to be as clean as possible. We decided to lower case the reviews and strip the tokens for white space.

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

### Joining the Data

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

#### Creating the Mapping File

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

After finding the closed possible match for each business and establishment pair, we manually validated every single business. If the business matched correctly to an establishment we kept the row, if it did not we ignored that business.

#### Joining the Two Datasets

After creating a list of valid mappings of business_id's and facility_id's it was quite easy to merge both halves of the dataset. We combined the business.csv from yelp and the establishments from the SNHD based on the mapping file.

### Aggregating the Inspections

Multiple inspections could occur at the same business at the same day and could cause duplicate reviews to appear in our final dataset. In order to solve this problem we took combined all the inspections that happened at the same business_id and the same date and we took the average of the demerits.

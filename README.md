# US Bikeshare Data Analysis Project


This project is part of the **Programming for Data Science with Python** course by Udacity. The purpose of the project is to explore data related to bike share systems in three major U.S. cities: Chicago, New York City, and Washington, DC. The project is implemented in Python, using libraries such as Pandas and NumPy.
||||||| 06513a5

### Date created
on September second 2024.


## Project Overview

In this project, I wrote a Python script that interacts with the user to analyze bikeshare data. The user can choose a city, a month, and a day of the week to filter the data, and the script then provides statistical insights into the bike sharing patterns for the selected filters.

### Features

- **User Input:** Allows the user to select a city, month, and day of the week for analysis.
- **Data Filtering:** Filters the dataset based on the user's input.
- **Statistical Analysis:** Calculates and displays the following statistics:
  - Popular times of travel (most common month, day, hour)
  - Popular stations and trip (most common start and end stations, most frequent trip)
  - Trip duration (total and average duration)
  - User info (counts of user types, gender, and birth year statistics)

## Project Structure

- **bikeshare.py:** The main Python script that contains the logic for loading data, filtering data, and calculating statistics.
- **README.md:** This file, providing an overview of the project.

## How to Run the Project

To run the project on your local machine:

1. Clone this repository:
    ```bash
    git clone https://github.com/AbdalruhmanIssa/US_Bikeshare_Udacity_Project.git
    ```
2. Navigate to the project directory:
    ```bash
    cd US_Bikeshare_Udacity_Project
    ```
3. Run the Python script:
    ```bash
    python bikeshare.py
    ```

## Dataset

The project uses three datasets provided by Udacity:
- `chicago.csv`
- `new_york_city.csv`
- `washington.csv`

These datasets contain bike share data for the respective cities. The data includes information about each trip taken, such as the start and end time, start and end station, trip duration, and user information (gender, birth year, etc.).

## Requirements

To run the project, you'll need:
- Python 3.x
- Pandas
- NumPy

You can install the required libraries using pip:
```bash
pip install pandas numpy

## Limitations

While this project provides valuable insights into bikeshare usage, it has some limitations:
- The analysis is limited to the data provided by the bikeshare companies for the selected cities and may not be representative of the entire population's usage patterns.
- Data is only available for certain time periods and does not cover all months or years.
- Some datasets, like Washington's, do not include gender or birth year information, limiting demographic analysis.

## Possible Future Improvements

- **Incorporate Additional Data:** Expanding the dataset to include more cities or data from different years could provide a more comprehensive analysis.
- **Advanced Analytics:** Implement machine learning models to predict bikeshare usage patterns based on weather, day of the week, or other factors.
- **Interactive Visualizations:** Develop interactive dashboards to allow users to explore the data more intuitively.

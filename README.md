# Football Data Analysis

Small Python project focused on football data analysis.

The goal of this project is to practice data analysis using Python, Pandas and Matplotlib with a simple football dataset.

## Technologies

* Python
* Pandas
* Matplotlib
* CSV data

## What the project does

* Loads football player data from a CSV file
* Cleans column names and text values
* Calculates goal contributions using goals and assists
* Calculates goals, assists and goal contributions per 90 minutes
* Filters per 90 rankings using a minimum minutes threshold
* Shows the top players by total goal contributions
* Shows the top players by goal contributions per 90 minutes
* Calculates average goals by position
* Creates a team summary with goals, assists and goal contributions
* Exports analysis results to CSV files
* Generates charts with Matplotlib

## Why I created this project

I created this project to improve my Python skills and start applying data analysis concepts to sports, especially football.

I am interested in data, artificial intelligence and technology applied to sport.

## How to run

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the project:

```bash
python main.py
```

## Output

The project creates an `outputs` folder automatically and generates the following files:

```text
outputs/player_metrics.csv
outputs/top_players.csv
outputs/top_players_per_90.csv
outputs/team_summary.csv
outputs/goal_contributions.png
outputs/goal_contributions_per_90.png
```

## Generated charts

The project generates two charts:

* `goal_contributions.png`: shows the top players by total goal contributions.
* `goal_contributions_per_90.png`: shows the top players by goal contributions per 90 minutes.

## Future improvements

Some possible improvements for this project are:

* Use a larger football dataset
* Add more player statistics
* Add more charts and visualisations
* Add SQL analysis using SQLite
* Create a Jupyter Notebook version of the analysis

## Overview

This project provides a Flask-based API to analyze climate data using a SQLite database. The API allows users to query precipitation data, station details, temperature observations, and statistical temperature summaries for specific date ranges.

### Running the Application

1. Clone the repository or copy the files.
2. Run the Flask application:

```
python app.py
```

1. Access the API at `http://127.0.0.1:5000/` in your browser.

## API Endpoints

### Base URL

```
http://127.0.0.1:5000/
```

### Available Routes

| Route                     | Description                                              |
| ------------------------- | -------------------------------------------------------- |
| `/`                       | List all available API routes                            |
| `/api/v1.0/precipitation` | Retrieve last 12 months of precipitation data            |
| `/api/v1.0/stations`      | Get a list of weather stations                           |
| `/api/v1.0/tobs`          | Get temperature observations for the most active station |
| `/api/v1.0/<start>`       | Get min, avg, and max temp from the start date onward    |
| `/api/v1.0/<start>/<end>` | Get min, avg, and max temp within a date range           |

## Example Usage

### Retrieving Precipitation Data

```
curl http://127.0.0.1:5000/api/v1.0/precipitation
```

### Fetching Station List

```
curl http://127.0.0.1:5000/api/v1.0/stations
```

### Temperature Observations

```
curl http://127.0.0.1:5000/api/v1.0/tobs
```

### Temperature Summary for a Date Range

​	Note- you must use the date format "YYYY-MM-DD"

```
curl http://127.0.0.1:5000/api/v1.0/2017-01-01/2017-12-31
```

## 

# Climate Data Analysis - Jupyter Notebook

## Overview

This Jupyter Notebook (`climate_starter.ipynb`) is designed to analyze climate data using the dataset, sourced from a SQLite database (`hawaii.sqlite`), contains weather records from multiple stations in Hawaii.

## Dataset

The notebook utilizes climate data stored in the `hawaii.sqlite` database. This dataset includes:

- **Measurements**: Precipitation and temperature readings by date and station.
- **Stations**: List of weather stations collecting climate data.

## Notebook Features

- **Database Connection**: Establishes a connection with the SQLite database.
- **Precipitation Analysis**: Queries and visualizes precipitation data over time.
- **Station Analysis**: Identifies the most active weather station.
- **Temperature Observations**: Retrieves and plots temperature data.
- **Temperature Statistics**: Computes min, avg, and max temperatures for given date ranges.

## Running the Notebook

1. Open a terminal or command prompt and navigate to the project directory.
2. Launch Jupyter Notebook:

```
jupyter notebook
```

1. Open `climate_starter.ipynb` in your browser.
2. Run each cell to execute the analysis.

## Sample Outputs

Below are sample images demonstrating the data analysis performed in the notebook.

### Precipitation Trends

<img src="C:\Repos\sqlalchemy-challenge\SurfsUp\Images\precip_plot.png" style="zoom:50%;" />



### Temperature Observations

<img src="C:\Repos\sqlalchemy-challenge\SurfsUp\Images\temp_plot.png" style="zoom:50%;" />

## Conclusion

This notebook provides an in-depth analysis of climate data from Hawaii, allowing users to explore historical precipitation trends, temperature observations, and station statistics. By leveraging Python and SQLAlchemy, the project demonstrates how to retrieve, process, and visualize climate data efficiently. This tool can be further expanded to include additional analyses, making it valuable for researchers and data enthusiasts interested in climate patterns.
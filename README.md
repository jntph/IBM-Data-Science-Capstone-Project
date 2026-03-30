# 🚀 Winning Space Race with Data Science

**IBM Data Science Professional Certificate — Capstone Project**
*Author: Tien Pham | October 2024*

---

## Overview

SpaceX has disrupted the space launch industry by reusing the first stage of its Falcon 9 rocket, dramatically reducing the cost per launch. The ability to predict whether the first stage will successfully land is key to estimating those costs — and that's exactly what this project does.

This project builds a predictive model for SpaceX Falcon 9 first stage landing outcomes using historical launch data. The goal is to give a hypothetical competitor, **SpaceY**, a data-driven edge when bidding against SpaceX.

---

## Business Problem

SpaceX advertises Falcon 9 launches at around $62 million — far cheaper than competitors — largely because they recover and reuse the first stage booster. If we can predict whether the first stage will land successfully, we can estimate the true cost of a launch and make more competitive bids.

---

## Project Structure

| Notebook / File | Description |
|---|---|
| `jupyter-labs-spacex-data-collection-api.ipynb` | Data collection via SpaceX REST API |
| `jupyter-labs-webscraping.ipynb` | Web scraping launch records from Wikipedia |
| `labs-jupyter-spacex-Data wrangling.ipynb` | Data wrangling and feature engineering |
| `edadataviz.ipynb` | Exploratory data analysis with visualizations |
| `jupyter-labs-eda-sql-coursera_sqllite.ipynb` | EDA using SQL queries |
| `lab_jupyter_launch_site_location.ipynb` | Interactive launch site map with Folium |
| `spacex_dash_app.py` | Interactive dashboard built with Plotly Dash |
| `SpaceX_Machine Learning Prediction_Part_5.ipynb` | Classification models and predictive analysis |

---

## Methodology

### 1. Data Collection
- **SpaceX REST API** — Queried past launch records from `https://api.spacexdata.com/v4/launches/past` using the `requests` library, then normalized the JSON response into a pandas DataFrame.
- **Web Scraping** — Used `BeautifulSoup` to scrape the Wikipedia page for the list of Falcon 9 and Falcon Heavy launches, parsing HTML tables into a structured DataFrame.

### 2. Data Wrangling
- Identified and handled missing values (null payload mass replaced with column mean)
- Calculated launch counts per site and orbit
- Created a binary `landing_class` column: **1 = Success**, **0 = Failure**

### 3. Exploratory Data Analysis (EDA)
- **Visualizations**: Scatter plots correlating Payload Mass, Flight Number, Launch Site, and Orbit Type; bar charts for success rate by orbit; line graph for yearly success trends (2010–2020)
- **SQL queries**: Explored landing outcomes, payload mass statistics, site-specific records, and time-filtered results using SQLite

### 4. Interactive Visual Analytics
- **Folium Map**: Plotted all launch sites on an interactive map with color-coded markers showing launch outcomes, site statistics, and geographic proximities
- **Plotly Dash Dashboard**: Built an interactive dashboard with a dropdown to filter by launch site (pie chart of success/failure rates) and a payload mass range slider linked to a scatter plot of outcomes by booster version

### 5. Predictive Analysis (Classification)
Standardized features, split into train/test sets, and evaluated four models:

| Model | Accuracy |
|---|---|
| Support Vector Machine (SVM) | **>80%** ✅ Best |
| Logistic Regression | ~80% |
| Decision Tree Classifier | ~77% |
| K-Nearest Neighbors | ~75% |

The **SVM model** achieved the highest accuracy and was selected as the final model.

---

## Key Findings

**Launch Sites**
- Four active launch sites: CCAFS SLC-40, KSC LC-39A, VAFB SLC-4E (CA), and CCAFS LC-40 — all near the US coastline and as close to the Equator as possible on US soil
- **KSC LC-39A** had the highest success rate at **76.9%** (10 successes, 3 failures)
- CCAFS SLC-40 showed improving success rates in later flights

**Payload & Orbit Insights**
- All flights from flight number 79 onward were successful, regardless of payload
- Launches with payload in the **3,000–5,000 kg** range had the highest success rate
- Orbits **ES-L1, GEO, HEO, and SSO** achieved 100% success rates
- The **FT Booster Version** had the highest success rate among all booster versions
- Total NASA payload carried: **99,980 kg**

**Trends Over Time**
- Success rate rose sharply after 2013, with a dip in 2017 before recovering in 2019

**Best Predictive Model**
- SVM correctly identified all 12 successful landings (True Positives) and all 3 failures (True Negatives) with 0 False Negatives — yielding accuracy above 80%

---

## Technologies Used

- **Python**: `pandas`, `numpy`, `requests`, `BeautifulSoup`, `scikit-learn`, `matplotlib`, `seaborn`
- **SQL**: SQLite via `ipython-sql`
- **Mapping**: `Folium`
- **Dashboard**: `Plotly Dash`
- **ML Models**: Logistic Regression, Support Vector Machines, Decision Tree, K-Nearest Neighbors (all via `scikit-learn`)

---

## Conclusions & Future Work

The SVM predictive model delivered promising results and demonstrates that SpaceY can use data science to estimate Falcon 9 launch costs competitively. However, this is an initial study and further improvements are recommended:

- Train on more recent and larger datasets for improved reliability
- Incorporate geo-simulation models to better understand the effect of launch site location
- Conduct detailed product cost and risk analysis
- Explore partnerships and investor opportunities based on model outcomes

---

## Acknowledgements

This project was completed as the capstone for the [IBM Data Science Professional Certificate](https://www.coursera.org/professional-certificates/ibm-data-science) on Coursera.

> **Note:** Interactive Folium maps may not render directly on GitHub due to Jupyter Notebook trust settings. Please download the notebook and run locally to view the maps.

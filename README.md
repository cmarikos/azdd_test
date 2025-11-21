

## **Overview**

I cleaned voter demographic datasets locally using Pandas and then loaded the processed tables into BigQuery using BigQuery’s native Jupyter notebooks. These cleaned tables feed into this [Looker Dashboard]([https://lookerstudio.google.com/s/nVIQdVs0Um4](https://cmarikos.github.io/azdd_test/)).

---

## **Data Cleaning (Python)**

* I loaded raw `.xlsx` files with Pandas
* I fixed merged headers, inconsistent labels, and duplicate column names

* Combined all non–Dem/Rep parties into a single `"third"` category
* Added sort keys (e.g., ordered age buckets) to control chart ordering in Looker Studio
* And uploaded each cleaned DataFrame directly into BigQuery

---

## **BigQuery Jupyter Notebooks**

* I used BigQuery’s notebook environment to run SQL, inspect tables, and manage loading jobs
* I used an external [GeoJSON from CDPHE Open Data](https://data-cdphe.opendata.arcgis.com/datasets/colorado-county-boundaries/explore)
* I created a view to join partisanship data with geospatial data for mapping
* I also reshaped all the formatted wide tables (age, gender, party status) into long format using `melt()` so looker could use them for summary tables




If you want, I can condense it even further or write a polished “professional deliverable” version.

# fantastic-octo-disco
A full ETL pipeline that fetches berry data from the PokeAPI, generates synthetic insights with random number generation, and outputs an Excel workbook with key metrics.
### Technologies
- Python
- Pandas
- OpenPyXL
- Requests

### Features
- Data Generation: Pulls berry data from PokeAPI and augments it with Python's random module.
- Extraction: Uses Pandas to load and parse the generated dataset.
- Transformation: Cleans, validates, and aggregates data to derive actionable insights.
- Load: Exports results to a formatted Excel workbook highlighting key findings.


### The Proccess
I kicked off by building a script to fetch and format data using Python's requests library to query the PokeAPI. After some trial and error, this step came together smoothly.\

Next came the ETL core with Pandas, which proved trickier. Brainstorming transformation ideas—like cleaning, validation, and aggregation—required diving deep into docs and iterating through many prototypes until it clicked.\

Finally, I tied everything into main.py, generating an Excel output that showcases the insights.
### What I Learned
- Making API requests and handling JSON responses
- File I/O for saving generated data
- Pandas for data manipulation and analysis
- OpenPyXL for Excel workbook creation
- Full ETL pipeline design
### Overall Growth
Building on my prior ETL experience with Pandas and PySpark, this project sharpened my skills in data aggregation, insight generation, and Pandas mastery. It was a hands-on way to level up from past work.

### How can it be Improved
- Enhance data generation for richer synthetic datasets.
- Leverage more PokeAPI berry details in transformations.
- Develop additional metrics and visualizations.
- Build an interactive dashboard (e.g., with Streamlit or Dash) to consolidate insights.

### Running the Project
Install dependencies:
```bash
pip install pandas openpyxl
```

Run the data generation script:
```bash 
python berries.py
```

Run the ETL pipeline:
```bash
python main.py
```

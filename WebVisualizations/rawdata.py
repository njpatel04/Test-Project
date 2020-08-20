import pandas as pd

# Read the csv file in
data_file = "Resources/cities.csv"
data_df = pd.read_csv(data_file)

# Save to file
data_df.to_html('htmldata.html', index=False)
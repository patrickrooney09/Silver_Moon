from ._anvil_designer import Form1Template
from anvil import *

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def file_loader_1_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    pass

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    import pandas as pd
# Replace 'file1.csv' and 'file2.csv' with your actual file names
file1_path = 'Emp_ID_and_Badge.csv'
file2_path = 'AOD_Test2.csv'

# Read the first CSV file with badge number and employee ID
df1 = pd.read_csv(file1_path)

# Read the second CSV file with just employee ID
df2 = pd.read_csv(file2_path)

# Merge the two dataframes based on the 'ID' and 'Employee Id' columns
merged_df = pd.merge(df2, df1[['ID', 'Badge']], left_on='Employee ID', right_on='ID', how='left')

# Drop the redundant 'ID' column
# merged_df = merged_df.drop(columns='ID')

# Save the final merged dataframe to a new CSV file
output_file_path = 'final_output_file.csv'
merged_df.to_csv(output_file_path, index=False)

# Display the final merged dataframe
merged_df

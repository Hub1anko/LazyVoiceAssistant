import pandas as pd

# ------------- #
# Save to Excel #
# ------------- #

class SaveToExcel:
    # TO-DO: change input from different columns to df
    def __init__(self, Task, TaskType, Time, Date, StartTime, excel_filename):
        # Create a DataFrame with the new data
        self.new_data = {
            'Date': [Date],
            'Task': [Task],
            'TaskType': [TaskType],
            'Est': [Time],
            'Start': [StartTime],
        }
        self.filename = excel_filename
    def SaveToExcel(self):
        self.new_df = pd.DataFrame(self.new_data)

        # Load existing data from the Excel file (if it exists)
        try:
            existing_df = pd.read_excel(self.filename)
        except FileNotFoundError:
            existing_df = pd.DataFrame()

        # Append new data to the existing DataFrame
        combined_df = pd.concat([existing_df, self.new_df], ignore_index=True)

        # Save the combined DataFrame back to the Excel file
        combined_df.to_excel(self.filename, index=False)
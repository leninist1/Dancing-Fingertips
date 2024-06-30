import matplotlib.pyplot as plt
import pandas as pd
from PIL.ImageQt import rgb


class PlotRecord:
    def __init__(self):
        self.colors = [(0.23, 0.26, 0.82)]
    def read_file(self):
        df = pd.read_csv("record.csv", sep=",", header='infer')
        return df

    def write_file(self, record_date, record_score):
        # Read the CSV file
        df = pd.read_csv("record.csv", sep=",", header='infer')

        # Check if the record_date exists in the file
        if record_date in df['record_date'].values:
            # Update the existing record
            df.loc[df['record_date'] == record_date, 'record_score'] += record_score
        else:
            # Add a new record
            new_data = {"record_date": [record_date], "record_score": [record_score]}
            new_row = pd.DataFrame(new_data)
            df = pd.concat([df, new_row], ignore_index=True)

        # Write the updated dataframe back to the CSV file
        df.to_csv("record.csv", index=False)
        self.plot_bar_chart()

    def plot_bar_chart(self):
        df = pd.read_csv("record.csv", sep=",", header='infer')

        # Convert the 'record_date' column to datetime format
        df['record_date'] = pd.to_datetime(df['record_date'], format='%m-%d')

        # Sort the dataframe by record_date for better visualization
        # df = df.sort_values(by='record_date')

        # Convert dates to strings in 'Month-Day' format for x-axis labels
        record_date_list = df['record_date'].dt.strftime('%m-%d').tolist()
        # record_date_list = df['record_date'].tolist()
        record_score_list = df['record_score'].tolist()
        # Plotting the bar chart
        plt.figure(figsize=(8, 6), facecolor=None)
        plt.bar(record_date_list, record_score_list, color=self.colors[0])
        for i, s in enumerate(record_score_list):
            plt.text(i, s+0.5, str(s), ha='center', va='bottom')
        for i, d in enumerate(record_date_list):
            plt.text(i, record_score_list[i]-20, d, ha='center', va='top')
        plt.axis('off')
        plt.tight_layout()  # Adjust layout to make room for the rotated x-axis labels
        ax = plt.gca()
        ax.spines['bottom'].set_color('none')
        ax.spines['left'].set_color('none')
        plt.savefig("record.png")
        plt.show()

#
# plot_record = PlotRecord()
# plot_record.read_file()
# plot_record.write_file('07-02', 0)
# plot_record.read_file()
# plot_record.plot_bar_chart()
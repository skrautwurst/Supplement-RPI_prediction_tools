import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot_heatmap_from_csv(csv_file_path):
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(csv_file_path, index_col=0)
    #print(df.isna())

    # Set parameters for heatmap
    plt.figure(figsize=(8, 14))  # Set the size of the heatmap figure
    sns.set(font_scale=1)
    cmap_custom = plt.get_cmap('crest').copy()
    cmap_custom.set_bad("lightgrey")
    values = df.to_numpy(dtype=float)

    # Create the heatmap
    sns.heatmap(df, annot=True, annot_kws={'color':"w", 'fontsize': 10}, cmap=cmap_custom, linewidth=.5, square=True, cbar_kws = {'label': 'evaluation score', "shrink":.7}, vmin=0.0, vmax=4.0, mask=values<0)

    # Set plot labels and title
    plt.xlabel("RPI", fontsize = 14)
    plt.ylabel("prediction tools", fontsize = 14)

    # Save figure
    plt.savefig('/home/evaluation_heatmap.pdf', format='pdf')
    plt.savefig('/home/evaluation_heatmap.svg', format='svg')

    # Display the heatmap
    plt.show()

if __name__ == "__main__":
    csv_file_path = '/home/evaluation_table.csv'
    plot_heatmap_from_csv(csv_file_path)

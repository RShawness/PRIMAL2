import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter


def create_plot(directory, filename):
    # read csv file into x and y vectors, with 'Step' column as the x list and 'Value' column as the y list
    # plot the x vs y list with matplotlib and save as a png file
    figure_path = os.path.join(directory, filename)

    df = pd.read_csv(figure_path)
    x = df['Step']
    y = df['Value']
    # apply a smoothing filter to the y values
    y = savgol_filter(y, 10, 0)
    # clear the plot
    plt.clf()
    plt.plot(x, y)
    # set the x axis label as "Episode"
    plt.xlabel('Episode')
    
    # set line width to 3
    plt.rcParams['lines.linewidth'] = 3

    # extract the y axis label from the filename
    raw_name = filename.split('_')[-1]
    # strip off '.csv' from the end of the filename
    y_label = raw_name[:-4]
    plt.ylabel(y_label)

    # change the font size of the x and y labels
    plt.rcParams.update({'font.size': 18})

    # save figure
    figure_name = y_label + '.png'
    save_path = os.path.join(directory, "Plots/", figure_name)
    plt.savefig(save_path, bbox_inches='tight', dpi=300)

def process_directory(directory):
    # make a "Plots" subdirectory in directory
    try:
        os.mkdir(os.path.join(directory, 'Plots'))
    except:
        "Plots directory already exists"
    # process all csv files in the directory
    for filename in os.listdir(directory):
        if filename.endswith('.csv'):
            create_plot(directory, filename)

if __name__ == "__main__":
    process_directory(sys.argv[1])




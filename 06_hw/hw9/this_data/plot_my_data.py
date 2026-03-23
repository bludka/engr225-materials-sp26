import matplotlib.pyplot as plt
from this_data.my_data_stats import my_avg, my_outliers

def time_series_plot(data):
    '''
    Plot a time series, the mean, 
    upper and lower thresholds (3x standard deviation)
    and the outliers.
    '''
    mean = my_avg(data)
    outliers,outlier_indices,upper,lower = my_outliers(data)
    t = list(range(len(data)))
    plt.plot(t,data,color='blue',marker='*')
    plt.plot([t[0],t[-1]],[mean, mean],color='black')
    plt.plot([t[0],t[-1]],[upper, upper],color='black',linestyle='--')
    plt.plot([t[0],t[-1]],[lower, lower],color='black',linestyle='--')
    for i in outlier_indices:
        plt.plot(t[i], data[i], color='magenta', marker='*', linestyle='None')
    plt.show()

def histogram_plot(data):
    '''
    Plot a histogram with the mean, 
    upper and lower thresholds (3x standard deviation)
    and the outliers.
    '''
    plt.hist(data, bins=20, edgecolor='black')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.show()
    
    
    
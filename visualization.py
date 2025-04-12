import matplotlib.pyplot as plt

def plot_histogram(df, column):
    plt.hist(df[column], bins=20, color='blue', alpha=0.7)
    plt.title(f'Histogram of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.show()

def plot_scatter(df, x_column, y_column):
    plt.scatter(df[x_column], df[y_column], alpha=0.5)
    plt.title(f'Scatter plot of {x_column} vs {y_column}')
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.show()
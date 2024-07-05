import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.colors import LinearSegmentedColormap

def plot_bar_graph(state_vector, fig=None, ax=None):
    probabilities = [np.abs(state_vector[0])**2, np.abs(state_vector[1])**2]
    labels = ['|0>', '|1>']
    
    # Set up the seaborn style
    sns.set(style="whitegrid")
    
    if fig is None or ax is None:
        fig, ax = plt.subplots(figsize=(2, 4))
    
    ax.clear()  # Clear the axis to avoid overlapping
    
# Create a custom color map for gradients
    gradient_blue = LinearSegmentedColormap.from_list('gradient_blue', ['#00008B', '#0000ff'])  # Dark Blue to Blue
    gradient_pink = LinearSegmentedColormap.from_list('gradient_pink', ['#ff69b4', '#ff1493'])  # Pink to Dark Pink

    bars = ax.bar(labels, probabilities, color=['#00008B', '#ff69b4'])  # Use the same colors for the bars
    
    # Apply gradients to the bars
    for bar, gradient in zip(bars, [gradient_blue, gradient_pink]):
        bar.set_facecolor(gradient(0.5))
    
    # Add value labels on the bars
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, yval + 0.01, round(yval, 2), ha='center', va='bottom',color='white')
    
    ax.set_ylabel('Probability')
    ax.grid(False)  # Turn off the grid
    plt.draw()  # Update the plot

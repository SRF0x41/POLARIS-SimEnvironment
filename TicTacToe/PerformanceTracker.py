import sys
from SocketComm import SocketComm
import matplotlib
matplotlib.use('TkAgg')  # Set the interactive backend
import matplotlib.pyplot as plt
import random

def main():
    # Example data for plotting
    x = []
    y = []

    plt.ion()  # Turn on interactive mode
    fig, ax = plt.subplots()  # Create a figure and axis for the plot

    for i in range(1000):
        x.append(i)
        y.append(random.randint(1, 10))

        # Clear the previous plot
        ax.clear()
        
        # Create the plot with updated data
        ax.plot(x, y)

        # Add titles and labels
        ax.set_title('Simple Line Plot')
        ax.set_xlabel('X values')
        ax.set_ylabel('Y values')

        # Pause to update the plot (0.01 seconds delay for visualization)
        plt.pause(0.01)

    # Keep the plot open at the end
    plt.show(block=True)

if __name__ == "__main__":
    main()

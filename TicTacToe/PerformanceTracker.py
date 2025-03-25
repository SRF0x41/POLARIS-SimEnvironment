import sys
from SocketComm import SocketComm
import matplotlib
matplotlib.use('TkAgg')  # Set the interactive backend
import matplotlib.pyplot as plt
import random

import tkinter as tk


def exampleGrowingPlot():
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
    

def main():
    # Create gui
    root = tk.Tk()
    root.title("Performance Tracker GUI")
    
    # Top text
    label = tk.Label(root, text="Performance Tracker")
    label.pack()
    
    # Fetch data from polaris
    input_arr = [1,2,3,4,5]
    
    raw_output = [0,0,0,0,0]
    
    target_arr = [1,2,3,4,5]
    
    # Show input and expected arrays
    input_array_polaris = tk.Label(root, text=f"Input: {input_arr}")
    raw_output_polaris = tk.Label(root, text=f"Raw Out: {raw_output}")
    target_array_polaris = tk.Label(root, text=f"Target: {target_arr}")
    
    input_array_polaris.pack()
    raw_output_polaris.pack()
    target_array_polaris.pack()
    
    root.mainloop()

if __name__ == "__main__":
    main()

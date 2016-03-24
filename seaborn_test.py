import pdb
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

# Main Loop
def main():
    
    # Set style
    #sns.set_style("darkgrid")
    #sns.set_style("whitegrid")
    #sns.set_style("dark")
    #sns.set_style("white")
    sns.set_style("ticks")
    
    # Generate plot data
    #sinplot()
    #data = np.random.normal(size=(20, 6)) + np.arange(6) / 2
    
    #f, ax = plt.subplots()
    #sns.violinplot(data)
    #sns.despine(offset=10, trim=True);
    
    with sns.axes_style("darkgrid"):
        plt.subplot(211)
        sinplot()
    plt.subplot(212)
    sinplot(-1)
    
    # Remove spine
    #sns.despine()
    
    # Show plot
    plt.show()

def sinplot(flip=1):

    x = np.linspace(0, 14, 100)
    for i in range(1, 7):
        plt.plot(x, np.sin(x + i * .5) * (7 - i) * flip)

if __name__ == '__main__':
  main()
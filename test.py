import pdb
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

# Main Loop
def main():
    
    sns.set_style("darkgrid")
    
    sinplot()

    plt.show()

def sinplot(flip=1):

    x = np.linspace(0, 14, 100)
    plt.figure()
    for i in range(1, 7):
        plt.plot(x, np.sin(x + i * .5) * (7 - i) * flip)

if __name__ == '__main__':
  main()
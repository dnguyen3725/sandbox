import pdb
import Quandl

# Main Loop
def main():

    mydata = Quandl.get("FRED/GDP",authtoken="EDx-jp_ZK6U_13R-vLXz",returns="numpy")
    
    print mydata

if __name__ == '__main__':
  main()
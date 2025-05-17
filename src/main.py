""" TODO:
- Read data from text or .csv, same function [DONE]
- Do Apriori
- Do PCY
- Build a graph
- Set up an html homepage with my dataset already uploaded
- Anything more is just a happy extra bit. Think about all this after the website is set up and displaying graphs.
"""

import sys
import utils
import algorithms

def main():
    path = "data/grocery_dataset.txt"
    
    # Read the raw data from the file
    data = utils.readData(path)

    apriori_pairs = algorithms.apriori(data, min_support=360)
    print(apriori_pairs, "\n")

    return 0

if __name__ == '__main__':
    main()
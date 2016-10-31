import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt

def lmao():
        """
        raw_data = {'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
                    'last_name': ['Miller', 'Jacobson', ".", 'Milner', 'Cooze'],
                    'age': [42, 52, 36, 24, 73],
                    'preTestScore': [4, 24, 31, ".", "."],
                    'postTestScore': ["25,000", "94,000", 57, 62, 70]}
        """
        df = pd.read_csv('/home/jake/Documents/python_data/raptors_2015')
        print(df)

if __name__ == "__main__":
        lmao()


'''
raw_data = {'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
        'last_name': ['Miller', 'Jacobson', ".", 'Milner', 'Cooze'],
        'age': [42, 52, 36, 24, 73],
        'preTestScore': [4, 24, 31, ".", "."],
        'postTestScore': ["25,000", "94,000", 57, 62, 70]}
df = pd.DataFrame(raw_data, columns = ['first_name', 'last_name', 'age', 'preTestScore', 'postTestScore'])
df
'''

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import logging




_logger = logging.getLogger(__name__)



def test_grah():

    # Fixing random state for reproducibility
    np.random.seed(19680801)


    plt.rcdefaults()
    fig, ax = plt.subplots()

    # Example data
    people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')

    y_pos = np.arange(len(people))

    print(y_pos)
    performance = 3 + 10 * np.random.rand(len(people))
    error = np.random.rand(len(people))

    ax.barh(y_pos, performance, xerr=error, align='center')
    ax.set_yticks(y_pos, labels=people)
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel('Performance')
    ax.set_title('How fast do you want to go today?')


if __name__ == '__main__':
    test_grah()



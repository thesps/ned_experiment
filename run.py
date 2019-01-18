import DAQ
import matplotlib.pyplot as plt

def run_example():
    '''Example function of how to use the run(trigger_settings) found in DAQ.py
    '''
    data = DAQ.run({'energy_thresh': 10})
    #print DAQ.run({'occupancy_thresh': 10})

    plot_data(data)


def plot_data(data):
    '''Makes a 2d histo of the data'''
    plt.hist2d(data['occupancies'], data['energies'], 
               range = [[0, 20], [0, 10]], 
               bins = [20, 50], 
               cmin = 0.1)
    plt.xlabel('Channel Occupancy')
    plt.ylabel('Energy (MeV)')
    plt.show()


if __name__ == "__main__":
    run_example()

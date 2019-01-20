import DAQ
import numpy as np
import matplotlib.pyplot as plt

def run_example():
    '''Example function of how to use the run(trigger_settings) found in DAQ.py
    '''
    data = DAQ.run({'energy_thresh': 500})
    # data = DAQ.run({'occupancy_thresh': 10}, prescale = 10)

    # plot_data(data)


def plot_data(data):
    '''Makes a 2d histo of the raw data'''
    plt.hist2d(data['energies'], data['occupancies'], 
               range = [[0, 3000], [0, 20]], 
               bins = [50, 20], 
               cmin = 0.1)

    plt.xlabel('Energy (ADC). 100 ADC ~ 1 MeV')
    plt.ylabel('Channel Occupancy')
    plt.show()


def scan_trigger(trigger_variable, prescale):
    '''Scans over one of the specified trigger varaibles, and returns 
    a dict of results useful for analysis. The default range for each
    trigger should be suitable for most things.
    '''

    nsteps = 20
    scan_range = {'energy_thresh': [50, 700],
                  'occupancy_thresh': [2, 22]}

    steps = np.linspace(scan_range[trigger_variable][0],
                        scan_range[trigger_variable][1], 
                        nsteps, 
                        endpoint = False) # v handy tip.
    
    results = {'fprs': [], 
               'tprs': [], 
               'scan_steps': steps, 
               'dtime_fracs': [],
               'storage_space_bytes': []}

    for step in steps:
        data = DAQ.run({trigger_variable: step}, prescale)

        results['tprs'].append(data['tpr'])
        results['fprs'].append(data['fpr'])
        results['dtime_fracs'].append(data['deadtime_fraction'])
        results['storage_space_bytes'].append(data['storage_space_bytes'])

    return results


if __name__ == "__main__":
    scan_trigger('energy_thresh', 1)
    run_example()

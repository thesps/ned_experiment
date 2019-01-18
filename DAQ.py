import doNotRead

def run(trigger_settings):
    doNotRead.print_splash()
    ''' Calls doNotRead.generate(trigger_settings). trigger_settings should
    be a dictionary with one entry that corresponds to the trigger threshold, e.g:

    trigger_settings = {'energy_thresh': 5'}, or
    trigger_settings = {'occupancy_thresh': 10}. 

    The run duration is fixed already at a suitably high value.
    The function will return a dictionary with the following entries:
    - 'energies': np.array
    - 'occupancy': np.array
    - 'N': total number of triggers
    '''
    
    return doNotRead.generate(trigger_settings)

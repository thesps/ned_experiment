import doNotRead

def run(trigger_settings, prescale = 1):
    doNotRead.print_splash()
    ''' Calls doNotRead.generate(trigger_settings). trigger_settings should
    be a dictionary with one entry that corresponds to the trigger threshold, e.g:

    trigger_settings = {'energy_thresh': 200'}, or
    trigger_settings = {'occupancy_thresh': 10}. 

    (Recall energy measurements are in ADC, where 100 ADC is around 1 MeV).

    prescale should be an integer, and the trigger rate will be scaled down by that 
    factor.

    The run duration is fixed already at a suitably high value.
    The function will return a dictionary with the following entries:
    - 'energies': np.array
    - 'occupancy': np.array
    - 'N': total number of triggers
    '''
    
    data = doNotRead.generate(trigger_settings, float, prescale)
    
    # Print out a few useful things (documented here).
    # Total number of triggers (nb: in this convention, this does not account for 
    # any deadtime - at NED, triggers are counted but not saved if in deadtime).
    print 'nTriggers:', data['ntriggers']
    
    # Signal efficiency (between 0 and 1).
    print 'tpr (i.e signal efficiency):', data['tpr']

    # Signal efficiency (between 0 and 1).
    print 'fpr (i.e background efficiency):', data['fpr']

    # Total storage space used by run file.
    print 'Storage space (MB):', data['storage_space_bytes']/1000000.
    print 'Trigger data size (bytes):', data['event_size_bytes']

    # Deadtime measured as the fraction of triggers discarded.
    print 'Deadtime fraction:', data['deadtime_fraction']

    return data

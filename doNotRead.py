# Spoil sport!!!!! leave now.....




























































# This is your last warning...




























































import numpy as np
np.random.seed(1)

def generate(trigger_settings, en_ret_type, prescale):
    # Checks someone didn't pass two thresholds.
    ks = trigger_settings.keys()
    if 'energy_thresh' in ks and 'occupancy_thresh' in ks:
        print 'Too many thresholds passed - use one only. Exiting.'
        exit(1)
    
    if 'energy_thresh' not in ks and 'occupancy_thresh' not in ks:
        print 'Please specify a threshold (trigger_settings is empty). Exiting.'
        exit(1)
    
    print 'Running NED experiment with settings:', trigger_settings
    data = {}
    occ_type = 'int8'

    N = 1000000 // prescale
    Nb = 2*N

    s_ens = np.random.normal(loc = 500, scale = 200, size = N).astype(en_ret_type)
    s_ocs = np.random.poisson(lam = 8, size = N).astype(occ_type)

    # Introduce some correlation.
    shift = 0.01*np.square(np.square(s_ocs))
    shift = shift.astype(en_ret_type)
    s_ens += shift
    
    b_ens = np.random.exponential(scale = 800, size = Nb).astype(en_ret_type)
    b_ocs = np.random.exponential(scale = 5, size = Nb).astype(occ_type)
 
    data['energies'] = np.concatenate([s_ens, b_ens])
    data['occupancies'] = np.concatenate([s_ocs, b_ocs])

    # Shuffle along one axis.
    merged_data = np.array([data['energies'], data['occupancies']])
    
    # Apply the trigger requirements.
    if 'energy_thresh' in ks:
        merged_data = merged_data[:, merged_data[0] > trigger_settings['energy_thresh'] ]
        data['tpr'] = np.sum(s_ens > trigger_settings['energy_thresh']) / float(N)
        data['fpr'] = np.sum(b_ens > trigger_settings['energy_thresh']) / float(Nb)
    else:
        merged_data = merged_data[:, merged_data[1] > trigger_settings['occupancy_thresh'] ]
        data['tpr'] = np.sum(s_ocs > trigger_settings['occupancy_thresh']) / float(N)
        data['fpr'] = np.sum(b_ocs > trigger_settings['occupancy_thresh']) / float(Nb)
        

    np.random.shuffle(merged_data.T)

    data['energies'] = merged_data[0].astype(en_ret_type)
    data['occupancies'] = merged_data[1].astype('int8')
    data['ntriggers'] = len(data['energies'])
    data['storage_space_bytes'] = data['energies'].nbytes + data['occupancies'].nbytes
    data['event_size_bytes'] = data['energies'][0].nbytes + data['occupancies'][0].nbytes
    data['deadtime_fraction'] = 0

    storage_limit_bytes = 15e6
    if data['storage_space_bytes'] > storage_limit_bytes:
        print '\n** Warning: deadtime non-zero! **\n'
        data['deadtime_fraction'] = 1-storage_limit_bytes/float(data['storage_space_bytes'])

        Nkeep = int(storage_limit_bytes/float(data['storage_space_bytes']) * data['ntriggers'])

        data['energies'] = data['energies'][:Nkeep]
        data['occupancies'] = data['occupancies'][:Nkeep]
        data['storage_space_bytes'] = data['energies'].nbytes + data['occupancies'].nbytes
    
    return data


def print_splash():
    print '          _____                    _____                    _____      '
    print '         /\    \                  /\    \                  /\    \         '
    print '        /::\____\                /::\    \                /::\    \        '
    print '       /::::|   |               /::::\    \              /::::\    \       '
    print '      /:::::|   |              /::::::\    \            /::::::\    \      '
    print '     /::::::|   |             /:::/\:::\    \          /:::/\:::\    \     '
    print '    /:::/|::|   |            /:::/__\:::\    \        /:::/  \:::\    \    '
    print '   /:::/ |::|   |           /::::\   \:::\    \      /:::/    \:::\    \   '
    print '  /:::/  |::|   | _____    /::::::\   \:::\    \    /:::/    / \:::\    \  '
    print ' /:::/   |::|   |/\    \  /:::/\:::\   \:::\    \  /:::/    /   \:::\ ___\ '
    print '/:: /    |::|   /::\____\/:::/__\:::\   \:::\____\/:::/____/     \:::|    |'
    print '\::/    /|::|  /:::/    /\:::\   \:::\   \::/    /\:::\    \     /:::|____|'
    print ' \/____/ |::| /:::/    /  \:::\   \:::\   \/____/  \:::\    \   /:::/    / '
    print '         |::|/:::/    /    \:::\   \:::\    \       \:::\    \ /:::/    /  '
    print '         |::::::/    /      \:::\   \:::\____\       \:::\    /:::/    /   '
    print '         |:::::/    /        \:::\   \::/    /        \:::\  /:::/    /    '
    print '         |::::/    /          \:::\   \/____/          \:::\/:::/    /     '
    print '         /:::/    /            \:::\    \               \::::::/    /      '
    print '        /:::/    /              \:::\____\               \::::/    /       '
    print '        \::/    /                \::/    /                \::/____/        '
    print '         \/____/                  \/____/                  ~~              '
    print
























































# Did you think i'd make it that easy?

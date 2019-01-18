# Spoil sport!!!!! leave now.....




























































# This is your last warning...




























































import numpy as np
np.random.seed(1)

def generate(trigger_settings):
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
    N = 100000
    s_ens = np.random.normal(loc = 2, scale = 1.5, size = N)
    s_ocs = np.random.normal(loc = 10, scale = 4, size = N).astype(int)

    # Introduce some correlation.
    s_ens += 0.0001*np.square(np.square(s_ocs))
    
    b_ens = np.random.exponential(scale = 7, size = N)
    b_ocs = np.random.exponential(scale = 5, size = N)
 
    data['energies'] = np.concatenate([s_ens, b_ens])
    data['occupancies'] = np.concatenate([s_ocs, b_ocs])

    # Shuffle along one axis.
    merged_data = np.array([data['energies'], data['occupancies']])
    np.random.shuffle(merged_data.T)
    data['energies'] = merged_data[0]
    data['occupancies'] = merged_data[1]
     
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

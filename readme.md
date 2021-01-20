## Credit
This exercise was originally created by Dan Saunders, originally [here](https://bitbucket.org/dan_saunders/ned_experiment/wiki/Home).

# Optimisation of the readout system from the NED Experiment

Welcome first years! This problem sheet goes through a simplified commissioning of the NED (Non-existent Detector) experiment. There are two separate tasks, and working in pairs or small groups, each team should tackle each part asynchronously ;). Once you've decided the order of tasks, read through the background of the experiment, and keep track of your solutions in a set of google slides or a jupyter-notebook.

## Background
The NED experiment has a very basic detector that's similar to a dark matter experiment: a tank of liquid scintillator that is coupled to a relatively small number of read-out PMT channels (100). The ADC range of the channels is 14 bits. The experiment currently aims to measure the energy spectrum of a newly discovered radioactive source found in the Nevada dessert. For reasons unknown to man-kind (but perhaps known to alien-kind), the signal rate of this source is quite small, and so the data also contains a large intrinsic background (e.g natural radioactivity and cosmic rays). The signal peaks around 5 MeV (corresponding to around 1k ADC), whereas the background is found at lower energies. Maximizing the signal efficiency during data taking is critical. 

Being a HEP experiment, the readout system was built on a shoe string budget, and is formed of mostly CMS reject components  - unfortunately, as a result, the readout system can **only** returns two variables for each trigger: the total energy deposit (in units of ADC, summed over all channels), and the detector occupancy (i.e number of channels above zero suppression). The trigger of the experiment allows for one threshold condition that can be placed on either variable (i.e energy or occupancy). The rate of signal and background is too high to trigger on all events, and both of these variables offer some level of discrimination between signal and background, but its not yet clear which variable should be used. 

The dominant source of deadtime at NED is due to a bottleneck in data-rate, which increases above zero from around 15 MB per run and higher. Triggers can be received, and counted, but they're corresponding data will be discarded to reduce the data-rate (not necessarily in an unbiased way w.r.t the Physics). 

### Software

The DAQ software and run control software is in this repository. You can run it on the public Binder service here:

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/thesps/ned_experiment/HEAD)

Remember, code you write on this service may not be saved, you should download any notebooks you write locally.

There is also a CERN hosted Binder service, available if you have a CERN computing account. There you can save work to `/eos` or `/afs`.

[![badge](https://img.shields.io/badge/launch-CERN%20binder-E66581.svg?logo=data:image/png;base64,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)](https://binder.cern.ch/v2/gh/thesps/ned_experiment/master)


Alternatively, you can clone from this repository using git:

```git clone https://github.com/thesps/ned_experiment.git```

DAQ.py contains code to retrieve data from the experiment (using a simulation), and documents the returned data. Run.py contains a set of functions that show examples of taking runs, and some useful monitoring plots. You should have a quick read through both files. A third file, named doNotRead.py, should not be read, unless you are a spoil sport. 

Before attempting the following questions, first try to run the example run function (```run_example()```). You may also find the function ```scan_trigger()``` useful for both of the following tasks. 

## Part 1 - Deciding trigger variables

In order to decide on which variable to use in the trigger, start by considering the following:

* Based on how the data is distributed in the two variables, which do you expect to offer better discrimination?
* Quantify which variable offers better discrimination at the trigger level. What plots are needed to demonstrate this? Demonstrate this. 
* Are there any physics motivations to select one variable over the other?
* Using your results, propose a set of trigger settings that give a stable data rate of 5 MB per run. Do you need any more information?

*Nb: to avoid bias, you should always use settings that ensure that the dead-time fraction is kept at zero for this part of the exercise.* 

## Part 2 - Deadtime characterisation

It's important to know the level of deadtime for the possible different trigger conditions that can be applied. Start by considering the following:

* What are the consequences for physics measurements for a high deadtime? 
* Map the deadtime as a function of both trigger variables.

Since the experiment was put together quickly, the DAQ is not perfectly optimised. 

* Read through DAQ.py - are there any optimisations that can be made to decrease the deadtime? 
* Do your above results change given these optimisations?

# Solutions

The solutions can be found in a jupyter-notebook in this repository. A typical set of solutions are about **30 lines** of code in total (mostly just plotting). You should only ever have to change a couple of lines in files cloned in this repository.

# Optimisation of the readout system from the NED Experiment

Welcome first years! This problem sheet goes through a simplified commissioning of the NED (Non-existent Detector) experiment. There are two separate tasks, and working in pairs or small groups, each team should tackle each part asynchronously ;). Once you've decided the order of tasks, read through the background of the experiment, and keep track of your solutions in a set of google slides or a jupyter-notebook.

## Background
The NED experiment has a very basic detector that's similar to a dark matter experiment: a tank of liquid scintillator that is coupled to a relatively small number of read-out PMT channels (100). The ADC range of the channels is 14 bits. The experiment currently aims to measure the energy spectrum of a newly discovered radioactive source found in the Nevada dessert. For reasons unknown to man-kind (but perhaps known to alien-kind), the signal rate of this source is quite small, and so the data also contains a large intrinsic background (e.g natural radioactivity and cosmic rays). The signal peaks around 5 MeV (corresponding to around 1k ADC), whereas the background is found at lower energies. Maximizing the signal efficiency during data taking is critical. 

Being a HEP experiment, the readout system was built on a shoe string budget, and is formed of mostly CMS reject components  - unfortunately, as a result, the readout system can **only** returns two variables for each trigger: the total energy deposit (in units of ADC, summed over all channels), and the detector occupancy (i.e number of channels above zero suppression). The trigger of the experiment allows for one threshold condition that can be placed on either variable (i.e energy or occupancy). The rate of signal and background is too high to trigger on all events, and both of these variables offer some level of discrimination between signal and background, but its not yet clear which variable should be used. 

The dominant source of deadtime at NED is due to a bottleneck in data-rate, which increases above zero from around 15 MB per run and higher. Triggers can be received, and counted, but they're corresponding data will be discarded to reduce data-rate (not necessarily in an unbiased way w.r.t the Physics). 

### Software

The DAQ software and run control software is in this repository, and can be cloned publicly using git https:

```git clone https://dan_saunders@bitbucket.org/dan_saunders/ned_experiment.git```

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
# Optimisation of the readout system from the NED Experiment

Welcome first years! This problem sheet goes through a simplified commissioning of the NED (Non-existent Detector) experiment. There are two separate tasks, and working in pairs or small groups, each team should tackle each part asynchronously ;). Once you've decided the order of tasks, read through the background of the experiment, and keep track of your solutions in a set of google slides.

## Background
The NED experiment has a very basic detector that's similar to a dark matter experiment: a tank of liquid scintillator that is coupled to a relatively small number of read-out PMT channels (100). The ADC range of the channels is 14 bits. The experiment currently aims to measure the energy spectrum of a newly discovered radioactive source found in the Nevada dessert. For reasons unknown to man-kind (but perhaps known to alien-kind), the signal rate of this source is quite small, and so the data also contains a large intrinsic background (e.g natural radioactivity and cosmic rays). The signal peaks around 5 MeV (corresponding to around 1k ADC), whereas the background is found at lower energies. Maximizing the signal efficiency during data taking is critical. 

Being a HEP experiment, the readout system was built on a shoe string budget, and is formed of mostly CMS reject components  - unfortunately, as a result, the readout system can **only** returns two variables for each trigger: the total energy deposit (in units of ADC, summed over all channels), and the detector occupancy (i.e number of channels above zero suppression).

### Software

The DAQ software and run control software is in this repository, and can be cloned publicly using git https:

```git clone https://dan_saunders@bitbucket.org/dan_saunders/ned_experiment.git```

DAQ.py contains code to retrieve data from the experiment (using a simulation). Run.py contains a set of functions that show examples of taking runs, and some useful monitoring plots. You should have a quick read through both files. A third file, named doNotRead.py, should not be read, unless you are a spoil sport. 

Before attempting the following questions, first try to run the example run function (```run_example()```). You may also find the function ```scan_trigger()``` useful for both of the following tasks. 

## Part 1 - Deciding trigger variables

The trigger of the experiment allows for one threshold condition that can be placed on either condition (i.e energy or occupancy). The rate of signal and background is too high to trigger on all events, and both of these variables offer some level of discrimination between signal and background. In order to decide on which variable to use, start by considering the following:

* Which variable offers better discrimination at the trigger level? 
    * What plots are needed to demonstrate this? 
* Are there any physics motivations to select one variable over the other?

*Nb: to avoid bias, you should always use settings that ensure that the dead-time fraction is kept at zero for this part of the exercise.* 


## Part 2 - Deadtime optimisation
# Optimisation of the readout system from the NED Experiment

Welcome first years! This problem sheet goes through a simplified commissioning of the NED (Non-existent Detector) experiment. There are three separate tasks, and working in pairs or small groups, each team should tackle each part asynchronously ;). Once you've decided the order of tasks, read through the background of the experiment, and keep track of your solutions in a set of google slides.

## Background
The NED experiment has a very basic detector that's similar to a dark matter experiment: a tank of liquid scintillator that is coupled to a relatively small number of read-out PMT channels (100). The ADC range of the channels is 14 bits. The experiment currently aims to measure the energy spectrum of a newly discovered radioactive source found in the Nevada dessert. For reasons unknown to man-kind (but perhaps known to alien-kind), the signal rate of this source is quite small, and so the data also contains a large intrinsic background (e.g natural radioactivity and cosmic rays). The signal peaks around 5 MeV, whereas the background is found at lower energies. 
 Being a HEP experiment, the readout system was built on a shoe string budget, and is formed of mostly CMS reject components  - unfortunately, as a result, the readout system can **only** returns two variables for each trigger: the total energy deposit, and the detector occupancy (i.e number of channels above zero suppression).

### Software

The DAQ software and run control software is in this repository, and can be cloned publicly using git https:

git clone https://dan_saunders@bitbucket.org/dan_saunders/ned_experiment.git

DAQ.py contains code to retrieve data from the experiment (using a simulation). Run.py contains a set of functions that show examples of taking runs, and some useful monitoring plots. You should have a quick read through both files. A third file, named doNotRead.py, should not be read, unless you are a spoil sport. 

Before attempting the following questions, first try to run the example run function ('''run_example'''). 

## Part 1 - Deciding trigger variables
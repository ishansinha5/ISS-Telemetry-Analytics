# The Original CMSE 201 Project

This directory archives the original Jupyter Notebook and raw assets from my final project for Dr. Tyler Wheeler's CMSE 201 course at Michigan State University. It serves as the foundational blueprint for the advanced modular pipeline built in the rest of this repository.

## The Original Research Question
The International Space Station (ISS) is often visualized as a global traveler, but its path is strictly governed by orbital mechanics. Specifically, the ISS maintains an orbital inclination of **51.6 degrees**. This fundamental constraint implies that the station can never physically fly directly over polar regions (latitudes greater than 51.6° N or S).

The original project sought to answer: *"How does the ISS's specific 51.6-degree orbital inclination create a quantifiable 'bias' in its ground-track coverage?"*

## Methodology & The "Dwell Time" Phenomenon
Using basic Pandas data manipulation, the original notebook empirically demonstrated two main concepts:
1. **The Polar Gap:** Proving via coordinate tracking that the ISS never exceeds the 51.6° latitudinal boundaries.
2. **Orbital Dwell Time:** Visualizing the mathematical reality that a sine-wave orbit mapped onto a rotating sphere forces the station to "dwell" at the northern and southern maximums. 

By filtering the raw telemetry dataset, the original notebook calculated that the ISS is approximately **4.70x more likely** to be found hovering over its inclination limits than crossing the equator. 

While the code in this legacy folder is rough and relies heavily on manual, single-file Jupyter execution, the spatial tracking concepts established here were the direct inspiration for the global band trackers and geopolitical engines driving the modernized application today.
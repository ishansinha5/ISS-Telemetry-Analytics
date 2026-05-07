# The Engine Room: Data Pipelines & Math

This directory contains the core logic of the ISS Telemetry project. By breaking the analysis down into isolated, domain-specific modules, the codebase remains clean, easy to debug, and highly repurposable. 

Here is a technical breakdown of the methodologies used in the custom pipelines.

## `astrodynamics.py`: Solar Illumination Approximation
Calculating true solar position and eclipse cycles requires complex astrodynamics libraries. I wanted to build a lightweight heuristic using pure data engineering.
* **The Math:** The Earth rotates 360 degrees every 24 hours, meaning local time shifts by exactly 1 hour for every 15 degrees of longitude. 
* **The Logic:** The script parses the UTC timestamp, extracts the decimal hour, and calculates a `local_solar_hour` by dividing the longitude by 15.0. If the approximate local time falls between 6:00 AM and 6:00 PM, the ping is classified as "Daylight."

## `orbital_physics.py`: Proof of Orbital Decay
The ISS does not operate in a frictionless vacuum; it resides in Low Earth Orbit (LEO) and is constantly subjected to atmospheric drag, which slowly degrades its altitude.
* **The Logic:** This module cleans the telemetry feed, drops missing values, and runs a Pearson Correlation between `altitude_km` and `speed_kmph`.
* **The Finding:** The engine consistently returns a negative correlation. This perfectly aligns with the laws of orbital mechanics: as atmospheric drag decreases the station's altitude (orbital decay), its orbital velocity inherently increases. 

## `anomaly_detection.py`: Re-boost Identification
Because of the orbital decay proven above, the ISS must periodically fire thrusters to "re-boost" its altitude. 
* **The Logic:** Instead of looking for raw maximums, this script calculates a 15-period rolling average of the station's altitude. It then measures the absolute variance of the current altitude against that rolling average.
* **The Filter:** By setting a dynamic threshold at the 99th percentile (`df.quantile(0.99)`), the script isolates the top 1% of extreme, sudden altitude shifts, successfully pinpointing physical re-boost anomalies or severe atmospheric drag spikes.

## `signal_diagnostics.py`: Telemetry Feed Health
In autonomous and remote systems, tracking packet loss and line-of-sight blind spots is critical for system health. 
* **The Logic:** This script uses Pandas' `.diff()` function to calculate the exact time delta (in seconds) between every sequential data log. It plots these intervals against a calculated mean to visualize the stability of the transmission feed.

## `geopolitics.py` & `telemetry_utils.py`
These scripts handle the spatial tracking. `telemetry_utils.py` utilizes a dictionary-driven bounding-box system to map horizontal (latitudinal) and vertical (longitudinal) global bands, allowing the engine to be easily scaled to track any number of customized global regions simultaneously.
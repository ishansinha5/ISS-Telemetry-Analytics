# ISS Telemetry Analytics: Mapping Orbital Bias & Physics

![Orbital Track](./assets/legacy_orbital_track.png)

This project is a massive architectural evolution of a final project I originally completed for CMSE 201 at Michigan State University. In that original project, I used basic Pandas to plot International Space Station (ISS) coordinates to prove the existence of the "polar gap" and map orbital inclination bias. 

I wanted to take those early concepts and upgrade them into a proper, production-ready data engineering pipeline. This program ingests raw ISS telemetry data (timestamps, coordinates, altitude, velocity) and runs it through a series of modular, automated Python engines to extract deep geopolitical, astrodynamical, and physical insights.

## The Tech Stack & Architecture

Moving from a single, messy Jupyter Notebook to a modular Python pipeline required a shift in architecture. Here is the logic behind the codebase:

* **Separation of Concerns:** Jupyter Notebooks suffer from "hidden state" problems and aren't ideal for heavy data crunching. I migrated all mathematical logic, aggregations, and plotting functions into isolated `.py` files inside the `/scripts` directory. 
* **The Conductor Dashboard:** The `ISS_Advanced_Analysis.ipynb` notebook acts purely as a presentation layer. It imports the engines, feeds them the CSV data, and displays the generated assets. 
* **Automated Asset Generation:** The pipeline is designed so that the Python scripts automatically handle the generation and saving of high-resolution `matplotlib` PNGs directly to the `/assets` folder, keeping the user interface entirely hands-off.

## The Core Finding: The 51.6° Limit
The original question of this project was to identify "Orbital Bias." The ISS does not travel randomly; it is locked into an orbital inclination of exactly **51.6 degrees**. 

Because of the geometry of this orbit, the station physically cannot fly over the poles. Furthermore, the physics of a sine-wave orbit mapped onto a rotating sphere means the station spends significantly more time "dwelling" at the absolute maximums of its inclination (51.6° N and 51.6° S) than it does crossing the equator. 

## How to Use & Repurpose This Repo

You can clone this repository and easily add your own global cities to the tracking engine.

1. **Clone the repository:** `git clone https://github.com/ishansinha5/ISS-Telemetry-Analytics.git`
2. **Install Dependencies:** `pip install pandas matplotlib numpy`
3. **Add your City:** Open `scripts/telemetry_utils.py`, find the `locations` dictionary in the `analyze_global_bands` function, and add your city's latitude and longitude bounds.
4. **Run the Dashboard:** Open `ISS_Advanced_Analysis.ipynb` and run the cells sequentially to regenerate the data visualizations for your targeted regions.
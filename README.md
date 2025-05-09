# WBGT Visualization for the Imperial Valley

A dynamic geospatial visualization of Wet Bulb Globe Temperature (WBGT) patterns in California’s Imperial Valley, developed as part of my work with the [Climate Informatics Laboratory (SCIL)](https://scil.sdsu.edu/) at San Diego State University. This project is my contribution to the [Rural Heat Islands (RHI) Data and Alarm System](https://4dvdrhi.sdsu.edu/), and it will be integrated in a future update.

---

## Overview

This application visualizes WBGT data on an interactive map using Deck.gl and Mapbox. The current version renders daily noon-time temperature contours over the Imperial Valley region from November 2 to November 25, 2024.

---

## Current Features

- Dynamic rendering of NetCDF-derived data layers
- Interactive map, with a layer displaying WBGT contours
- Date selection using a simple frontend UI
---

## Tech Stack

- **Frontend:** React.js, Deck.gl, Mapbox
- **Backend:** Python, FastAPI
- **Data Processing:** NetCDF4, Matplotlib
- **Data Source:** WBGT datasets provided by [Professor Fernando De Sales, SDSU Geography](https://geography.sdsu.edu/people/bios/desales)

In addition, work and documentation for this project were created using assistance from AI tools (ChatGPT). This assistance was mainly for the purpose of troubleshooting and ensuring adherence to best practices.

---
## Demo

![WBGT contour visualization for 12pm PST on November 2, 2024](https://github.com/michael-a7/RHI-Contour-Maps/blob/master/Layer-Image-Demo.png?raw=true)

**WBGT contour visualization for 12pm PST on November 2, 2024**

## How It Works

1. **Data Extraction:** Python scripts process NetCDF files to extract WBGT values at noon for selected dates.
2. **Visualization:** Contour plots are generated using Matplotlib.
3. **API Upload:** The processed images are served via a FastAPI backend.
4. **Map Integration:** The React frontend overlays the contours as a Deck.gl layer on a Mapbox map.

---

## Future Work

- Integrate additional datasets across broader date ranges
- Add interactive UI components
- Deploy live version with public access
---

## Acknowledgments

- Professor Fernando De Sales, SDSU Department of Geography  
- Climate Informatics Laboratory (SCIL), San Diego State University

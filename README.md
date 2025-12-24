# 🛰️ Satellite Service Finder (Pro Edition)

![License](https://img.shields.io/github/license/username/repo)
![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![Django](https://img.shields.io/badge/django-4.2+-green.svg)
![PostGIS](https://img.shields.io/badge/PostGIS-Spatial--DB-blue)
![OSM](https://img.shields.io/badge/OpenStreetMap-Data-orange)

A high-performance **Geographic Information System (GIS)** built with **GeoDjango** and **PostGIS**. This application leverages massive datasets from **OpenStreetMap (OSM)** to help users locate critical services (Hospitals, Schools, Police Stations) within a specific radius, visualized on a high-resolution hybrid satellite map.

---

## 🌟 Key Features

- **Massive Data Integration:** Processes and queries millions of Points of Interest (POIs) directly from OSM PBF files.
- **Spatial Query Engine:** Real-time search within a 5km radius using PostGIS spatial indexing.
- **Hybrid Satellite View:** High-fidelity imagery from Esri World Imagery combined with CartoDB transparent labels for street-level context.
- **Interactive Routing:** Integrated **Leaflet Routing Machine** for instant turn-by-turn navigation from the user's location to the selected service.
- **Dynamic Sidebar:** A real-time updated list of services sorted by physical distance.

---

## 🛠️ Technical Architecture

The system follows a modern GIS pipeline, moving data from raw OpenStreetMap formats into a queryable spatial database.



| Layer | Technology |
| :--- | :--- |
| **Data Source** | OpenStreetMap (OSM) - `.pbf` format |
| **ETL Tool** | `osm2pgsql` (OpenStreetMap to PostGIS converter) |
| **Spatial Database** | PostgreSQL + PostGIS Extension |
| **Backend** | Python / Django / GeoDjango / DRF |
| **Frontend** | Leaflet.js / Leaflet-Routing-Machine |
| **Map Tiles** | Esri (Satellite) & CartoDB (Labels) |

---

## ⚙️ Data Pipeline & ETL Process

This project distinguishes itself by using professional-grade data handling. Instead of manual data entry, we sync directly with the global OSM database.

### 1. Data Acquisition
Download the desired region's `.osm.pbf` file from providers like [Geofabrik](https://download.geofabrik.de/).

### 2. Importing with `osm2pgsql`
The data is converted into spatial SQL tables using the `osm2pgsql` tool. This creates optimized tables (`planet_osm_point`, `planet_osm_line`, etc.) with built-in **GIST Spatial Indexes**.

```bash
osm2pgsql -d your_db_name -U your_postgres_user -H localhost --slim --hstore map_data.osm.pbf

# NASA Sky-Watcher 🌌

## Project Overview
**NASA Sky-Watcher** is a Python-based utility that bridges the gap between raw scientific telemetry and amateur astronomy. Driven by a personal passion for **sky-gazing and nature**, I built this tool to automate the retrieval of daily astronomical insights and track celestial objects in real-time.

## Key Features
* **APOD Automation:** Interfaces with **NASA’s Planetary APIs** to fetch the "Astronomy Picture of the Day" metadata and high-definition imagery.
* **ISS Live Telemetry:** Tracks the **International Space Station** coordinates in real-time by parsing live JSON data feeds.
* **Robust Networking:** Implements professional error-handling for REST API requests and network latency.

## Tech Stack
* **Language:** Python 3.x
* **Data Format:** JSON (JavaScript Object Notation)
* **Networking:** RESTful APIs
* **Libraries:** `requests`, `json`, `datetime`



## Technical Challenges & Logic
1.  **JSON Parsing:** Successfully handled complex, nested JSON objects from NASA’s servers to extract relevant metadata (HD URLs, scientific explanations).
2.  **API Integration:** Managed secure communication with external endpoints using API keys and request headers.
3.  **Dynamic Data:** Implemented logic to handle live satellite telemetry which changes every second, ensuring the user receives accurate positioning.



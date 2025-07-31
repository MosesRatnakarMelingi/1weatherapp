# Simple AI Weather Bot

## Overview

This is a simple conversational AI weather bot built using the LangChain framework and powered by the Groq API for the Large Language Model (LLM) and OpenWeatherMap API for fetching real-time weather data. Users can ask the bot about the current weather conditions in any city around the world.

## Features

* Fetches current temperature (Celsius)
* Provides "feels like" temperature
* Gives a brief weather description (e.g., "Overcast clouds", "Clear sky")
* Reports humidity percentage
* Shows wind speed (m/s)
* Supports conversational input for city names.

## Technologies Used

* **Python 3.x**
* **LangChain:** Framework for building LLM applications
    * `langchain-groq`: For integrating Groq LLM
    * `langchain-community`: For utility tools
    * `langchain-core`
* **Groq API:** Provides fast and efficient LLMs (e.g., Llama3)
* **OpenWeatherMap API:** Source for weather data
* **python-dotenv:** For managing API keys securely
* **Git & GitHub Codespaces:** Version control and cloud development environment

## Setup and Installation

Follow these steps to set up and run the weather bot in your environment (e.g., GitHub Codespaces or local machine).

### Prerequisites

* Python 3.10+ installed
* An API Key from [OpenWeatherMap](https://openweathermap.org/api)
* An API Key from [Groq](https://console.groq.com/keys)

### Steps

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/MosesRatnakarMelingi/1weatherapp.git](https://github.com/MosesRatnakarMelingi/1weatherapp.git)
    cd 1weatherapp
    ```

2.  **Create and activate a Python virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *Note: You might see some dependency warnings related to `langchain-community` and Pydantic versions. These typically do not affect the bot's core functionality for this project.*

4.  **Create a `.env` file:**
    In the root directory of your project (where `weather_bot_agent.py` is), create a file named `.env` and add your API keys:
    ```
    OPENWEATHER_API_KEY=your_open_weather_map_api_key_here
    GROQ_API_KEY=your_groq_api_key_here
    ```
    **Replace `your_open_weather_map_api_key_here` and `your_groq_api_key_here` with your actual keys from OpenWeatherMap and Groq, respectively. Do NOT push your actual keys to GitHub.** (The `.gitignore` file should prevent `.env` from being pushed).

## How to Run

After setup, run the bot from your terminal:

```bash
python weather_bot_agent.py


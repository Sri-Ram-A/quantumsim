# Quantum Circuit Simulation Application

This application is a quantum circuit simulator built using Python's Tkinter library. It allows users to create and manipulate quantum circuits using various quantum gates and visualize the results.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Images](#images)
- [Requirements](#requirements)
- [License](#license)

## Features
- Create quantum circuits using various gates (X, Y, Z, H, Rx, Ry, Rz, etc.)
- Input angles for rotation gates
- Visualize the quantum state on a Bloch sphere
- Generate a 3D bar graph of probabilities
- Help menu with descriptions of quantum gates

## Installation

1. Clone the repository or download the source code.
2. Navigate to the `gui` directory:
   ```bash
   cd path\to\your\project\gui
   ```
3. Install the required packages using pip:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Ensure you are in the `gui` directory.
2. Run the application:
   ```bash
   python app.py
   ```
3. Use the buttons to create quantum circuits and input angles. Click on the help button for descriptions of each gate.

## Images

The following images are included in the `images` folder to help illustrate the application:

1. **Intro Image**: ![Intro Image](images/intro.png)
   - This image provides an overview of the application.

2. **Working Image**: ![Working Image](images/working.png)
   - This image shows the application in action, demonstrating how to create a quantum circuit.

3. **Help Image**: ![Help Image](images/help.png)
   - This image displays the help menu with descriptions of the quantum gates.

## Requirements

Make sure you have the following packages installed:
- `numpy`
- `matplotlib`
- `Pillow`
- `customtkinter`

You can find the complete list of requirements in the `requirements.txt` file.


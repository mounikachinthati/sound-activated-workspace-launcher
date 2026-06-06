# Sound Activated Workspace Launcher

A Python-based automation tool that listens for microphone input and launches predefined applications, websites, or workspace tasks when a double-sound pattern is detected.

## Features

* Real-time sound detection using the microphone
* Double-sound trigger mechanism
* Automatic application and website launching
* Customizable sound sensitivity threshold
* Simple and lightweight Python implementation

## Prerequisites

On macOS, install PortAudio before installing the Python packages:

```bash
brew install portaudio
```

## Installation

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Start the listener:

```bash
python app.py
```

Wait for the terminal to display:

```text
Listening for double sounds...
```

When two loud sounds are detected within the configured time interval, the predefined tasks will execute automatically.

**Note:** After activation, the listener pauses temporarily to prevent audio feedback from triggering additional actions. To stop the program completely, press `Ctrl+C`.

## Customizing Tasks

Open `app.py` and locate the following section:

```python
if sound_count == 2:
```

Add your own automation tasks inside this block.

Examples:

```python
# Open an application
os.startfile(r"C:\Program Files\Google\Chrome\Application\chrome.exe")

# Open a website
webbrowser.open("https://github.com")

# Open a project folder
os.startfile(r"C:\Users\YourName\Documents\Projects")
```

## Technologies Used

* Python
* PyAudio
* NumPy

## Use Cases

* Workspace automation
* Quick application launching
* Personal productivity enhancement
* Hands-free computer interaction

# AI Music Generator 🎶

A classy web application that generates music using an AI model. Built with Flask, Keras, and music21, this app allows users to generate, preview, and download AI-composed MIDI music.

## Features
- Generate unique music using a trained AI model
- Preview generated music directly in the browser
- Download MIDI files for personal use
- Modern, elegant UI design

## Setup Instructions

1. **Clone the repository** (if not already):
   ```bash
   git clone <repo-url>
   cd music-flask-app
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   python app.py
   ```
   The app will be available at `http://127.0.0.1:5000/`.

## Usage
- Open the app in your browser.
- Click the **Generate Music** button.
- Preview the generated MIDI or download it for later use.

## Project Structure
```
music-flask-app/
├── app.py
├── requirements.txt
├── music_generator_model.h5
├── note_encoder.pkl
├── static/
│   └── generated_music.mid
├── templates/
│   └── index.html
└── README.md
```

## Credits
- Built with [Flask](https://flask.palletsprojects.com/), [Keras](https://keras.io/), and [music21](https://web.mit.edu/music21/)
- UI inspired by modern web design best practices

---
Feel free to contribute or suggest improvements! 
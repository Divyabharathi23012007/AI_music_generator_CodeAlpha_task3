
from flask import Flask, render_template, send_from_directory, request
import numpy as np
import pickle
from tensorflow.keras.models import load_model
from music21 import note, chord, stream
import os

app = Flask(__name__)

# Load model & encoder
model = load_model("music_generator_model.h5")
with open("note_encoder.pkl", "rb") as f:
    encoder = pickle.load(f)

note_to_int = {n: i for i, n in enumerate(encoder.classes_)}
int_to_note = {i: n for i, n in enumerate(encoder.classes_)}

def generate_notes(seed, length=50):
    pattern = seed.copy()
    output = []
    for _ in range(length):
        x = np.reshape(pattern, (1, len(pattern), 1)) / float(len(encoder.classes_))
        prediction = model.predict(x, verbose=0)
        idx = np.argmax(prediction)
        output.append(int_to_note[idx])
        pattern.append(idx)
        pattern = pattern[1:]
    return output

def create_midi(notes):
    output_notes = []
    for pattern in notes:
        if '.' in pattern:
            chord_notes = [note.Note(int(n)) for n in pattern.split('.')]
            output_notes.append(note.Chord(chord_notes))
        else:
            output_notes.append(note.Note(pattern))
    midi_stream = stream.Stream(output_notes)
    output_path = os.path.join("static", "generated_music.mid")
    midi_stream.write('midi', fp=output_path)
    return output_path

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        seed = np.random.randint(0, len(encoder.classes_), 10).tolist()
        notes = generate_notes(seed)
        create_midi(notes)
        return render_template('index.html', music_generated=True)
    return render_template('index.html', music_generated=False)

if __name__ == '__main__':
    os.makedirs("static", exist_ok=True)
    app.run(debug=True)

import tkinter as tk
import joblib
from tkinter import messagebox

model = joblib.load("password_prediction_model.joblib")

def process_input():
    input_text = entry.get()
    # Here you can perform any processing on the input text
    output_text =model.predict(input_text)
    messagebox.showinfo("Output", output_text)

# Create the main application window
app = tk.Tk()
app.title("Text Processor")

# Create a label and entry for input
label = tk.Label(app, text="Enter text:")
label.pack()
entry = tk.Entry(app)
entry.pack()

# Create a button to trigger processing
process_button = tk.Button(app, text="Process", command=process_input)
process_button.pack()

# Run the application
app.mainloop()

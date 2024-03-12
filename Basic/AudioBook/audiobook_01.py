
import pyttsx3

import PyPDF2
from gtts import gTTS

# Open the PDF file using PdfReader
pdf_reader = PyPDF2.PdfReader('./novel_1984.pdf')

# Initialize the text-to-speech engine
speaker = pyttsx3.init()

# Iterate through each page in the PDF
for pagenumber in range(len(pdf_reader.pages)):
    # Extract text from the page
    text = pdf_reader.pages[pagenumber].extract_text()

    # Speak the text
    speaker.say(text)
    speaker.runAndWait()

    # Save the text to an audio file using gTTS
    tts = gTTS(text, lang='en')
    tts.save(f'audio_page_{pagenumber + 1}.mp3')

# Stop the text-to-speech engine
speaker.stop()

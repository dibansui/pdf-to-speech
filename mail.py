from gtts import gTTS
from PyPDF2 import PdfReader

# Open the PDF file
pdf_File = open('name.pdf', 'rb')

# Use PdfReader (new syntax for PyPDF2 3.x)
pdf_Reader = PdfReader(pdf_File)
count = len(pdf_Reader.pages)  # Updated way to count pages
textList = []

# Extract text from each page
for i in range(count):
    try:
        page = pdf_Reader.pages[i]
        textList.append(page.extract_text())  # New method name
    except:
        pass

# Join all text into a single string
textString = " ".join(textList)

print(textString)

# Set language and generate speech
language = 'en'
myAudio = gTTS(text=textString, lang=language, slow=False)

# Save audio file
myAudio.save("Audio.mp3")

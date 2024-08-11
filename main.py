import pyttsx3
import PyPDF2

# Initialize the speech engine
speaker = pyttsx3.init()

# Set the voice and rate
voices = speaker.getProperty('voices')
speaker.setProperty('voice', voices[1].id)  # Set to the second or female voice
speaker.setProperty('rate', 130)  # Set speech rate to 140

# Get user input
#pdf_path = 'Oreilly Hands-On_Machine_Learning.pdf'
pdf_path = input('\nEnter the name of your PDF (including the extension, e.g., "file.pdf"): ')
start_page = int(input("\nEnter the start page number: "))
end_page = int(input("\nEnter the end page number: "))

# Open and read the PDF
with open(pdf_path, 'rb') as book:
    pdf_reader = PyPDF2.PdfReader(book)
    num_pages = len(pdf_reader.pages)
    
    # Ensure the page range is valid
    if start_page < 0 or end_page >= num_pages or start_page > end_page:
        print("Invalid page range. Please ensure start and end pages are within the document range and start page is less than or equal to end page.")
    else:
        for page_num in range(start_page, end_page + 1):
            page = pdf_reader.pages[page_num]
            text = page.extract_text()
            if text:
                speaker.say(text)
                speaker.runAndWait()

# python one file pdf to png

import fitz  # PyMuPDF

def pdf_to_png(pdf_file, output_folder):
    # Open the PDF file
    pdf_document = fitz.open(pdf_file)
    
    for page_number in range(pdf_document.page_count):
        # Get the page
        page = pdf_document[page_number]
        
        # Convert the page to an image
        image = page.get_pixmap()
        
        # Save the image as a PNG file
        image.save(f"{output_folder}/page_{page_number + 1}.png", "png")

    # Close the PDF file
    pdf_document.close()

if __name__ == "__main__":
    input_pdf = "input.pdf"  # Replace with your PDF file path
    output_folder = "output_images"  # Replace with your output folder
    
    pdf_to_png(input_pdf, output_folder)

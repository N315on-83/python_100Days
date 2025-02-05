from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_pdf(filename):
    # Create a canvas object with letter page size
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter

    # Set the font and size
    c.setFont("Helvetica", 12)

    # Draw some strings on the PDF
    c.drawString(100, height - 100, "Welcome to your PyPDF2 practice PDF!")
    c.drawString(100, height - 120, "This PDF was generated using ReportLab.")
    c.drawString(100, height - 140, "Feel free to experiment with PyPDF2 on this file.")

    # Save the PDF file
    c.save()

if __name__ == "__main__":
    filepath = "/Users/nelsonezeanya/Documents/Python_100_days/Nelson/DayTwentySix/practice.pdf"
    generate_pdf("practice.pdf")
    print("PDF generated successfully as 'practice.pdf'")

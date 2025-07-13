import pandas as pd
from fpdf import FPDF
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors

# Function to read CSV file
def read_csv_data(file_name):
    try:
        data = pd.read_csv(file_name)
        return data
    except Exception as e:
        print(f"❌ Error loading CSV file: {e}")
        return None

# Generate PDF using FPDF
def generate_fpdf(data, filename="report_fpdf.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Employee Report (FPDF)", ln=True, align='C')
    pdf.ln(10)

    # Header
    for col in data.columns:
        pdf.cell(60, 10, str(col), 1)
    pdf.ln()

    # Rows
    for _, row in data.iterrows():
        for item in row:
            pdf.cell(60, 10, str(item), 1)
        pdf.ln()

    pdf.output(filename)
    print(f"✅ FPDF PDF created: {filename}")

# Generate PDF using ReportLab
def generate_reportlab(data, filename="report_reportlab.pdf"):
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter

    c.setFont("Helvetica-Bold", 16)
    c.drawCentredString(width / 2, height - 50, "Employee Report (ReportLab)")

    table_data = [list(data.columns)] + data.values.tolist()

    table = Table(table_data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
    ]))

    table.wrapOn(c, width, height)
    table.drawOn(c, 30, height - 150)

    c.save()
    print(f"✅ ReportLab PDF created: {filename}")

# Main code
if __name__ == "__main__":
    file_name = "data.csv"
    data = read_csv_data(file_name)

    if data is not None:
        generate_fpdf(data)
        generate_reportlab(data)
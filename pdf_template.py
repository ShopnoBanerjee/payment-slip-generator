from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.platypus import Spacer
from reportlab.platypus import PageBreak
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.units import inch



#function for creating payment slip
def create_payment_slip(details, content):
    # Define styles
    company_name_style = ParagraphStyle(
        name='Company Name',
        fontSize=14,  # You can adjust the font size as needed
        leading=16,
        alignment=1  # Center alignment
    )
    subheading_style = ParagraphStyle(
        name='Subheading',
        fontSize=12,  # You can adjust the font size as needed
        leading=14,
        alignment=1  # Center alignment
    )

    # Company Name
    company_name_para = Paragraph("Hanglaatherium", company_name_style)
    content.append(company_name_para)

    # Subheading
    subheading_para = Paragraph("Payment Slip", subheading_style)
    content.append(subheading_para)

    content.append(Paragraph("Name: "+details[1]+" "+details[2], ParagraphStyle(name='Normal')))
    content.append(Paragraph("Emp code: "+details[0], ParagraphStyle(name='Normal')))
    content.append(Paragraph("Total Working Days: "+details[3], ParagraphStyle(name='Normal')))
    
    spacer = Spacer(1, 13)
    content.append(spacer)
    
    # Create the table
    table_data = [
        ["Earnings", "Deductions"],
        ["Basic : "+details[4], "P.T. : "+details[10]],
        ["HRA : "+details[5], "P.F. : "+details[11]],
        ["Conveyance : "+details[6], "ESI : "+details[12]],
        ["Washing : "+details[7], "Advance : "+details[13]],
        ["Overtime + "+details[8], "Total Deductions : "+details[14]],
        ["Total Earnings : "+details[9] , ""],
    ]

    # Set up table style
    table_style = TableStyle([
                               ('ALIGN', (0, 0), (-1, -1), 'CENTRE'),
                               ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                               ('BOTTOMPADDING', (0, 0), (-1, 0), 6),
                               ('GRID', (0, 0), (-1, -1), 1, colors.black),
                               ('LEFTPADDING', (0, 0), (-1, -1), 0)
                               ])

    # Create the table
    earnings_table = Table(table_data,)
    earnings_table.setStyle(table_style)
    content.append(earnings_table)
    
    spacer = Spacer(1, 13)
    content.append(spacer)

    details[9] = details[9].replace(",",'')
    details[14] = details[14].replace(",",'')
    
    content.append(Paragraph("Net Salary : "+ str(int(details[9])-int(details[14])), ParagraphStyle(name='Normal')))

    spacer = Spacer(1, 35)
    
    content.append(spacer)


#no of payment slips that pdf has
def no_of_slips(emp_no,details,content):
    
    for i in range(0,int(emp_no/3)):
        create_payment_slip(details,content)
        create_payment_slip(details,content)
        create_payment_slip(details,content)
        content.append(PageBreak())
    for i in range(0,int(emp_no%3)):
        create_payment_slip(details,content)
        content.append(PageBreak())




top_margin = 0.1
bottom_margin = 0.1

doc = SimpleDocTemplate("payslip_demo.pdf", pagesize=A4,
                        topMargin=top_margin*inch, bottomMargin=bottom_margin*inch)

content = []


no_of_slips(6,details,content)


doc.build(content)

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.platypus import Spacer
from reportlab.platypus import PageBreak
from reportlab.lib.units import inch
import pandas as pd
import os
from datetime import datetime

'''ALL THE FUNCTIONS'''





#function for creating payment slip
def create_payment_slip(details, content):
    #                 Define styles
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
    # Input date string
    date_string = details[0]
    date_obj = datetime.strptime(date_string, '%Y-%m-%d')
    formatted_date = date_obj.strftime('%B %Y')

    # Company Name
    company_name_para = Paragraph("Hanglaatherium", company_name_style)
    content.append(company_name_para)

    # Subheading
    subheading_para = Paragraph("Payment Slip of :" + " " + formatted_date, subheading_style)
    content.append(subheading_para)
    
    spacer = Spacer(1, 15)
    content.append(spacer)

    content.append(Paragraph("Name: "+details[1]+" "+details[2], ParagraphStyle(name='Normal',alignment=1)))
    content.append(Paragraph("UAN: "+details[3], ParagraphStyle(name='Normal', alignment=1)))
    content.append(Paragraph("Total Working Days: "+details[4], ParagraphStyle(name='Normal',alignment=1)))
    
    spacer = Spacer(1, 15)
    content.append(spacer)
    
    # Create the table
    table_data = [
        ["Earnings", "Deductions"],
        ["Basic : "+ details[5], "P.T. : "+ details[11]],
        ["HRA : "+ details[6], "P.F. : "+ details[12]],
        ["Conveyance : "+ details[7], "ESI : "+ details[13]],
        ["Washing : "+ details[8], "Advance : "+ details[14]],
        ["Overtime : "+ details[9], "Total Deductions : "+ details[15]],
        ["Total Earnings : "+ details[10] , "Net Salary : "+ details[16]],
    ]

    # Set up table style
    table_style = TableStyle([
                               ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                               ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                               ('BOTTOMPADDING', (0, 0), (-1, 0), 6),
                               ('GRID', (0, 0), (-1, -1), 1, colors.black)
                               ])

    # Create the table
    earnings_table = Table(table_data)
    earnings_table.setStyle(table_style)
    content.append(earnings_table)

    # details[10] = details[10].replace(",",'')
    # details[15] = details[15].replace(",",'')
    
    # content.append(Paragraph("Net Salary : "+ details[16])), ParagraphStyle(name='Normal')))
    spacer = Spacer(1, 30)
    content.append(spacer)



    
#what i want is that i create in a systematic form and that every 3 creations there is a pagebreak
#total creations are suppose 30 i.e total employees whose payslips are to be made are 30 so 
def pdf_maker(no_of_emp,listy,filename):
    top_margin = 0.1
    bottom_margin = 0.1
    doc = SimpleDocTemplate(f"{filename}_payslip.pdf", pagesize=letter,
                        topMargin=top_margin*inch, bottomMargin=bottom_margin*inch)
    content = []
    
    if (no_of_emp%3==0):
        j=0
        for i in range(0,no_of_emp//3):
            create_payment_slip(listy[j],content)
            j+=1
            create_payment_slip(listy[j],content)
            j=j+1
            create_payment_slip(listy[j],content)
            j=j+1
            content.append(PageBreak())
        
    elif (no_of_emp%3==1):
        j=0
        for i in range(0,no_of_emp//3):
                create_payment_slip(listy[j],content)
                j+=1
                create_payment_slip(listy[j],content)
                j=j+1
                create_payment_slip(listy[j],content)
                j=j+1
                content.append(PageBreak())
        create_payment_slip(listy[j],content)
        j=j+1
            
    elif (no_of_emp%3==2):
        j=0
        for i in range(0,no_of_emp//3):
                create_payment_slip(listy[j],content)
                j+=1
                create_payment_slip(listy[j],content)
                j=j+1
                create_payment_slip(listy[j],content)
                j=j+1
                content.append(PageBreak())
                
        create_payment_slip(listy[j],content)
        j=j+1
        create_payment_slip(listy[j],content)
        j=j+1
    
    doc.build(content)   


       
    
def generate_pdf(filename):
    df = pd.read_excel(f"./input/{filename}.xlsx")
    df = df.rename(columns={'Net Payment (Take Home)': 'Net Payment'})
    df=df[['Month & Year', 'Name of the employees','UAN no','Actual','Basic', 'HRA', 'conveyance', 'Washing','Extra', 'TOTAL','P.T.', 'P.F.(12%)', 'ESI (0.75%)','Adv.', 'Total deduction', 'Net Payment']]
    df=df.astype(str)
    df['Adv.'] = df['Adv.'].str.replace('nan','-')
    
    columns = [['Month & Year', 'Name of the employees','UAN no',
            'Actual','Basic', 'HRA', 'conveyance', 'Washing','Extra', 'TOTAL',
            'P.T.', 'P.F.(12%)', 'ESI (0.75%)','Adv.', 'Total deduction','Net Payment']]
    
    list_of_emp=[]
    for index, row in df.iterrows():
        words=" "
        list=[]
        for col in columns:
            words = words + ' '.join(row[col])+' '
            list=words.split()
            list_of_emp.append(list)
    
    
    no_of_emp=len(list_of_emp)
       
    pdf_maker(no_of_emp,list_of_emp,filename)
    return(f"{filename}_payslip.pdf")
    
    
    
    

''' PDF CREATION '''



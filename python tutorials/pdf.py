from fpdf import FPDF


my_pdf = FPDF()

my_pdf.add_page()
my_pdf.set_font("Arial",size = 18)
my_pdf.cell(200,10,txt = "Hello my name is arindam pradhan",ln = 1,align = "C")
my_pdf.cell(200,10,txt = "I am currently studying in class twelve",ln = 2,align = "C")
my_pdf.cell(200,10,txt = "I am a science student.. ",ln = 3,align = "C")
my_pdf.cell(200,10,txt = "I love to learn about coding. ",ln = 4,align = "C")
my_pdf.cell(200,10,txt = "I am a jee aspirant also.",ln = 5,align = "C")
my_pdf.cell(200,10,txt = "I like to learn about physics.",ln = 6,align = "C")


my_pdf.output("myPDF.pdf")
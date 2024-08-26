from fpdf import FPDF

def main():
  pdf = FPDF()
  pdf.add_page()
  pdf.set_font("helvetica", "B", 30)
  pdf.cell(200, 50, "CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT", align='C')
  pdf.image('shirtificate.png', x= 20, y= 80, w=170)
  pdf.set_text_color(r=255, g=255, b=255)
  pdf.cell(200, 150, f'{input("Name: ")} took CS50', new_x="LMARGIN", new_y="NEXT", align='C')
  pdf.output("shirtificate.pdf")

if __name__ == '__main__':
  main()


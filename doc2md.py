#!/usr/bin/python3

from docx import Document
from docx.oxml import CT_P, CT_Tbl
from docx.text.paragraph import Paragraph
from docx.table import Table

def docx_to_markdown(docx_file):
  # 读取 docx 文件
  doc = Document(docx_file)
  markdown_text = ""
  for element in doc.element.body:
    if isinstance(element, CT_P):
      paragraph = Paragraph(element, doc)
      markdown_text += f"{paragraph.text}\n\n"
    elif isinstance(element, CT_Tbl):
      table = Table(element, doc)
      markdown_text += "| " + " | ".join(cell.text for cell in table.rows[0].cells) + " |\n"
      markdown_text += "| " + " | ".join(["---"] * len(table.rows[0].cells)) + " |\n"
      for row in table.rows[1:]:
        markdown_text += "| " + " | ".join(cell.text for cell in row.cells) + " |\n"
      markdown_text += "\n"
  return markdown_text

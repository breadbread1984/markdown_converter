#!/usr/bin/python3

from docx import Document

def docx_to_markdown(docx_file):
  # 读取 docx 文件
  doc = Document(docx_file)
  markdown_text = ""
  for element in doc.element.body:
    if element.tag.endswith('p'):
      paragraph = doc.paragraphs[doc.element.body.index(element)]
      markdown_text += f"{paragraph.text}\n\n"
    elif element.tag.endswith('tbl'):
      table = doc.tables[doc.element.body.index(element) - len(doc.paragraphs)]
      markdown_text += "| " + " | ".join(cell.text for cell in table.rows[0].cells) + " |\n"
      markdown_text += "| " + " | ".join(["---"] * len(table.rows[0].cells)) + " |\n"
      for row in table.rows[1:]:
        markdown_text += "| " + " | ".join(cell.text for cell in row.cells) + " |\n"
      markdown_text += "\n"
  return markdown_text

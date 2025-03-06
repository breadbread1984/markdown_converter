#!/usr/bin/python3

from docx import Document
from markdownify import markdownify as md

def docx_to_markdown(docx_file):
  # 读取 docx 文件
  doc = Document(docx_file)
  markdown_text = ""
  for para in doc.paragraphs:
    # 将每个段落转换为 Markdown
    markdown_text += para.text + "\n\n"  # 添加两个换行符以分隔段落
  return markdown_text

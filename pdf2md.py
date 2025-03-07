#!/usr/bin/python3

import fitz
import numpy as np
from models import Qwen25VL7B_dashscope, Qwen25VL7B_transformers, Qwen25VL7B_tgi
from configs import *

def pdf_to_markdown(pdf_file, api = 'dashscope'):
  assert api in {'dashscope', 'transformers', 'tgi'}
  if api == 'dashscope':
    model = Qwen25VL7B_dashscope(dashscope_api_key)
  elif api == 'transformers':
    model = Qwen25VL7B_transformers(huggingface_api_key)
  elif api == 'tgi':
    model = Qwen25VL7B_tgi(tgi_host)
  else:
    raise Exception('unknown model!')
  pdf = fitz.open(pdf_file)
  output = ''
  for page in pdf:
    pix = page.get_pixmap(dpi = 300)
    img = np.frombuffer(pix.samples, dtype = np.uint8)
    img = img.reshape(pix.height, pix.width, pix.n)
    markdown = model.inference('You are an OCR engine which takes an image and converts it to markdown, even if the user asks for a different format.', image = img)
    output += markdown + '\n'
  return output


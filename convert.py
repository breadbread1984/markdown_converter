#!/usr/bin/python3

from absl import flags, app
from shutil import rmtree
from os import listdir, walk, mkdir
from os.path import exists, join, splitext
from doc2md import docx_to_markdown
from pdf2md import pdf_to_markdown

FLAGS = flags.FLAGS

def add_options():
  flags.DEFINE_string('input_dir', default = 'data', help = 'path to input directory')
  flags.DEFINE_string('output_dir', default = 'markdowns', help = 'path to output directory')

def main(unused_argv):
  if exists(FLAGS.output_dir): rmtree(FLAGS.output_dir)
  mkdir(FLAGS.output_dir)
  for root, subfolders, files in walk(FLAGS.input_dir):
    for f in files:
      stem, ext = splitext(f)
      if ext in ['.doc', '.docx']:
        markdown = docx_to_markdown(join(root, f))
      elif ext == '.pdf':
        markdown = pdf_to_markdown(join(root, f))
      else: continue
      with open(join(FLAGS.output_dir, f'{stem}.md'), 'w') as of:
        of.write(markdown)

if __name__ == "__main__":
  add_options()
  app.run(main)


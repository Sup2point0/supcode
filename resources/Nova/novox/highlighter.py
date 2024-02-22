'''
Novax v0.1.0
supcode Syntax Highlighter
'''

import re
import json

from io import StringIO

from selenium import webdriver


def render(file: str):
  '''Applies syntax highlighting to a .txt file and saves it as a .png file.'''

  with open(file) as f:
    text = highlight(f)
    export(text, "export.html")


def highlight(source):
  '''Apply *supcode Nova* syntax highlighting to a source file.'''

  with open("tokens.json") as f:
    tokens = json.load(f)

  new = StringIO()
  context = []

  ## contextual styles
  for line in source:
    for each in re.split("(\W)", line):

      # test different tokens
      for key, vals in tokens.items():

        # pair tokens open a new context
        if key == "pair":
          for kind, matches in vals.items():
            break
          
        # lone tokens can be simply replaced
        else:
          if each in vals:
            new.write(f'<span class="{key}">{each}</span>')
            break
          
      else:
        new.write(each)
    
    new.write("\n")

  ## character alterations
  new = new.getvalue()
  new = re.sub("=<", "&le;", new)
  new = re.sub(">=", "&ge;", new)
  ...
  # ligatures
  # dualshift

  return new


def repl(char):
  '''Replace a character.'''

  ...


def export(content, file):
  '''Save a .html file as a .png image.'''

  content = re.sub("<", "&lt;", content)
  content = re.sub(">", "&gt;", content)

  with open(file, "w") as f:
    text = f"""<!DOCTYPE html>
<html>
  <head>
    <title> supcode Render </title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="style.css">
  </head>
  <body>
    <p><pre>{content}</pre></p>
  </body>
</html>"""
    
    f.write(text)

  return

  options = webdriver.ChromeOptions()
  options.add_argument("--headless")

  driver = webdriver.Chrome(options = options)

  driver.get("data:text/html;charset=utf-8," + content)
  driver.save_screenshot(file)

  driver.quit()


def style():
  with open("tokens.json", "r") as f:
    tokens = json.load(f)

  with open("colours.json", "r") as f:
    colours = json.load(f)
  
  text = "\n".join(f".{token} \{color: {colours[token]}}" for token in tokens)
  
  with open("style.css", "w") as f:
    f.write(text)

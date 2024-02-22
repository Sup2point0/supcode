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
    text = highlight(f).getvalue()
    style()
    export(text, "export.html")


def highlight(source):
  '''Apply *supcode Nova* syntax highlighting to a source file.'''

  with open("tokens.json", "r") as f:
    tokens = json.load(f)
  with open("semantics.json", "r") as f:
    semantics = json.load(f)

  new = StringIO()
  context = []

  ## contextual styles
  for line in source:
    line = re.sub("=<", "&le;", line)
    line = re.sub(">=", "&ge;", line)

    for each in re.split("(\W)", line):

      # test different tokens
      for construct, token in tokens.items():
        if context:
          continue
        if each in token:
          new.write(f'<span class="{construct}">{repl(each)}</span>')
          break
          
      else:
        # for construct, token in semantics.items():
        #   if each in token:
        #     if context:
        #       if context[-1] == construct:
        #         context.pop()
        #         new.write(f"{repl(each)}</span>")
        #     else:
        #       context.append(construct)
        #       new.write(f'<span class="{construct}">{repl(each)}')

        # else:
          new.write(each)
    
    new.write("\n")

  ## character alterations
  ...
  # ligatures
  # dualshift

  return new


def repl(char):
  '''Replace a character.'''

  match char:
    case "<":
      return "&lt;"
    case ">":
      return "&gt;"
    case _:
      return char


def export(content, file):
  '''Save a .html file as a .png image.'''

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
  with open("novox.json", "r") as f:
    novox = json.load(f)

  text = "\n".join(
    f""".{token} {{color: {colours[novox["colours"][token]]}}}"""
    for token in tokens
  )
  text += f"\n* {{color: #fff; background-color: {colours['blue-midnight']}}}"
  
  with open("style.css", "w") as f:
    f.write(text)

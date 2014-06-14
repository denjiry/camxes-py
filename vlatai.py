
import sys

from parsimonious.exceptions import ParseError

from structures import jbovlaste_types
from camxes import configure_platform
from parsers.camxes_ilmen import Parser
from transformers.vlatai import Visitor

VLATAI_RULE = "vlatai"

def main(text):
  gensuha = analyze_morphology(text)
  print jbovlaste_types.classify(gensuha)

def analyze_morphology(text):
  parser = Parser(VLATAI_RULE)
  visitor = Visitor()
  gensuha = None
  try:
    parsed = parser.parse(text)
    gensuha = visitor.visit(parsed)
  except ParseError as e:
    pass
  return gensuha

if __name__ == '__main__':
  text = " ".join(sys.argv[1:])
  configure_platform()
  main(text)


import sys
import urllib.request
import html

if len(sys.argv) < 2:
  print(sys.argv)
  raise "Expected an argument with the URL to fetch"

url = sys.argv[1]
#print(url)

def rt(s, sep):
  if s.find(sep) < 0:
    return s
  ps = s.split(sep)
  return sep.join(ps[1:])

def lt(s, sep):
  if s.find(sep) < 0:
    return s
  ps = s.split(sep)
  return ps[0]

START = '<div align="justify">'
END = '</div></font></td></tr>'

allhtml = urllib.request.urlopen(url).read().decode('utf-8').replace('\r', '')
#allhtml = open('the-input.txt', 'rt').read().replace('\r', '')
#print(allhtml)

middle = lt(rt(allhtml, START), END)
#print(middle)

middle = html.unescape(middle.replace("<img src='/pics/PixelClear.gif' width='25' height='1' alt='     '>", ''))
middle = middle.replace('&', '&amp;')

pieces = [x.strip().replace('\n', ' ') for x in middle.split('<br />\n\n')]

def pwrap(x):
  if x.endswith('>') or x.startswith('<'):
    return x
  return '<p>' + x + '</p>'
pieces = [pwrap(x) for x in pieces]

print('\n'.join(pieces))

# #python3 grabber.py https://www.hplovecraft.com/writings/texts/fiction/bws.aspx > bws.xhtml

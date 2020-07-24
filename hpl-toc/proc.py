def proc(line):
  ps = line.split(': ')
  title = ''
  date = ''
  urls = ''
  if len(ps) == 1:
    title = ps[0]
  elif len(ps) == 2:
    title = ps[1]
    date = ps[0]
  title = title.replace('</a>', '')
  if title.find('<a href="') > -1:
    title = title.replace('<a href="', '')
    ps = title.split('">')
    title = ps[1]
    urls = '<a href="https://www.hplovecraft.com/writings/fiction/%s">HPL</a>' % (ps[0], )
  return '''<tr>
  <td>%s</td>
  <td></td>
  <td>%s</td>
  <td>%s</td>
</tr>''' % (title, date, urls)
#lines = [x for x in open('todo.txt', 'rt').read().replace('\r', '').split('\n') if x != '']
#lines = [proc(x) for x in lines]
#print('\n\n'.join(lines))

def makechunk(arr, more):
  ret = ['<tr>']
  ret += arr[3:] # URLs
  ret.append(arr[2]) # date
  ret.append(arr[1].replace('<td>', '<td>'+more)) # length + other icons
  ret.append(arr[0]) # title
  ret.append('</tr>')
  return '\n'.join(ret)

chunks = [x for x in open('input.txt', 'rt').read().replace('\r', '').split('$') if x != '']
for chunk in chunks:
  more = ''
  if chunk.find('†') > -1:
    more += '†'
  if chunk.find('‡') > -1:
    more += '‡'
  if chunk.find('∗') > -1:
    more += '∗'
  if chunk.find('⁑') > -1:
    more += '⁑'
  if chunk.find('<i class="dc"></i>') > -1:
    more += '<i class="dc"></i>'
  if chunk.find('<i class="cm"></i>') > -1:
    more += '<i class="cm"></i>'
  chunk = chunk.replace('∗', '')
  chunk = chunk.replace('⁑', '')
  chunk = chunk.replace('†', '')
  chunk = chunk.replace('‡', '')
  chunk = chunk.replace('<i class="cm"></i>', '')
  chunk = chunk.replace('<i class="dc"></i>', '')
  chunk = chunk.replace('<a href="https://www.hplovecraft.com/writings/fiction/chrono.aspx">†</a>', '')
  chunk = chunk.replace('<a href="https://www.hplovecraft.com/writings/fiction/publish.aspx">‡</a>', '')
  lines = [y for y in chunk.split('\n') if y != '']
  chunk = makechunk(lines, more)
  print(chunk)

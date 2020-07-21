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
lines = [x for x in open('todo.txt', 'rt').read().replace('\r', '').split('\n') if x != '']
lines = [proc(x) for x in lines]
print('\n\n'.join(lines))

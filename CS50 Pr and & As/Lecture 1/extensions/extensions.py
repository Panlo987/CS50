f = input('File name: ').lower().strip()
ext = f[-4 : len(f) + 1]
if ext == '.jpg':
  print('image/jpeg')
elif f[-5 : len(f) + 1] == '.jpeg':
  print('image/jpeg')
elif ext == '.pdf':
  print('application/pdf')
elif ext == '.gif':
  print('image/gif')
elif ext == '.png':
  print('image/png')
elif ext == '.txt':
  print('text/plain')
elif ext == '.zip':
  print('application/zip')
else:
  print('application/octet-stream')

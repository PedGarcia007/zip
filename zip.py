import zipfile

with zipfile.ZipFile('files.zip,','w') as my_zip:  ##('zip file name', 'type of mode'
    my_zip.write('test.txt')
    my_zip.write('image.png')

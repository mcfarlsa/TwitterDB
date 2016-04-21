import os

filelist = []

for file in os.listdir('/media/data/daily_files/raw_files/'):
    if file.endswith('.txt'):
        filename = file.replace('.txt','.trg')
        filelist.append(filename)

for file in filelist:
    with open('/media/data/daily_files/raw_files/' + file, 'w') as outfile:
        outfile.write('trigger file')
#!/usr/bin/python
import os, gzip, shutil

# in_dir -- input directory to search for trigger files (use full path with leading and trailing '/')
# gz_dir -- output directory for archived files (use full path with leading and trailing '/')
# filetype -- file extension of files being compressed (use leading '.'; ex - '.txt')
# triggertype -- file extension of trigger file (use leading '.'; ex - '.trg')

def gzipper (in_dir, gz_dir, tr_dir, filetype, triggertype):
    filelist = []
    
    for file in os.listdir(in_dir):
        if file.endswith(triggertype):
            shutil.move(in_dir + file, tr_dir + file)
            filename = file.replace(triggertype,filetype)
            filelist.append(filename)

    for item in filelist:
        with open(in_dir + item, 'rb') as f_in, gzip.open(gz_dir + item + '.gz', 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
        os.remove(in_dir + item)
    
    return filelist

if __name__ == "__main__":

    gzipper('/media/data/daily_files/raw_files/',
        '/media/data/daily_files/gz_files/',
        '/media/data/daily_files/trg_files/',
        '.txt',
        '.trg')
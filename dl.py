import tkinter as tk
import urllib.request
import sys
import re
import os
import ffmpeg
import os
import glob
import shutil
import time
import traceback
from pathlib import Path

os.chdir(os.path.dirname(__file__))
print(sys.executable)

def work():
    try:
        url = entry.get()
        m3u8_file_path = os.getcwd() + '\\' + 'download\\' + 'z.txt'
        url_base = ""

        if not url:
            return

        if not os.path.exists(os.getcwd() + '\\' + 'download'):
            os.makedirs(os.getcwd() + '\\' + 'download')
        else:
            shutil.rmtree(os.getcwd() + '\\' + 'download')
            os.makedirs(os.getcwd() + '\\' + 'download')

        urlx = filter(lambda x: "m3u8" not in x, url.split('/'))

        for item in urlx:
            url_base += item
            url_base += "/"

        #call out to the m3u8 endpoint
        urllib.request.urlretrieve(url, m3u8_file_path)

        all_ts_files = []

        # filter through the mru8 playlist and only grab the .ts endpoints
        with open(m3u8_file_path) as f:
            lines = [line.rstrip() for line in f]
            for line in lines:
                if("EXT" not in line and ".ts" in line):
                    all_ts_files.append(url_base + line)

        # download the .ts files
        cnt = 1
        for f in all_ts_files:
            print("%s/%s\r" % (cnt, len(all_ts_files)), end="")
            current_seg = 'seg-'+ str(cnt) + '-'
            file_path = os.getcwd() + '\\' + 'download\\' + current_seg + 'z.ts'
            urllib.request.urlretrieve(f, file_path)
            cnt += 1

        #sort the ts files
        files = glob.glob("%s*.ts" % (os.getcwd() + '\\' + 'download\\'))
        files.sort(key=lambda f: int(''.join(filter(str.isdigit, f))))

        #the file name of newly merged file
        epoch_timestamp = str(time.time()) + '.ts'

        #merge the .ts files
        with open(epoch_timestamp, 'wb') as merged:
            for fname in files:
                with open(fname, 'rb') as mergefile:
                    shutil.copyfileobj(mergefile, merged)

        #move merged file out of download directory
        Path(os.getcwd() + '\\' + 'download\\' + epoch_timestamp).renames(os.getcwd() + '\\' + epoch_timestamp)
    except Exception as e:
        if("no attribute 'renames'" not in str(e)):
            f = open( os.getcwd() + '\\' +'log.txt', 'a+')
            f.write('%s\n' % e)
            traceback.print_exc()
            print(e)
    finally:
        #remove non-merged .ts files
        files = glob.glob("%s*.ts" % (os.getcwd() + '\\' + 'download\\'))
        for fname in files:
            os.remove(fname)
        
        #remove mru8 file
        os.remove(m3u8_file_path)
    

window = tk.Tk()


label = tk.Label(window, text="url").pack()
entry = tk.Entry()
entry.pack()

button = tk.Button(
    text="Download!",
    width=25,
    height=5,
    bg="grey",
    fg="black",
    command=work
).pack()

window.mainloop()
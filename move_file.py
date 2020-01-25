#!/usr/bin/env python
# -*- coding: utf-8 -*-

import glob
import sys
import os
import shutil

def search_file(extension):
    file_out = []

    files = glob.glob("*")
    for file in files:
        if(extension in file):
            file_out.append(file)

    return file_out

def search_file_in_title(title, files):
    titles = []

    for file in files:
        if(title in file):
            titles.append(file)

    return titles

def mk_dir_filename(title):
    if(os.path.isdir(title) == False):
        print("Make New Directory")
        os.mkdir(title)
        return True
    else:
        print("This Directory[{}] Exsited.".format(title))
        return False

def move_file_with_title(title, files):
    if(type(files) == list):
        for file in files:
            print("{} ---> {}".format(file, title))
            shutil.move(file, title)
    else:
        shutil.move(files, title)

class dir_list_class():
    def __init__(self):
        self.dir_lists = []
        self.file_lists = []
        self.file = ""
        self.extention = ""

    def set_extention(self, extention):
        self.extention = extention

    def search_dirctory(self):
        for file in os.listdir():
            test = os.path.splitext(file)
            if("" == test[1]):
                self.dir_lists.append(test[0])

    def search_file_and_move(self):
        files = glob.glob("*")
        for dir in self.dir_lists:
            self.file_lists = []
            for self.file in files:
                if(self.extention in self.file):
                    if(dir in self.file):
                        print("{} ---->> {}".format(dir, self.file))
                        shutil.move(self.file, dir)

    def print_list(self):
        print(self.dir_lists)

if __name__ == "__main__":
    if(len(sys.argv) == 2):
        dir_list = dir_list_class()
        dir_list.search_dirctory()
        dir_list.set_extention(sys.argv[1])
        dir_list.search_file_and_move()

    elif(len(sys.argv) == 3):
        title_files = []
        mk_dir_filename(sys.argv[2])
        files = search_file(sys.argv[1])
        title_files = search_file_in_title(sys.argv[2], files)

        if len(title_files) > 1:
            print("Move File to Directory")
            move_file_with_title(sys.argv[2], title_files)

        else:
            print("Don't file")

    elif(len(sys.argv) == 1):
        dir_list = dir_list_class()
        dir_list.search_dirctory()
        dir_list.set_extention("mp4")
        dir_list.search_file_and_move()

    else:
        print("Usage:")
        print("    [Extention]")
        print("    [Extention][New DirName]")
        exit()

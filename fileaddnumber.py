#!/usr/bin/env python
#    Copyright (C) 2016  Takuya Chaen
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
import shutil
import sys
import glob
import math

class FileAddNumber():
    def do_change(self,target_dir,separate_str):
        if target_dir[len(target_dir)-1] != '/':
            target_dir = target_dir + '/'
        is_dir = os.path.isdir(target_dir)
        if is_dir == False:
            print(target_dir + " is not directory.")
            return
        get_dir_list_arg = target_dir + "*"
        file_path_list = glob.glob(get_dir_list_arg)
        change_target_files = []
        file_counter = 0
        for check_path in file_path_list:
            is_file = os.path.isfile(check_path)
            if is_file == True:
                change_target_files.append(check_path)
                file_counter = file_counter + 1
        num_len = int(math.log10(file_counter) + 1)
        if len(change_target_files) > 0:
            add_number = 0
            for change_file in change_target_files:
                file_name, ext = os.path.splitext(os.path.basename(change_file))
                add_number_string = str(add_number).zfill(num_len)
                file_name = add_number_string + separate_str + file_name
                last_set_path = target_dir + file_name + ext
                shutil.move(change_file,last_set_path)
                print(change_file + " -> " + last_set_path)
                add_number = add_number + 1
        else:
            print("change file nothing")

if __name__ == '__main__':
    args = sys.argv
    if len(args) == 3:
        change_dir = args[1]
        separate_str = args[2]
        fileaddnumber = FileAddNumber()
        fileaddnumber.do_change(change_dir,separate_str)
    else:
        print("usage: python fileaddnumber.py /change/dir _")

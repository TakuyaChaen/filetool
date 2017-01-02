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

class FileNameAdd():
    def do_change(self,target_dir,set_position,add_name):
        if target_dir[len(target_dir)-1] != '/':
            target_dir = target_dir + '/'
        is_dir = os.path.isdir(target_dir)
        if is_dir == False:
            print(target_dir + " is not directory.")
            return
        get_dir_list_arg = target_dir + "*"
        file_path_list = glob.glob(get_dir_list_arg)
        change_target_files = []
        for check_path in file_path_list:
            is_file = os.path.isfile(check_path)
            if is_file == True:
                change_target_files.append(check_path)
        if len(change_target_files) > 0:
            for change_file in change_target_files:
                file_name, ext = os.path.splitext(os.path.basename(change_file))
                if set_position == "begin":
                    file_name = add_name + file_name
                else:
                    file_name = file_name + add_name
                last_set_path = target_dir + file_name + ext
                shutil.move(change_file,last_set_path)
                print(change_file + " -> " + last_set_path)
        else:
            print("change file nothing")

if __name__ == '__main__':
    args = sys.argv
    if len(args) == 4:
        set_position = args[1]
        change_dir = args[2]
        add_name = args[3]
        filenameadd = FileNameAdd()
        filenameadd.do_change(change_dir,set_position,add_name)
    else:
        print("usage: python filenameadd.py begin /change/dir addname")
        print("       python filenameadd.py end /change/dir addname")

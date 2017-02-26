
import os
import shutil
import sys
import glob


class FileMoveWithNum():
    def do_move(self,source_dir,dest_dir,move_num):
        if move_num.isdigit() == False:
            print("please input number")
            return
        move_num_int = int(move_num)
        if source_dir[len(source_dir)-1] != '/':
            source_dir = source_dir + '/'
        if dest_dir[len(dest_dir)-1] != '/':
            dest_dir = dest_dir + '/'
        is_dir = os.path.isdir(source_dir)
        if is_dir == False:
            print(source_dir + " is not directory.")
            return
        is_dir = os.path.isdir(dest_dir)
        if is_dir == False:
            print(des_dir + " is not directory.")
            return
        get_dir_list_arg = source_dir + "*"
        file_path_list = glob.glob(get_dir_list_arg)
        move_files = []
        file_counter = 0
        for check_path in file_path_list:
            is_file = os.path.isfile(check_path)
            if is_file == True:
                move_files.append(check_path)
                file_counter = file_counter + 1
            if move_num_int == file_counter:
                break
        if len(move_files) > 0:
            for change_file in move_files:
                file_name, ext = os.path.splitext(os.path.basename(change_file))
                last_set_path = dest_dir + file_name + ext
                shutil.move(change_file,last_set_path)
                print(change_file + " -> " + last_set_path)

if __name__ == '__main__':
    args = sys.argv
    if len(args) == 4:
        source_dir = args[1]
        dest_dir = args[2]
        move_num = args[3]
        filemove = FileMoveWithNum()
        filemove.do_move(source_dir,dest_dir,move_num)
    else:
        print("usage: python filemovewithnum.py sourcdir/ destdit/ 10")

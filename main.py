from glob import glob
import os
import shutil

def main():
    normal_picture_paths = glob("./VRChat_*.png")
    wide_picture_paths = glob("./VRChat *.png")
    print(normal_picture_paths)
    print(wide_picture_paths)

    for path in normal_picture_paths:
        date_list = path.split("_")[2].split("-")
        formated_path = f"{date_list[0].zfill(2)}-{date_list[1].zfill(2)}"

        os.makedirs(formated_path, exist_ok=True)
        shutil.move(path, formated_path)
    
    for path in wide_picture_paths:
        date_list = path.split(" ")
        formated_path = f"{date_list[1].zfill(2)}-{date_list[2].zfill(2)}"

        os.makedirs(formated_path, exist_ok=True)
        shutil.move(path, formated_path)

if __name__ == '__main__':
    main()
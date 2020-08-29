#!/usr/bin/env python3

import json
import os
import pathlib
import shutil
import sys
import zipfile


def tsnano_to_wintime(tsnano):
    epoch_in_wintime = 116444736000000000
    return int(epoch_in_wintime + (tsnano / 100))

def update_layout(package_dir):
    layout_json = {}
    layout_json_path = os.path.join(package_dir, "layout.json")
    with open(layout_json_path, "r") as old_layout:
        layout_json = json.load(old_layout)
        files = layout_json["content"]
        for file in files:
            path = file["path"]
            stats = os.stat(os.path.join(package_dir, path))
            size = stats.st_size
            mtime = stats.st_mtime_ns
            wintime = tsnano_to_wintime(mtime)
            file["size"] = size
            file["date"] = wintime

    shutil.copyfile(layout_json_path, os.path.join(package_dir, "layout.json.bak"))
    with open(layout_json_path, "w", newline='\r\n') as new_layout:
        json.dump(layout_json, new_layout, indent=4)
    os.unlink(os.path.join(package_dir, "layout.json.bak"))

def zip_package(package_dir):
    package_path = pathlib.Path(package_dir)
    zip_dir = package_path.parent
    zip_name = package_path.name

    old_dir = os.getcwd()
    os.chdir(zip_dir)
    
    with zipfile.ZipFile(f"{zip_name}.zip", "w") as zipped:
        try:
            for root, dirs, files in os.walk(zip_name):
                for file in files:
                    zipped.write(os.path.join(root, file))
        finally:
            os.chdir(old_dir)
        
        


def main():
    package_dir = sys.argv[1]
    update_layout(package_dir)
    zip_package(package_dir)

if __name__ == "__main__":
    main()

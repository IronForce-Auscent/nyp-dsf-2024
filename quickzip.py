import argparse
import pathlib
import zipfile

def zip_target_folder(module_id: int, week: int, target: str):
    target_dir = pathlib.Path(f"{module_id}/Week{week}/{target}")

    with zipfile.ZipFile(f"{module_id}-Week{week}-{target}.zip", mode="w") as archive:
        for file_path in target_dir.iterdir():
            archive.write(file_path, arcname=file_path.name)
    
    print("Zip created")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="File zipper")
    parser.add_argument('-module', "-m", dest='module_id', help='Module ID', required=True)
    parser.add_argument('-week', "-w", dest='week', help='Week', required=True)
    parser.add_argument('-target', "-t", dest='target', help='Target Folder', required=True)

    args = parser.parse_args()

    module_id = args.module_id
    week = args.week
    target = args.target
    zip_target_folder(module_id, week, target)
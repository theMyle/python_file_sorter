import os

class FileEntry:
	def __init__(self, absPath, destPath, fileName, ext):
		self.srcPath = absPath
		self.destPath = destPath
		self.fileName = fileName
		self.ext = ext

def scanFiles(output_dir_name, path) -> tuple[list[FileEntry], set[str]]:
	extensions = set()
	file_entries: list[FileEntry] = []
	baseDir = os.path.abspath(path)

	for root, _, files in os.walk(path):

		root = os.path.abspath(root)
		for name in files:
			abspath = os.path.join(root, name)
			fileName, ext = os.path.splitext(name)
			ext_clean = ext[1:] if ext else 'no_extension'
			destPath = os.path.join(baseDir, output_dir_name, ext_clean, name)
			extensions.add(ext_clean)
			file_entries.append(FileEntry(abspath, destPath, fileName, ext))

	return file_entries, extensions

def moveFile(file: FileEntry):
	# auto rename if file exists

	# skip "sorted" files
	if file.srcPath == file.destPath:
		return

	# move if no existing file
	res = os.path.exists(file.destPath)
	if not res:
		os.rename(file.srcPath, file.destPath)
		return

	counter = 1
	destDirName = os.path.dirname(file.destPath)

	# will loop until destPath is free and move the file
	while res:
		for i in range(counter, counter + 5):
			newFileName = f"{file.fileName} ({i}){file.ext}"
			newDest = os.path.join(destDirName, f"{newFileName}")
			if not os.path.exists(newDest):
				os.rename(file.srcPath, newDest)
				res = False
				break
		counter += 5

def main():
	folder_name = "PySort"
	targetDir = input("Enter directory path to be sorted: ")

	if not os.path.exists(targetDir):
		print("\nProvided path doesn't exists.")
		return

	prompt = input(f"\nAre you sure you want to sort this directory?\n{os.path.abspath(targetDir)} (y/N): ")
	if prompt[0].lower() != "y":
		print("\nOperation cancelled")
		return

	# scan files recursively
	files, extensions = scanFiles(folder_name, targetDir) 

	# create output dir
	if os.path.exists(folder_name):
		print("Path Exists")
	else:
		os.mkdir(folder_name)

	# create sub folders inside output dir
	for ext in extensions:
		folder_path = os.path.join(folder_name, ext)
		if not os.path.exists(folder_path):
			os.mkdir(folder_path)
		else:
			print(f"{ext} folder already exists")

	# move files
	for file in files:
		# check if file exists
		# check for duplicates and automatically rename
		moveFile(file)

	# delete empty folders
	for root, dirs, _ in os.walk(targetDir, topdown=False):
		for d in dirs:
			dir_path = os.path.join(root, d)
			if not os.listdir(dir_path):
				print(f"able to delete: {dir_path}")
				os.rmdir(dir_path)

	# delete empty PySort folder
	if not os.listdir(folder_name):
		os.rmdir(folder_name)

main()

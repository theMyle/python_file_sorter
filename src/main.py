import os

class FileEntry:
	def __init__(self, absPath, destPath, fileName, ext):
		self.srcPath = absPath
		self.destPath = destPath
		self.fileName = fileName
		self.ext = ext

def scanFiles(path:str, outputDirName="PySort", unsortMode=False) -> tuple[list[FileEntry], set[str]]:
	extensions = set()
	file_entries: list[FileEntry] = []
	baseDir = os.path.abspath(path)

	for root, _, files in os.walk(path):

		root = os.path.abspath(root)
		for name in files:
			abspath = os.path.join(root, name)
			fileName, ext = os.path.splitext(name)
			ext_clean = ext[1:] if ext else 'no_extension'
			destPath = None

			if unsortMode:
				destPath = os.path.join(baseDir, name)
			else:
				destPath = os.path.join(baseDir, outputDirName, ext_clean, name)

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

def sortFiles(targetDir: str, outputFolderName: str):
	print("\nScanning files 🔎...")

	# scan files recursively
	files, extensions = scanFiles(targetDir) 

	print(f"Total files seen 🔎: {len(files)}\n")

	# create output dir
	if not os.path.exists(outputFolderName):
		os.mkdir(outputFolderName)

	# create sub folders inside output dir
	for ext in extensions:
		folder_path = os.path.join(outputFolderName, ext)
		if not os.path.exists(folder_path):
			os.mkdir(folder_path)

	print("Moving files, please wait 📂📂📂...")

	# move files
	for file in files:
		# check if file exists
		# check for duplicates and automatically rename
		moveFile(file)

	print("Cleanup 🧹🧹🧹...")

	# delete empty folders
	for root, dirs, _ in os.walk(targetDir, topdown=False):
		for d in dirs:
			dir_path = os.path.join(root, d)
			if not os.listdir(dir_path):
				os.rmdir(dir_path)

	# delete empty PySort folder
	if not os.listdir(outputFolderName):
		os.rmdir(outputFolderName)

	print("\nOperation complete! ✅")

def unsortFiles(targetDir: str):
	print("\nScanning files 🔎...")

	# scan files recursively
	files, extensions = scanFiles(targetDir, unsortMode=True) 

	print(f"Total files seen 🔎: {len(files)}\n")
	print("Moving files, please wait 📂📂📂...")

	# move files
	for file in files:
		# check if file exists
		# check for duplicates and automatically rename
		moveFile(file)

	print("Cleanup 🧹🧹🧹...")

	# delete empty folders
	for root, dirs, _ in os.walk(targetDir, topdown=False):
		for d in dirs:
			dir_path = os.path.join(root, d)
			if not os.listdir(dir_path):
				os.rmdir(dir_path)

	print("\nOperation complete! ✅")

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
	
	sortFiles(targetDir, folder_name)
	# unsortFiles(targetDir)

main()

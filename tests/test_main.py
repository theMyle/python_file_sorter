import sys
import unittest
import os
import shutil

test_path = os.path.dirname(os.path.abspath(__file__))
test_folder = os.path.join(test_path, "sample_dir")

# 6 files types for each dir
file_types = [".docx", ".ppt", ".txt", ".mp4", ".mp3", "_no_ext"]
dir_names = []
num_of_dirs = 5
num_of_files = len(file_types) * num_of_dirs 

class TestSortFiles(unittest.TestCase):
    # test startUp
    def setUp(self):
        if not os.path.exists(test_folder):
            os.mkdir(test_folder)
        else:
            shutil.rmtree(test_folder)
            os.mkdir(test_folder)

        # create dir from 1 - 5 
        for i in range(1, num_of_dirs + 1):
            dir_name = os.path.join(test_folder, f"sample_dir_{i}")
            dir_names.append(dir_name)
            os.mkdir(dir_name)
        
        for dir in dir_names:
            # create sample files
            for ext in file_types:
                file_path = os.path.join(dir, f"sample_file{ext}")
                open(file_path, "w").close()

    # test cleanUp 
    def tearDown(self):
        if os.path.exists(test_folder):
            shutil.rmtree(test_folder)

    def test_setup(self):
        self.assertTrue(os.path.exists(test_folder))

    def test_sort(self):
        src_path = os.path.abspath(os.path.join(test_path, "../src"))
        if src_path not in sys.path:
            sys.path.insert(0, src_path)

        # import the main.py file for testing
        from main import sortFiles, unsortFiles, scanFiles

        # run the sorting logic
        sortFiles(test_folder, testing=True)

        files = []
        # check the output for correctness
        for root, _, file_list in os.walk(test_folder):
            files += file_list

        self.assertEqual(len(files), num_of_files)

        # check the number of each file extension: there should be 5 each
        for ext in file_types:
            if ext == "_no_ext":
                # files with no extension
                count = len([f for f in files if '.' not in f])
            else:
                count = len([f for f in files if f.endswith(ext)])
            self.assertEqual(count, num_of_dirs, f"Expected {num_of_dirs} files with extension {ext}, found {count}")

    def test_unsort(self):
        src_path = os.path.abspath(os.path.join(test_path, "../src"))
        if src_path not in sys.path:
            sys.path.insert(0, src_path)

        # import the main.py file for testing
        from main import sortFiles, unsortFiles, scanFiles

        # run the sorting logic
        unsortFiles(test_folder, testing=True)

        files = []
        # check the output for correctness
        for root, _, file_list in os.walk(test_folder):
            files += file_list

        self.assertEqual(len(files), num_of_files)

        # check the number of each file extension: there should be 5 each
        for ext in file_types:
            if ext == "_no_ext":
                # files with no extension
                count = len([f for f in files if '.' not in f])
            else:
                count = len([f for f in files if f.endswith(ext)])
            self.assertEqual(count, num_of_dirs, f"Expected {num_of_dirs} files with extension {ext}, found {count}")

if __name__ == "__main__":
    unittest.main()
import os
import filecmp

def check_eq_files(path1, path2):
    """ Return True if both files are identical, False otherwise """
    return filecmp.cmp(path1, path2, shallow=False)

def check_eq_dir(path1, path2):
    """ Return True if both folders have totally identical files, False otherwise """
    d = filecmp.dircmp(path1, path2)
    a = d.left_only + d.right_only + d.diff_files + d.funny_files
    if a:
        return False
    else:
        return True

def path_input(path=None):
    if path:
        return os.path.join('tests', 'files', path)
    else:
        return os.path.join('tests', 'files')

def path_results(path=None):
    if path:
        return os.path.join('tests', 'results', path)
    else:
        return os.path.join('tests', 'results')

def path_output(path=None):
    if path:
        return os.path.join('tests', 'out', path)
    else:
        return os.path.join('tests', 'out')
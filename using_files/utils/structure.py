# pip install easy-media-utils
from tree_utils.struct_tree_out import print_tree

path = r'../../../Operation_logs'
exclude_dirs_set = {'using_files'}
print_tree(directory=path, exclude_dirs=exclude_dirs_set)

""" Working With The Operating System """

# 1. Navigating File Paths
# To craft and dissect paths, ensuring compatibility across realms (operating systems):

import os
# Craft a path compatible with the underlying OS
path = os.path.join('mystic', 'forest', 'artifact.txt')
# Retrieve the tome's directory
directory = os.path.dirname(path)
# Unveil the artifact's name
artifact_name = os.path.basename(path)


# 2. Listing Directory Contents
# To reveal all entities within a mystical directory:

import os
contents = os.listdir('enchanted_grove')
print(contents)


# 3. Creating Directories
# To conjure new directories within the fabric of the filesystem:

import os
# create a single directory
os.mkdir('alchemy_lab')
# create a hierarchy of directories
os.makedirs('alchemy_lab/potions/elixirs')


# 4. Removing Files and Directories
# To erase files or directories, banishing their essence:

import os
# remove a file
os.remove('unnecessary_scroll.txt')
# remove an empty directory
os.rmdir('abandoned_hut')
# remove a directory and its contents
import shutil
shutil.rmtree('cursed_cavern')


# 5. Executing Shell Commands
# To invoke the shell’s ancient powers directly from Python:

import subprocess
# Invoke the 'echo' incantation
result = subprocess.run(['echo', 'Revealing the arcane'], capture_output=True, text=True)
print(result.stdout)


# 6. Working with Environment Variables
# To read and inscribe upon the ethereal environment variables:

import os
# Read the 'PATH' variable
path = os.environ.get('PATH')
# Create a new environment variable
os.environ['MAGIC'] = 'Arcane'


# 7. Changing the Current Working Directory
# To shift your presence to another directory within the filesystem:

import os
# Traverse to the 'arcane_library' directory
os.chdir('arcane_library')


# 8. Path Existence and Type
# To discern the existence of paths and their nature — be they file or directory:

import os
# Check if a path exists
exists = os.path.exists('mysterious_ruins')
# Ascertain if the path is a directory
is_directory = os.path.isdir('mysterious_ruins')
# Determine if the path is a file
is_file = os.path.isfile('ancient_manuscript.txt')


# 9. Working with Temporary Files
# To summon temporary files and directories, fleeting and ephemeral:

import tempfile
# Create a temporary file
temp_file = tempfile.NamedTemporaryFile(delete=False)
print(temp_file.name)
# Erect a temporary directory
temp_dir = tempfile.TemporaryDirectory()
print(temp_dir.name)


# 10. Getting System Information
# To unveil information about the host system, its name, and the enchantments it supports:

import os
import platform
# Discover the operating system
os_name = os.name  # 'posix', 'nt', 'java'
# Unearth detailed system information
system_info = platform.system()  # 'Linux', 'Windows', 'Darwin'







"""
os.chown: 
"""

import os
import constants

print(os.chown(constants.file_path3, 1000, 1500))

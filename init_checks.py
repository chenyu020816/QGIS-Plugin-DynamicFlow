import os
import sys
import subprocess
import platform
import pip
from PyQt5.QtWidgets import QMessageBox

def check_and_install_requirements():
    try:
        import geopandas
    except ModuleNotFoundError:
        print('installing geopandas')
        if platform.system() == 'Windows':
            subprocess.call([sys.exec_prefix + '/python', "-m", 'pip', 'install', 'geopandas'])
        else:
            subprocess.call(['python3', '-m', 'pip', 'install', 'geopandads'])
        try:
            import geopandas
            print('installation completed')
        except ModuleNotFoundError:
            QMessageBox.information(None, 'ERROR',
                                    """During the first startup this program there are some third party packages that is required to be installed, 
GeoDataFarm tried to install them automatic but failed. You can try to manually install the two packages with "pip install geopandas", "pip install reportlab", "pip install cython", "pip install pandas"
(If you are using Windows you need to run it from the OSGeo4W shell) 
If can't get the plugin to work, don't hesitate to send an e-mail to geodatafarm@gmail.com and tell which os you are using and QGIS version.""")
            sys.exit()
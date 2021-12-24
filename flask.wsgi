import sys
import site
import os.path

# Add custom site-packages directory
your_env_package_dir = '/home/va/.virtualenvs/api/lib/python3.9/site-packages'
site.addsitedir(your_env_package_dir)

# Add greetr to system path
app_path = os.path.dirname(__file__)
sys.path.insert(0, app_path)

from greetr import app as application

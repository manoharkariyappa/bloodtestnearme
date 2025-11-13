import subprocess
import sys

def after_install():
    """Auto install required Python packages"""
    packages = ["qrcode[pil]", "python-barcode~=0.15.1"]
    for pkg in packages:
        subprocess.check_call([sys.executable, "-m", "pip", "install", pkg])

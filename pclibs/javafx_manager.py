import os
import sys
import shutil
import zipfile
import requests
import tempfile
from pathlib import Path

from typing import Union

class JavaFXManager:
    url = "https://gluonhq.com/download/javafx-{}-{}-{}-sdk-windows/"
    temp_folder = Path(tempfile.gettempdir())
    filename = "javafx_sdk_{}.zip"

    def __init__(self, version="11.0.2"):
        self.version  = version
        self.url      = self.url.format(*version.split("."))
        self.filename = self.filename.format(version)

    def __clean_temp(self):
        os.remove(self.temp_folder / self.filename)
        shutil.rmtree(self.temp_folder / "javafx-sdk-{}".format(self.version))
    
    def download(self):
        params = { 'stream': True }
        
        response = requests.get(self.url, params=params)

        tempfile = self.temp_folder / self.filename
        
        if response.status_code == 200:
            total_bytes = 0 
            with open(tempfile, "wb") as javafx_zip:
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        total_bytes += 1024
                        javafx_zip.write(chunk)
                        yield "\rBaixado: {:.2f}MB...".format(total_bytes / (1024.0 * 1024.0))
    
    def extract_to(self, path: Union[str, Path]):
        with zipfile.ZipFile( self.temp_folder / self.filename ) as sdk_zip:
            sys.stdout.write("Extraindo...")
            sdk_zip.extractall(path=self.temp_folder)
        
        for folder in self.temp_folder.joinpath("javafx-sdk-{}".format(self.version)).iterdir():
            for item in folder.iterdir():
                shutil.move(item, path / folder.parts[-1] )

        self.__clean_temp()


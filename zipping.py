import os
import zipfile
import tempfile
import argparse
import logging
import shutil
import sys


class Zipping:
    def __init__(self, flname):
        self.myflname = flname
        self.mynewflname = self.myflname + '_new'
        self.pattern = "__init__.py"
        try:
            self.tmpdir = tempfile.mkdtemp()
            logging.info(f'Created tmpdir: {self.tmpdir}')
        except Exception as err:
            logging.error(err)
            sys.exit(1)

    def mycleanup(self):
        try:
            shutil.rmtree(self.tmpdir)
            logging.info(f'Deleted tmpdir: {self.tmpdir}')
        except Exception as err:
            logging.error(err)

    def myunzp(self):
        # 2. Unzip archive to temp directory.
        try:
            with zipfile.ZipFile(f'{self.myflname}.zip', 'r') as zf:
                zf.extractall(self.tmpdir)
                logging.info(f'Archive [{self.myflname}.zip] extracted in {self.tmpdir}')
        except Exception as err:
            logging.error(err)
            sys.exit(1)

    def mydelfl(self):
        # 3. Remove subfolders which don't contain __init__.py.
        for dirpath, dirnames, files in os.walk(self.tmpdir):
            if self.pattern not in files and self.pattern not in dirnames:
                shutil.rmtree(dirpath)
                d = dirpath.replace(self.tmpdir, "")
                logging.debug(f'Dir {d} deleted')

    def myzp(self):
        # 4. Create new archive with _new prefix (<old_name>_new.zip)
        with zipfile.ZipFile(f'{self.mynewflname}.zip', "w") as zf:
            for dirpath, dirnames, files in os.walk(self.tmpdir):
                for f in files:
                    filepath = os.path.join(dirpath, f)
                    filename = dirpath.replace(self.tmpdir, "") + '/' + f
                    zf.write(filepath, filename)
                    logging.debug(f'File {filename} added in {self.mynewflname}')


parser = argparse.ArgumentParser()
parser.add_argument('-n', help="Zip archive name", type=str)
args = parser.parse_args()

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    filename=f'{args.n}.log')

obj = Zipping(args.n)
obj.myunzp()
obj.mydelfl()
obj.myzp()
obj.mycleanup()

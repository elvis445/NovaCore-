import sys
import os

base_dir=os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,base_dir)
sys.path.insert(0,os.path.join(base_dir,"web"))

from app import app
if __name__ == "__main__":
    app.run()




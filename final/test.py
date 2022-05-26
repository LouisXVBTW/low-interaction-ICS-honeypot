import os, sys
filename = os.path.dirname(__file__)+'/dashboard'

os.system(f'cd {filename};uvicorn dashboard:app --reload')
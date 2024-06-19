import os
from flask import Flask

project_root = os.path.abspath('')
template_path = os.path.join(project_root, 'templates')

app = Flask(__name__, template_folder=template_path)

from app import routes

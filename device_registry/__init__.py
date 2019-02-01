import markdown
import os
# Import the framework
from flask import Flask

# Create an instance of flask
app = Flask(__name__)

@app.route("/")
def index():
    """Present some documentation"""

    # Open the Readme file
    with open(os.path.dirname(app.root_path)+'/Readme.md', 'r') as markdown_files:

        # Read the content of the file
        content = markdown_files.read()

        # Conver to HTML
        return markdown.markdown(content)

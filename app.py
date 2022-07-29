from flask import Flask
import sys
import project_name
from project_name.logger import logging
from project_name.exception import Project_nameException

app=Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    try:
        raise Exception("We are testing custom exception")
    except Exception as e:
        project_name = Project_nameException(e, sys)
        logging.info(project_name.error_message)
        logging.info("We are testing logging module")
    return "CI CD pipeline has been established."

if __name__=="__main__":
    app.run(debug=True)

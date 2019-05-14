from flask import Flask, request, render_template, Response, flash, redirect, url_for
from flask_bootstrap import Bootstrap
import boto3
import yaml
import csv

config = yaml.load(open('config.yml'))  # load values from config.yml

app = Flask(__name__)
Bootstrap(app)
app.debug = False
app.config['SECRET_KEY'] = '7dfdskodf9f9rf9CVFEEEDFf2b6176a'
bucket_name = config['bucket']  # name bucket from config.yml
ALLOWED_EXTENSIONS = set(['csv'])
s3 = boto3.client("s3")


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def upload_file_to_s3(fileName, bucket_name):
    """
    Docs: http://boto3.readthedocs.io/en/latest/guide/s3.html
    """
    print fileName.read()
    try:
        s3.upload_fileobj(
            fileName,
            bucket_name,
            fileName.filename
        )

    except Exception as e:
        print("Error: ", e)
        return e


@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        if "user_file" not in request.files:
            flash("No user_file key in request.files")
        UploadedFile = request.files["user_file"]
        if UploadedFile.filename == "":
            flash("Please select a file")
        if UploadedFile and allowed_file(UploadedFile.filename):
            '''Print CSV'''
            table_html = """<table border="1">\n<tr><th>col1</th><th>col2</th><th>col3</th></tr>"""
            f = UploadedFile.read()
            for line in f.splitlines():
                line = line.split(",")
                if len(line[0]) != 0:
                    table_html += """\n<tr><td>%s</td><td>%s</td><td>%s</td></tr>""" % (
                        line[0].replace('"', ''), line[1].replace('"', ''), line[2].replace('"', ''))
            table_html += "\n</table>"
            '''Upload File to S3'''
            upload_file_to_s3(request.files["user_file"], bucket_name)
            flash('You file was uploaded to S3')
            return render_template('show_csv.html', result=table_html)
        else:
            flash('you can upload only csv file')

    return render_template('index.html')


@app.route('/history', methods=['GET'])
def history():
    table_html = """<table border="1">\n<tr><th>FileName</th></tr>"""
    response = s3.list_objects(
    Bucket=bucket_name,
    Delimiter='string')
    for i in response['Contents']:
        table_html += """\n<tr><td>%s</td></tr>""" % i['Key']
    table_html += "\n</table>"
    return render_template('show_csv.html', result=table_html)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

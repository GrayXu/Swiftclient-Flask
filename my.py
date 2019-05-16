import os
from flask import Flask, render_template, request, url_for, send_from_directory
import platform

from SwiftClientTool import ConnUtil

app = Flask(__name__)
UPLOAD_FOLDER = 'request_upload'
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

@app.route('/')
def hello_world():
    # ip = request.remote_addr
    return render_template('login.html')


@app.route('/data', methods=['GET', 'POST'])
def data_handle():
    print(request)
    if ConnUtil.con is None:
        user = request.form['user']
        print(user)
        password = request.form['password']
        print(password)
        endpoint = request.form['endpoint']
        print(endpoint)

        ConnUtil.init_param(user, password, endpoint)

    result = ConnUtil.getList()
    output_list = []
    for i in result:
        output_list.append((i.pop("name"), i))
    # print(output_list)

    return render_template('data.html', name_list=sorted(output_list,key=lambda x:x[1]['last_modified'],reverse=True))


@app.route('/upload', methods=['GET', 'POST'])
def file_handle():
    # print(request)
    fname = request.form['new_name']
    print(fname)
    if fname is not None:
        f = request.files['new_file']  # get file
        print(f)
        ConnUtil.uploadFile(f, fname)

    result = ConnUtil.getList()
    output_list = []
    for i in result:
        output_list.append((i.pop("name"), i))
    # print(output_list)
    
    return render_template('data.html', name_list=sorted(output_list,key=lambda x:x[1]['last_modified'],reverse=True))


@app.route('/delete', methods=['GET', 'POST'])
def delete_handle():
    form_dic = request.form.to_dict()

    for key in form_dic.values():
        print(key)

        ConnUtil.deleteFile(key)

    result = ConnUtil.getList()
    output_list = []
    for i in result:
        output_list.append((i.pop("name"), i))
    # print(output_list)

    return render_template('data.html', name_list=sorted(output_list,key=lambda x:x[1]['last_modified'],reverse=True))

@app.route('/geturl', methods=['GET', 'POST'])
def url_handle():
    form_dic = request.form.to_dict()
    temp_url = None
    for key in form_dic.values():
        temp_url = ConnUtil.getTempUrl(key)

    print(temp_url)
    return temp_url


@app.route('/download', methods=['GET', 'POST'])
def download_handle():

    form_dic = request.form.to_dict()

    for key in form_dic.values():
        print(key)
        print(ConnUtil.downloadFile(key))

        return send_from_directory(BASE_DIR, "temp_file/"+key)



if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    if platform.system() == 'Linux':
        app.run(host='0.0.0.0', port=88)
    else:
        app.run()

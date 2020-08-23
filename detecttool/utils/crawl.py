import requests
import json
import io
import tarfile
import zipfile

def getcontent(url, st):
    try:
        r = requests.get(url, stream=st)
        r.raise_for_status()
    except requests.ConnectionError:
        print("Connection Error. Make sure you are conected to Internet.")
        return
    except requests.Timeout:
        print("Timeout Error")
        return
    except requests.URLRequired:
        print("Invalid URL")
        return
    except requests.RequestException:
        print("General Error. Technical Details given below")
        return
    return r.content


def gettar(content):
    tmp = content.decode('utf8')
    try:
        data = json.loads(tmp)
    except json.decoder.JSONDecodeError as e:
        print("An error occurred in the bytes-> json conversion process.")
        return
    url = data["urls"][-1]["url"]
    filetype = url[-3:]
    if filetype == "zip":
        name = data["urls"][-1]["filename"]
        name=name.replace(".zip","")
    elif filetype == ".gz":
        name = data["urls"][-1]["filename"]
        name = name.replace(".tar.gz","")
        filetype = "tar.gz"
    return url, name,filetype


def getsetup(content, filename,filetype):
    fileobject = io.BytesIO(content)
    try:
        if filetype=="tar.gz":
            tar = tarfile.open(fileobj=fileobject)
            filecontent = tar.extractfile(filename).read().decode()
        elif filetype == "zip":
            print('This type is not supported')
            return 
    except Exception as e:
        error = f'Don\'t have {filename} file'
        return
    return filecontent

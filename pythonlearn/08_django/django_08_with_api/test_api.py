import requests


def test_file_upload():
    url = "http://127.0.0.1:8000/uploadfile/"
    file_path = "db.sqlite3"  # 替换为你实际要上传的文件路径
    files = {'file': open(file_path, 'rb')}
    data = {'description': '这是一个测试用的文件描述', "file_id": "123"}
    response = requests.post(url, files=files, data=data)
    assert response.status_code == 200
    result = response.json()
    assert 'filename' in result
    assert 'description' in result
    assert 'message' in result
    print("文件上传接口测试通过")


if __name__ == "__main__":
    test_file_upload()

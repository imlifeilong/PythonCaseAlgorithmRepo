from fastapi import FastAPI, File, UploadFile, Form
import shutil
import uvicorn

app = FastAPI()


@app.post("/uploadfile/")
async def create_upload_file(
        file: UploadFile = File(...),
        file_id: str = Form(...),
        description: str = Form(...)
):
    """
    接收文件上传并处理额外参数的接口

    - **file**: 要上传的文件
    - **description**: 关于文件的描述信息（额外参数）
    """
    print(file_id)
    file_path = f"./{file.filename}"
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "filename": file.filename,
        "file_id": file_id,
        "description": description,
        "message": "文件上传成功"
    }


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)

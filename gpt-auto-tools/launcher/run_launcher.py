
from tkinter import *
import subprocess
import os

apps = {
    "입고 OCR 실행": "../01_입고자동화/입고OCR.exe",
    "입고 비교기 실행": "../01_입고자동화/입고비교기.py",
    "BOM 생성기 실행": "../02_BOM자동화/BOM생성기.exe",
    "PDF 요약기 실행": "../03_문서자동화/메뉴얼요약기.exe"
}

def run_app(path):
    if path.endswith(".py"):
        subprocess.Popen(["python", path], shell=True)
    else:
        subprocess.Popen(path, shell=True)

root = Tk()
root.title("GPT 업무자동화 실행기")

for name, path in apps.items():
    Button(root, text=name, width=40, command=lambda p=path: run_app(os.path.abspath(p))).pack(pady=5)

root.mainloop()

import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

def select_image_file():
    image_file = filedialog.askopenfilename(
        title=".png .jpg .jpeg .bmp 확장자 파일찾기",
        filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp")]
    )
    if image_file:
        image_file_var.set(image_file)

def select_zip_file():
    zip_file = filedialog.askopenfilename(
        title="ZIP 파일 선택",
        filetypes=[("*.zip")]
    )
    if zip_file:
        zip_file_var.set(zip_file)

def save_output_file():
    image_file = image_file_var.get()
    if not image_file:
        messagebox.showerror("오류", "이미지 파일을 먼저 선택하세요.")
        return


    _, ext = os.path.splitext(image_file)

 
    output_file = filedialog.asksaveasfilename(
        defaultextension=ext,
        filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp")],
        title="출력 파일 저장"
    )
    if output_file:
        output_file_var.set(output_file)
        app.after(1000, merge_files)

def merge_files():
    image_file = image_file_var.get()
    zip_file = zip_file_var.get()
    output_file = output_file_var.get()

    if not image_file or not zip_file:
        messagebox.showerror("오류", "모든 파일을 선택해야 합니다.")
        return

    if not output_file:
        messagebox.showerror("오류", "출력 파일 이름을 입력해야 합니다.")
        return

    try:
        with open(output_file, 'wb') as outfile:
            with open(image_file, 'rb') as img:
                shutil.copyfileobj(img, outfile)
            with open(zip_file, 'rb') as zf:
                shutil.copyfileobj(zf, outfile)
        messagebox.showinfo("성공", f"파일이 성공적으로 생성됨: {output_file}")
    except Exception as e:
        messagebox.showerror("오류", f"실패: {e}")

app = tk.Tk()
app.title("zip + 이미지 olr ol run")

image_file_var = tk.StringVar()
zip_file_var = tk.StringVar()
output_file_var = tk.StringVar()


tk.Label(app, text="이미지 파일:").pack(pady=5)
tk.Entry(app, textvariable=image_file_var, width=50).pack(padx=10)
tk.Button(app, text="이미지 파일 선택", command=select_image_file).pack(pady=5)


tk.Label(app, text="ZIP 파일:").pack(pady=5)
tk.Entry(app, textvariable=zip_file_var, width=50).pack(padx=10)
tk.Button(app, text="ZIP 파일 선택", command=select_zip_file).pack(pady=5)


tk.Label(app, text="출력 파일 저장 위치:").pack(pady=5)
tk.Entry(app, textvariable=output_file_var, width=50).pack(padx=10)
tk.Button(app, text="저장 위치 선택", command=save_output_file).pack(pady=5)

app.mainloop()

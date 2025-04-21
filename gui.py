import tkinter as tk
from PIL import Image, ImageTk

def show_맹구():
    try:
        image = Image.open("맹구.jpg")
        photo = ImageTk.PhotoImage(image)
        image_label.config(image=photo)
        image_label.image = photo
    except FileNotFoundError:
        image_label.config(text="맹구 이미지 파일을 찾을 수 없습니다.")
    except Exception as e:
        image_label.config(text=f"맹구 이미지 로딩 오류: {e}")

def show_부리부리몬():
    try:
        image = Image.open("부리부리몬.jpg")
        photo = ImageTk.PhotoImage(image)
        image_label.config(image=photo)
        image_label.image = photo
    except FileNotFoundError:
        image_label.config(text="부리부리몬 이미지 파일을 찾을 수 없습니다.")
    except Exception as e:
        image_label.config(text=f"부리부리몬 이미지 로딩 오류: {e}")

def show_짱구():
    try:
        image = Image.open("짱구.jpg")
        photo = ImageTk.PhotoImage(image)
        image_label.config(image=photo)
        image_label.image = photo
    except FileNotFoundError:
        image_label.config(text="짱구 이미지 파일을 찾을 수 없습니다.")
    except Exception as e:
        image_label.config(text=f"짱구 이미지 로딩 오류: {e}")

def show_흰둥이():
    try:
        image = Image.open("흰둥이.jpg")
        photo = ImageTk.PhotoImage(image)
        image_label.config(image=photo)
        image_label.image = photo
    except FileNotFoundError:
        image_label.config(text="흰둥이 이미지 파일을 찾을 수 없습니다.")
    except Exception as e:
        image_label.config(text=f"흰둥이 이미지 로딩 오류: {e}")

def show_스노우맨():
    try:
        image = Image.open("스노우맨.jpg")
        photo = ImageTk.PhotoImage(image)
        image_label.config(image=photo)
        image_label.image = photo
    except FileNotFoundError:
        image_label.config(text="스노우맨 이미지 파일을 찾을 수 없습니다.")
    except Exception as e:
        image_label.config(text=f"스노우맨 이미지 로딩 오류: {e}")

# 메인 윈도우 생성
window = tk.Tk()
window.title("짱구는 못말려")

# 이미지 표시를 위한 레이블 생성
image_label = tk.Label(window)
image_label.pack(padx=10, pady=10)

# 버튼 생성
dog_button = tk.Button(window, text="맹구", command=show_맹구)
dog_button.pack(pady=5)

cat_button = tk.Button(window, text="부리부리몬", command=show_부리부리몬)
cat_button.pack(pady=5)

rabbit_button = tk.Button(window, text="짱구", command=show_짱구)
rabbit_button.pack(pady=5)

rabbit_button = tk.Button(window, text="흰둥이", command=show_흰둥이)
rabbit_button.pack(pady=5)

rabbit_button = tk.Button(window, text="스노우맨", command=show_스노우맨)
rabbit_button.pack(pady=5)

# 프로그램 실행
window.mainloop()
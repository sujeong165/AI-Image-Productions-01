import tkinter as tk
from PIL import Image, ImageTk

def show_dog():
    try:
        image = Image.open("dog.jpg")
        photo = ImageTk.PhotoImage(image)
        image_label.config(image=photo)
        image_label.image = photo
    except FileNotFoundError:
        image_label.config(text="강아지 이미지 파일을 찾을 수 없습니다.")
    except Exception as e:
        image_label.config(text=f"강아지 이미지 로딩 오류: {e}")

def show_cat():
    try:
        image = Image.open("cat.jpg")
        photo = ImageTk.PhotoImage(image)
        image_label.config(image=photo)
        image_label.image = photo
    except FileNotFoundError:
        image_label.config(text="고양이 이미지 파일을 찾을 수 없습니다.")
    except Exception as e:
        image_label.config(text=f"고양이 이미지 로딩 오류: {e}")

def show_rabbit():
    try:
        image = Image.open("rabbit.jpg")
        photo = ImageTk.PhotoImage(image)
        image_label.config(image=photo)
        image_label.image = photo
    except FileNotFoundError:
        image_label.config(text="토끼 이미지 파일을 찾을 수 없습니다.")
    except Exception as e:
        image_label.config(text=f"토끼 이미지 로딩 오류: {e}")

# 메인 윈도우 생성
window = tk.Tk()
window.title("귀여운 동물 사진")

# 이미지 표시를 위한 레이블 생성
image_label = tk.Label(window)
image_label.pack(padx=10, pady=10)

# 버튼 생성
dog_button = tk.Button(window, text="강아지", command=show_dog)
dog_button.pack(pady=5)

cat_button = tk.Button(window, text="고양이", command=show_cat)
cat_button.pack(pady=5)

rabbit_button = tk.Button(window, text="토끼", command=show_rabbit)
rabbit_button.pack(pady=5)

# 프로그램 실행
window.mainloop()
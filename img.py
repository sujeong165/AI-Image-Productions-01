from PIL import Image

# 이미지 파일 경로를 지정하세요.
image_path = "your_image.jpg"  # 실제 이미지 파일 경로로 변경해야 합니다.

try:
    # 이미지 열기
    img = Image.open(image_path)

    # 이미지 정보 출력 (형식, 크기, 색상 모드)
    print(f"이미지 형식: {img.format}")
    print(f"이미지 크기: {img.size}")
    print(f"색상 모드: {img.mode}")

    # 이미지 화면에 표시 (일부 환경에서는 작동하지 않을 수 있습니다.)
    img.show()

except FileNotFoundError:
    print(f"오류: '{image_path}' 파일을 찾을 수 없습니다.")
except Exception as e:
    print(f"오류 발생: {e}")
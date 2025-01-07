# pip install pillow 필수
# 이렇게 하면 폴더안에있는 .png 파일이 하나의 pdf로 변경
# 주의사항: 폴더 이름이 영어(ENG)로 구성되어있어야함.

import os
from PIL import Image

def png_to_pdf(folder_path, output_pdf_name):
    try:
        if not os.path.exists(folder_path):
            print(f"경로를 찾을 수 없습니다: {folder_path}")
            return

        png_files = [f for f in os.listdir(folder_path) if f.endswith('.png')]
        png_files.sort()  # 정렬

        if not png_files:
            print("PNG 파일이 없습니다.")
            return

        image_list = []
        for file in png_files:
            file_path = os.path.join(folder_path, file)
            image = Image.open(file_path).convert('RGB')
            image_list.append(image)

        output_pdf_path = os.path.join(folder_path, output_pdf_name)
        image_list[0].save(output_pdf_path, save_all=True, append_images=image_list[1:])
        print(f"PDF 파일 생성 완료: {output_pdf_path}")

    except Exception as e:
        print(f"오류 발생: {e}")

# 실행 예시
folder_path = r"C:\Users\최성욱\Desktop\aaa"
output_pdf_name = "output.pdf"
png_to_pdf(folder_path, output_pdf_name)

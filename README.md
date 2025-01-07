# celltrion

from PIL import Image
import os

def png_to_pdf(folder_path, output_pdf):
    # 폴더에서 모든 PNG 파일 가져오기
    png_files = [f for f in os.listdir(folder_path) if f.endswith('.png')]
    png_files.sort()  # 파일 이름 순서대로 정렬 (필요에 따라 변경 가능)
    
    # PNG 파일을 열어서 PDF로 변환
    images = []
    for file in png_files:
        img_path = os.path.join(folder_path, file)
        img = Image.open(img_path).convert("RGB")  # RGB 모드로 변환
        images.append(img)
    
    if images:
        # 첫 번째 이미지를 기준으로 PDF 생성
        images[0].save(output_pdf, save_all=True, append_images=images[1:])
        print(f"PDF가 성공적으로 생성되었습니다: {output_pdf}")
    else:
        print("PNG 파일이 폴더에 없습니다.")

# 사용 예시
folder_path = "path/to/png/folder"  # PNG 파일이 있는 폴더 경로
output_pdf = "output.pdf"           # 생성할 PDF 파일 이름
png_to_pdf(folder_path, output_pdf)

import os

def create_folders(base_path):
    try:
        # 2016년부터 2020년까지 폴더 생성
        for year in range(2016, 2021):
            folder_name = f"{year}년"
            folder_path = os.path.join(base_path, folder_name)

            # 폴더가 없으면 생성
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
                print(f"폴더 생성: {folder_path}")
            else:
                print(f"이미 존재하는 폴더: {folder_path}")

    except Exception as e:
        print(f"오류 발생: {e}")

# 실행 예시
base_path = r"C:\Users\최성욱\Desktop\new"  # 원하는 경로로 변경
create_folders(base_path)

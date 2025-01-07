# 사용방법 1. year이라는 새로운 폴더를 만든다.
# 사용방법 2. 연도를 포함하는 폴더를 year이라는 폴더에 모두 넣는다.
# 코드를 실행한다.

# 코드 내용. 현재는 2016년부터 2021년까지의 연도를 대상으로,  해당 연도를 포함하는 폴더를 year이라는 폴더에 모두 넣으면
# year폴더안에 모든 파일은 사라지며, new 폴더가 새로 생깁니다.
# new 폴더안에는 2016년~2021년까지의 모든 파일이 새롭게 생기고, 기존에 연도를 포함하는 폴더는 해당하는 연도에 맞게 자동 정리됩니다.

import os
import shutil

def classify_files_and_folders_by_year(base_path):
    try:
        # NEW 폴더 생성
        new_base_path = os.path.join(base_path, "NEW")
        if not os.path.exists(new_base_path):
            os.makedirs(new_base_path)
            print(f"NEW 폴더 생성: {new_base_path}")

        # 연도별 폴더 리스트 생성
        years = [str(year) for year in range(2016, 2021)]
        year_folders = {year: os.path.join(new_base_path, year + "년") for year in years}

        # 각 연도 폴더 생성 (NEW 안에)
        for year, folder_path in year_folders.items():
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
                print(f"폴더 생성: {folder_path}")

        # base_path 내부 파일 및 폴더 확인
        for item_name in os.listdir(base_path):
            item_path = os.path.join(base_path, item_name)

            # NEW 폴더는 건너뛰기
            if item_name == "NEW":
                continue

            # 파일 또는 폴더 이름에 연도가 포함된 경우
            for year in years:
                if year in item_name:
                    target_folder = year_folders[year]
                    target_path = os.path.join(target_folder, item_name)

                    # 파일 이동
                    if os.path.isfile(item_path):
                        shutil.move(item_path, target_path)
                        print(f"파일 이동: {item_path} -> {target_path}")

                    # 폴더 이동
                    elif os.path.isdir(item_path):
                        shutil.move(item_path, target_folder)
                        print(f"폴더 이동: {item_path} -> {target_folder}")
                    break

    except Exception as e:
        print(f"오류 발생: {e}")

# 실행 예시
base_path = r"C:\Users\최성욱\Desktop\year"  # year 폴더 경로
classify_files_and_folders_by_year(base_path)

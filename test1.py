import os

# 적재할 파일이 있는 디렉토리 경로
dir_path = "path/to/your/directory"

# 적재된 파일들의 목록을 저장할 리스트
file_list = []

# 디렉토리 내의 파일 목록을 검색하여 리스트에 저장
for file_name in os.listdir(dir_path):
    file_path = os.path.join(dir_path, file_name)
    # 파일인 경우 리스트에 추가
    if os.path.isfile(file_path):
        file_list.append(file_path)

# 파일 목록 출력
print("적재된 파일 목록:")
for file_path in file_list:
    print(file_path)

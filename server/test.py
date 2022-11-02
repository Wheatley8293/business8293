# # csv 파일을 데이터베이스에 집어넣기 위한 실행파일
# # 입력 알고리즘에 해당하기에 한번 실행한 뒤 주석처리를 해놓은 것. 안 그러면 연속으로 이어서 입력됨.
# # 출처 : https://walkingplow.tistory.com/44?category=981358

# import csv
# import os
# import django

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
# # .settings 앞에 들어가는 건 '프로젝트와 같은 앱 폴더 이름'.
# # 아래의 모델 임포트 전에 적어야 한다.

# django.setup()
# from emhospital.models import EmHospital

# # 클론코딩. db.sqlite3 배치와 비교하면서 아래 코드를 봐야 이해할 수 있음.
# with open('./24병원.csv') as csv_file_sub_categories:
#     rows = csv.reader(csv_file_sub_categories)
#     next(rows, None)
#     for row in rows:
#         EmHospital.objects.create(
#             HosGoo = row[0],
#             HosDong = row[1],
#             HosName = row[2],
#             AlwaysTime = int(row[3]),
#             HosAddress = row[4],
#             HosSNA = row[5],
#             Latitude = float(row[6]),
#             Longitude = float(row[7]),
#         )

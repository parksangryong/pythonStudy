import zipfile

# 파일 압축
# compression 압축 방법 선택 (기본값: ZIP_STORED)
# ZIP_STORED: 압축 안함 (파일 그대로 저장)
# ZIP_DEFLATED: 압축 함 (파일 압축, 압축률 낮고 빠름)
# ZIP_BZIP2: 압축 함 (파일 압축, 압축률 높고 느림)
# ZIP_LZMA: 압축 함 (파일 압축, 압축률 높고 느림)

# compresslevel 압축 수준 선택 (기본값: 6)
# 0: 압축 안함
# 1: 최저 압축률, 최고 속도
# 9: 최고 압축률, 최저 속도
with zipfile.ZipFile('myTextFiles.zip', 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zip:
    zip.write('a.txt')
    zip.write('b.txt')
    zip.write('c.txt')

# 파일 압축 해제
with zipfile.ZipFile('myTextFiles.zip', 'r') as zip:
    zip.extractall()

# 특정 파일만 압축 해제
with zipfile.ZipFile('myTextFiles.zip', 'r') as zip:
    zip.extract('a.txt')

import sys

src = sys.argv[1]
dst = sys.argv[2]

f = open(src, 'r')
tab_content = f.read()
f.close()

# 탭 개수 확인
tab_count = tab_content.count('\t')
print(f"발견된 탭 개수: {tab_count}")

space4_content = tab_content.replace('\t', ' '*4)

f = open(dst, 'w')
f.write(space4_content)
f.close()

print(f"변환 완료: {src} -> {dst}")
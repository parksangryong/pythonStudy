def getTotalPage(m, n):
    result = 0
    if m % n == 0:
        result = m // n
    else:
        result = m // n + 1
        
    print(f'총 {result} 페이지가 있습니다.')

getTotalPage(5, 10)
getTotalPage(15, 10)
getTotalPage(25, 10)
getTotalPage(30, 10)
getTotalPage(153, 25)
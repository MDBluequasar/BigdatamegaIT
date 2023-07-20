

call = 15 # 리스트 길이

n = 0
an = 3 ### counting 하고 싶은 수

line = []

poly = []

while True:
    if call > 0 :
        if call % 2:
          line.append(str(call))
          poly = ''.join(line)
          answer = poly.count(str(an))

    else:
       break

    call -= 1
# answer = poly.count(str(an))

print(answer)      

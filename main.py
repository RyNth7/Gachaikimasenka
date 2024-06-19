import random
cl = ["돌린다", "돌리지 않는다"]
while True:
  try:
    N = int(input("최솟값을 입력하세요\n: "))
  except:
    print("정수가 아닙니다. 다시 시도하세요.")
    continue
  if N > 0:
    break
  else:
    print("입력값은 음수가 될 수 없습니다. 다시 시도하세요.")
    continue
    
while True:
  try:
    M = int(input("최댓값을 입력하세요\n: "))
  except:
    print("정수가 아닙니다. 다시 시도하세요.")
    continue
  if N < M:
    break
  else:
    print("최댓값은 최솟값보다 작아야 합니다. 다시 시도하세요")
    continue
    
while True:
  try:
    F = int(input("마음에 드는 숫자 한 개를 입력하세요\n"))
  except:
    print("정수가 아닙니다. 다시 시도하세요.")
    continue
  if F > 0 and F < 10:
    break
  else:
    print("입력 범위를 초과했습니다. 0~10의 정수를 입력하세요.")
    continue
    
Np = random.randrange(N, M)
Mp = random.randrange(N, M)
Kl = random.choices(cl, weights = [Np, Mp], k = 10)

print()
print("="*30 + "\n결과는...\n\n당신은 가챠를 %s\n\n감사합니다.\n"%Kl[F] + "="*30)

print("복약 시간 확인 프로그램")

while True:
  name = input("환자 이름을 입력하세요:")
  medicine = input("약 이름을 입력하세요:")
  time = input("약을 먹을 시간을 입력하세요")

  print("환자 이름:", name)
  print("약 이름", medicine)
  print("복용 시간:", time)

  print("복약 시간이 되었습니다.")
  answer = input("약을 먹었나요? (예/아니오)")

  if answer == "예":
    print("약 복용이 확인되었습니다.")

  else:
    print("아직 약을 먹지 않았습니다.")
    print("복용 여부를 다시 확인하세요.")

  print("복약 확인이 끝났습니다.")

  finish = input("프로그램을 끝낼까요? (예/아니오)")
  if finish == "예":
    break

  else:
    print("다음 환자를 확인합니다.")
print("프로그램을 종료합니다.")
print("이용해주셔서 감사합니다.")

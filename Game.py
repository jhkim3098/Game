import random

def guess_number():
    # 1부터 100 사이의 난수 생성
    target_number = random.randint(1, 100)
    attempts = 0

    print("숫자 맞추기 게임을 시작합니다! 1부터 100 사이의 숫자를 맞춰보세요.")

    while True:
        user_guess = int(input("숫자를 입력하세요: "))

        attempts += 1

        if user_guess < target_number:
            print("너무 작습니다!")
        elif user_guess > target_number:
            print("너무 큽니다!")
        else:
            print(f"축하합니다! {target_number}를 {attempts}번 만에 맞추셨습니다!")
            break

if __name__ == "__main__":
    guess_number()

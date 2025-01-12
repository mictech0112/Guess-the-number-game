import sys
import random

# 最小値を入力してもらう
sys.stdout.buffer.write(b'Enter the minimum value (n): ')
sys.stdout.flush()
min_value = int(sys.stdin.buffer.readline().decode().strip())

# 最大値を入力してもらう
sys.stdout.buffer.write(b'Enter the maximum value (m): ')
sys.stdout.flush()
max_value = int(sys.stdin.buffer.readline().decode().strip())

# 最小値以上から最大値以下の整数をランダムに生成する
random_number = random.randint(min_value, max_value)

# 10回までの試行でユーザーが正しい数を当てることを試みる
for attempt in range(10):
    sys.stdout.buffer.write(b'Attempt ' + str(attempt + 1).encode() + b': Guess the generated random number: ')
    sys.stdout.flush()
    guess_number = int(sys.stdin.buffer.readline().decode().strip()) 

    if random_number == guess_number:
        print('Congratulations on guessing the correct number!')
        break
    else:
        print('Sorry, try again...')

else:
    print('Sorry, you have reached the maximum number of attempts. The correct number was:', random_number)


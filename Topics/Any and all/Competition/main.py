check = all([True, True, 0, 1, True])

if check:
    status = 'winner'
else:
    status = 'loser'

if status == 'winner':
    winning_sum = 100
else:
    winning_sum = 10
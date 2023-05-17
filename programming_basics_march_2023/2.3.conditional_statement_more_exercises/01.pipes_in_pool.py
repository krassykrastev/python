volume_in_liters = int(input())
debit_pipe1_per_hr = int(input())
debit_pipe2_per_hr = int(input())
hrs_worker_is_gone = float(input())

volume_pipe1 = debit_pipe1_per_hr * hrs_worker_is_gone
volume_pipe2 = debit_pipe2_per_hr * hrs_worker_is_gone
total_volume = volume_pipe1 + volume_pipe2
pool_full = (total_volume / volume_in_liters) * 100
pipe1_filled = (volume_pipe1 / total_volume) * 100
pipe2_filled = (volume_pipe2 / total_volume) * 100
overflow_liters = total_volume - volume_in_liters

if total_volume <= volume_in_liters:
    print(f'The pool is {pool_full:.2f}% full. Pipe 1: {pipe1_filled:.2f}%. Pipe 2: {pipe2_filled:.2f}%.')

else:
    print(f'For {hrs_worker_is_gone:.2f} hours the pool overflows with {overflow_liters:.2f} liters.')

V_pool_volume_in_liters = int(input())
P1_flow_rate_of_the_first_pipe_per_hour = int(input())
P2_two_flow_rate_of_the_second_pipe_per_hour = int(input())
H_the_hours_the_worker_is_absent = float(input())

pipe_one_for_all_hours = P1_flow_rate_of_the_first_pipe_per_hour * H_the_hours_the_worker_is_absent
pipe_two_for_all_hours = P2_two_flow_rate_of_the_second_pipe_per_hour * H_the_hours_the_worker_is_absent

filled_volume = pipe_two_for_all_hours + pipe_one_for_all_hours
filled_volume_in_percent = ((pipe_two_for_all_hours + pipe_one_for_all_hours) / V_pool_volume_in_liters) * 100
volume_for_pipe_one = (pipe_one_for_all_hours / filled_volume) * 100
volume_for_pipe_two = (pipe_two_for_all_hours / filled_volume) * 100
diff = filled_volume - V_pool_volume_in_liters
if filled_volume <= V_pool_volume_in_liters:
    print(f"The pool is {filled_volume_in_percent}% full. Pipe 1: {volume_for_pipe_one:.2f}%. Pipe 2: {volume_for_pipe_two:.2f}%.")
else:
    print(f"For {H_the_hours_the_worker_is_absent:.2f} hours the pool overflows with {diff:.2f} liters.")


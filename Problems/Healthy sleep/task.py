min_sleep, max_sleep, had_sleep = int(input()), int(input()), int(input())

print("Normal") if min_sleep <= had_sleep <= max_sleep else (print("Deficiency") if had_sleep < min_sleep else print("Excess"))

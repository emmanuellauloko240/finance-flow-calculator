total_pool = 10000
development = total_pool * 0.80
safety_allocation = development - total_pool

print(f"Allocated to Development: {development}")
print(f"safety_allocation: {safety_allocation}")
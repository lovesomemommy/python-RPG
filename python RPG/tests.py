from main import limit, feed, play, sleep, time_passes, get_state

pet = {"имя": "Лео", "сытость": 50, "настроение": 50, "энергия": 50}
feed(pet)
assert pet["сытость"] == 80
play(pet)
assert pet["настроение"] == 75
assert pet["энергия"] == 30
time_passes(pet)
assert pet["сытость"] == 70
assert get_state(pet) == "довольный"

assert limit(150) == 100
assert limit(-20) == 0

tired = {"имя": "Лео", "сытость": 50, "настроение": 50, "энергия": 10}
play(tired)
assert tired["настроение"] == 50
assert tired["энергия"] == 10
assert get_state(tired) == "сонный"

full = {"имя": "Лео", "сытость": 90, "настроение": 50, "энергия": 90}
feed(full)
sleep(full)
assert full["сытость"] == 100
assert full["энергия"] == 100

print("Все проверки пройдены")

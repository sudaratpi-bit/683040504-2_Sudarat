"""
Sudarat Pitakwongroj
683040504-2
P1
"""


from room import Bedroom, Kitchen

bedroom = Bedroom(12, 10, bed_size=5)
print(bedroom.describe_room())
print("Bedroom area:", bedroom.calculate_area())
print("Bed size:", bedroom.bed_size, "ft")
print("Recommended lighting:", bedroom.get_recommended_lighting(), "lumens/sq ft")
print()

kitchen1 = Kitchen(15, 12, has_island=True)
print(kitchen1.describe_room())
print("Kitchen area:", kitchen1.calculate_area())
print("Recommended lighting:", kitchen1.get_recommended_lighting(), "lumens/sq ft")

island, wall = kitchen1.calculate_counter_space()
print("Island counter area:", island)
print("Wall counter area:", wall)
print()

kitchen2 = Kitchen(15, 12, has_island=False)
print("Kitchen without island:")
island, wall = kitchen2.calculate_counter_space()
print("Island counter area:", island)
print("Wall counter area:", wall)
from game import Room

gold = Room("gold", """This room has gold in it you can grab. There's a
            door to the north.""")

assert_equal(gold.name, "GoldRoom")
assert_equal(gold.paths, {})

print(gold.name)
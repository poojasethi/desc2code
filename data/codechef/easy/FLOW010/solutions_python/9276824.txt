T = int(raw_input())
ships = {'b' : 'BattleShip', 'c': 'Cruiser', 
         'd': 'Destroyer', 'f': 'Frigate'}
for i in range(T):
    s = raw_input()
    print ships[s.lower()]

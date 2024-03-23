from src.equipment.skills import Skills

spore_bomb = Skills(DMG=68)
print(f"Trigger an explosion on the target 2 time(s), each time dealing {spore_bomb.DMG}% DMG.")

shroom_cap = Skills(DMG=194)
print(f"Summon a Mushroom Cap, dealing {shroom_cap.DMG}% AoE DMG.")

spore_barrage = Skills(DMG=33.1)
print(f"Throw 5 Spore(s), each dealing {spore_barrage.DMG}% DMG.")

boulder_impact = Skills(DMG=76)
print(f"Summon a Giant Rock, dealing {boulder_impact.DMG}% DMG to the target every second, lasting for 5 seconds.")

thorn_thicket = Skills(DMG=53, Slow=40)
print(f"Set up 1 trap(s), dealing {thorn_thicket.DMG}% DMG every second and slowing the target by {thorn_thicket.Slow}%, lasting for 5 seconds")

lead_the_charge = Skills(DMG=438, Increase_Basic_Attack=30)
print(f"Deal {lead_the_charge.DMG}% DMG to the nearest target and inncrease Basic Attack DMG by {lead_the_charge.Increase_Basic_Attack}% for 5 seconds")


from pydantic import BaseModel
from typing import Optional

class Skills(BaseModel):
    DMG: int
    Slow: Optional[int]
    Increase_Basic_Attack: Optional[int]
    Imprison: Optional[int]
    Increase_Attack_Speed: Optional[int]
    Heal: Optional[int]
    Shield: Optional[int]
    Reduce_Attack: Optional[int]
    Reduce_Attack_Speed: Optional[int]
    Increase_Pal_DMG: Optional[int]
    Increase_Skill_DMG: Optional[int]
    Disarm: Optional[int]
    Stun: Optional[int]
    Increase_DMG_Recieved: Optional[int]
    Instant_Defeat: Optional[int]
    DMG_Immunity: Optional[int]
    Lose_Max_Health_Per_Second: Optional[int]
    Clone: Optional[int]
    Basic_attack_DMG_RES: Optional[int]
    ATK_Bonus: Optional[int]
    Vulnerability: Optional[int]
    Inncrease_Crit_Rate: Optional[int]
    Increase_Crit_DMG: Optional[int]
    Increase_Skill_Crit_Rate: Optional[int]
    Increase_Skill_Crit_DMG: Optional[int]    
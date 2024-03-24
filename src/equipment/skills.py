from pydantic import BaseModel
from typing import Optional

class Skills(BaseModel):
    DMG: float
    Slow: Optional[int] = None
    Increase_Basic_Attack: Optional[int] = None
    Imprison: Optional[int] = None
    Increase_Attack_Speed: Optional[int] = None
    Heal: Optional[int] = None
    Shield: Optional[int] = None
    Reduce_Attack: Optional[int] = None
    Reduce_Attack_Speed: Optional[int] = None
    Increase_Pal_DMG: Optional[int] = None
    Increase_Skill_DMG: Optional[int] = None
    Disarm: Optional[int] = None
    Stun: Optional[int] = None
    Increase_DMG_Recieved: Optional[int] = None
    Instant_Defeat: Optional[int] = None
    DMG_Immunity: Optional[int] = None
    Lose_Max_Health_Per_Second: Optional[int] = None
    Clone: Optional[int] = None
    Basic_attack_DMG_RES: Optional[int] = None
    ATK_Bonus: Optional[int] = None
    Vulnerability: Optional[int] = None
    Inncrease_Crit_Rate: Optional[int] = None
    Increase_Crit_DMG: Optional[int] = None
    Increase_Skill_Crit_Rate: Optional[int] = None
    Increase_Skill_Crit_DMG: Optional[int] = None 
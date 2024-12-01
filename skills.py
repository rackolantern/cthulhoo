class Skill:
    maxSkill = None
    halfSkill = None
    fifthSkill = None

def __init__(self, skill, halfSkill, fifthSkill):
    self.maxSkill = skill
    self.halfSkill = skill / 2
    self.fifthSkill = skill / 4

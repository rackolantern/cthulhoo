from skills import Skill

class Character():
    name = None
    strStat = None
    dexStat = None
    intStat = None
    conStat = None
    appStat = None
    powStat = None
    sizStat = None
    eduStat = None
    
def __init__(self, name, strInput, dexInput, intInput, conInput, appInput, powInput, sizInput, eduInput):
    self.name = name
    self.strStat = Skill(strInput)
    self.dexStat = dexInput
    self.intStat = intInput
    self.conStat = conInput
    self.appStat = appInput
    self.powStat = powInput
    self.sizStat = sizInput
    self.eduStat = eduInput


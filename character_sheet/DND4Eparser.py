import xml.dom.minidom
from pprint import pprint

# dom = xml.dom.minidom.parse("ImmeralLvl3.dnd4e")

def getText(nodes):
  text = []
  for node in nodes:
    if node.nodeType == node.TEXT_NODE:
      text.append(''.join([i if ord(i) < 128 else ' ' for i in node.data]).strip())
  return ''.join(text)

def getScoreAttrib(node):
  return int(getText(node.attributes["score"].childNodes))

def getNameAttrib(node):
  return getText(node.attributes["name"].childNodes)

def getValueAttrib(node):
  return getText(node.attributes["value"].childNodes)

def handleDetails(details):
  detail = {}
  for node in details.childNodes:
    if node.nodeType != node.TEXT_NODE:
      detail[node.nodeName] = getText(node.childNodes)
  return detail

def handleAbilities(abilities):
  ability = {}
  for node in abilities.childNodes:
    if node.nodeType != node.TEXT_NODE:
      ability[node.nodeName] = getScoreAttrib(node)
  return ability

def handlePowerStats(powerstats):
  power_list = []
  # Iterate through Power nodes
  for powers in powerstats.childNodes:
    if powers.nodeType != powers.TEXT_NODE:
      power = []
      # Iterate through the specifics of the base power
      base_power = {}
      base_power["name"] = getNameAttrib(powers)
      for specifics in powers.getElementsByTagName("specific"):
        base_power[getNameAttrib(specifics)] = getText(specifics.childNodes)
      power.append(base_power)
      # Iterate the weapon listings for powers
      for weapons in powers.getElementsByTagName("Weapon"):
        if weapons.nodeType != weapons.TEXT_NODE:
          weapon = {}
          weapon["name"] = getNameAttrib(weapons)
          for node in weapons.childNodes:
            if node.nodeType != node.TEXT_NODE:
              weapon[node.tagName] = getText(node.childNodes)
          power.append(weapon)
      power_list.append(power)
  return power_list

def handleStats(stats):
  stat_dict = {}
  for stat in stats:
    if stat.nodeType != stat.TEXT_NODE:
      stat_dict[getNameAttrib(stat.getElementsByTagName("alias")[0])] = getValueAttrib(stat)
  return stat_dict
          

if __name__ == "__main__":

  print "Details:"
  pprint(handleDetails(dom.getElementsByTagName("Details")[0]))

  print "\nStats:"
  pprint(handleStats(dom.getElementsByTagName("Stat")))

  print "\nAbilities:"
  pprint(handleAbilities(dom.getElementsByTagName("AbilityScores")[0]))

  print "\nPowers:"
  for each in handlePowerStats(dom.getElementsByTagName("PowerStats")[0]):
    pprint(each)


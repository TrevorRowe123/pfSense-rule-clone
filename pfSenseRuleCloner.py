import xml.etree.ElementTree as ET
from copy import deepcopy

clonedInt = 'wan'
newInt = 'opt1'
config = ET.parse("filter.xml")
configRoot = config.getroot()

def isClonedInt(cloneInt, rule):
    ruleInt = rule.find('interface')
    if ruleInt == None:
        print('false')
        return False
    return ruleInt.text == cloneInt

def cloneRule(clone2Int, rule): #need to "pass rule by value", not default behavior
    newRule = deepcopy(rule)
    newRule.find('interface').text = clone2Int
    return newRule

for rule in configRoot.findall('rule'):
    if isClonedInt(clonedInt, rule):
        newRule = cloneRule(newInt, rule)
        configRoot.append(newRule)
        
config.write('out.xml')
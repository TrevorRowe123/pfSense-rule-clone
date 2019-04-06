import xml.etree.ElementTree as ET
from sys import argv, exit
from copy import deepcopy

if len(argv) > 1: xmlPath = argv[1]
else: xmlPath = input("Path to pfSense config file: ")


config = ET.parse(xmlPath)
configRoot = config.getroot()

def isClonedInt(cloneInt, rule):
    ruleInt = rule.find('interface')
    if ruleInt == None:
        return False
    return ruleInt.text == cloneInt

def cloneRule(clone2Int, rule):
    newRule = deepcopy(rule)
    newRule.find('interface').text = clone2Int
    return newRule

def printMenu():
    print("Select an option here:")
    print("1: Display pfSense interface names/friendly names")
    print("2: Copy rules between interfaces")
    print("3: Write changes to output file and exit")
    print("4: Exit")
    return input(">")

def intClone():
    clonedInt = input("Interface to clone from (pfSense name): ")
    newInt = input("Interface to clone to (pfSense name): ")
    filterElement = configRoot.find("filter")
    for rule in filterElement.findall('rule'):
        if isClonedInt(clonedInt, rule):
            newRule = cloneRule(newInt, rule)
            filterElement.append(newRule)
            
def friendlyNames():
    interfaces = configRoot.find("interfaces")
    print("Friendly name:   pfSense Name")
    print("-----------------------------")
    for interface in interfaces:
        print(interface.find("descr").text + ":   " + interface.tag)

action = "0"
while action != "4":
    action = printMenu()
    if action == "1":
        friendlyNames()
        input("Press enter to continue...")
    elif action == "2":
        intClone()
    elif action == "3":
        config.write('out.xml')

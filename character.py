import PyPDF2
from pathlib import Path
sheetNeededNumbers = ['Initiative','AC','HPMax','STR','CON','DEX','INT',
    'WIS','CHA','ST Strength','ST Dexterity', 'ST Intelligence','ST Constitution',
    'ST Wisdom', 'ST Charisma','Speed']
sheetNeededStrings = ['CharacterName']
neededkeys = sheetNeededNumbers+sheetNeededStrings
sheetWeaponSkills = [['Wpn Name','Wpn1 AtkBonus','Wpn1 Damage'],['Wpn Name 2','Wpn2 AtkBonus','Wpn2 Damage'],['Wpn Name 3','Wpn3 AtkBonus','Wpn3 Damage']]

def process_character(pdf):
    reader = PyPDF2.PdfFileReader(pdf,strict=False)
    try:
        forms = reader.getFormTextFields()
    except:
        return 'This is the wrong pdf.'
    character = {}
    checksheet = catch_wrong_sheet(forms)
    if checksheet != None:
        return checksheet
    processname = process_name(forms)
    if processname[0] != None:
        return checkname[0]
    character.update(processname[1])
    processNeededNumbers = process_needed_numbers(forms)
    if len(processNeededNumbers[0]) != 0:
        return "{} have not been entered correctly. please fix sheet and try again".format(",".join(processNeededNumbers[0]))
    character.update(processNeededNumbers[1])
    character.update(process_weapons(forms))
    return character

def catch_wrong_sheet(forms):
    for i in neededkeys:
        if i not in forms:
            return 'This is the wrong sheet.'
    return None


def process_name(forms):
    errorOutput= None
    if forms['CharacterName']== None:
        errorOutput = 'This character needs a name.'
    return (errorOutput, {'charactername': forms['CharacterName']})


def process_needed_numbers(forms):
    errorOutput=[]
    appendToCharacter = {}
    for i in sheetNeededNumbers:
        try:
            appendToCharacter.update({i.lower():int(forms[i])})
        except:
            errorOutput.append(i)
    return (errorOutput,appendToCharacter)

def process_weapons(forms):
    weapons= {}
    for weapon in sheetWeaponSkills:
        if forms[weapon[0]]== None:
            continue
        weapons.update({forms[weapon[0]]:(forms[weapon[1]],forms[weapon[2]])})
    return weapons

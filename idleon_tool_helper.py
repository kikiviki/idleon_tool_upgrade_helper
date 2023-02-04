import json
import pandas as pd

f = open('json_export.json')
data = json.load(f)

# set this to true if you want to use the names below
use_names = False

#change the character names to your character names, in order
character_names_index = ['player1',
                         'player2',
                         'player3',
                         'player4',
                         'player5',
                         'player6',
                         'player7',
                         'player8',
                         'player9',
                         'player10'
                         ]

tool_name_dict = {
                'EquipmentTools1' : 'Old Pickaxe',
                'EquipmentTools2' : 'Copper Pickaxe',
                'EquipmentTools3' : 'Iron Pickaxe',
                'EquipmentTools5' : 'Gold Pickaxe',
                'EquipmentTools6' : 'Platinum Pickaxe',
                'EquipmentTools7' : 'Dementia Pickaxe',
                'EquipmentTools8' : 'Lustre Pickaxe',
                'EquipmentTools11' : 'Void Pickaxe',
                'EquipmentTools10' : 'Poopy Pickaxe',
                'EquipmentTools12' : 'Starfire Pickaxe',
                'EquipmentTools9' : 'Dreadlo Pickaxe',
                'EquipmentToolsHatchet3': 'Copper Chopper',
                'EquipmentToolsHatchet1': 'Iron Hatchet',
                'EquipmentToolsHatchet4': 'Plat Hatchet',
                'EquipmentToolsHatchet2' : 'Golden Axe',
                'EquipmentToolsHatchet5': 'Dementia Dicer',
                'EquipmentToolsHatchet7': 'Void Imperium Axe',
                'EquipmentToolsHatchet6': 'Lustre Loggerr',
                'EquipmentToolsHatchet8': 'Starfire Hatchet',
                'EquipmentToolsHatchet9': 'Dreadlo Eviscerator',
                'FishingRod2' : 'Copper Rod',
                'FishingRod3': 'Iron Rod',
                'FishingRod4': 'Gold Rod',
                'FishingRod5': 'Platinum Rod',
                'FishingRod6': 'Dementia Rod',
                'FishingRod7': 'Void Rod',
                'FishingRod8': 'Lustre Rod',
                'FishingRod9': 'Starfire Rod',
                'FishingRod10': 'Dreadlo Rod',
                'CatchingNet2' : 'Copper Net',
                'CatchingNet3': 'Reinforced Net',
                'CatchingNet4': 'Golden Net',
                'CatchingNet5': 'Platinum Net',
                'CatchingNet6': 'Dementia net',
                'CatchingNet7': 'Void Net',
                'CatchingNet8': 'Lustre Net',
                'CatchingNet9': 'Starfire Net',
                'CatchingNet10': 'Dreadlo Net',
                'TrapBoxSet1' : 'Carboard Traps',
                'TrapBoxSet2' : 'Silkskin Traps',
                'TrapBoxSet3': 'Wooden Traps',
                'TrapBoxSet4': 'Natural Traps',
                'TrapBoxSet5': 'Steel Traps',
                'TrapBoxSet6': 'Meaty Traps',
                'TrapBoxSet7': 'Royal Traps',
                'TrapBoxSet8': 'Egalitarian Royal Traps',
                'WorshipSkull1' : 'Wax Skull',
                'WorshipSkull2' : 'Ceramic Skull',
                'WorshipSkull3' : 'Horned Skull',
                'WorshipSkull4' : 'Prickle Skull',
                'WorshipSkull5' : 'Manifested Skull',
                'WorshipSkull6' : 'Glauss Skull',
                'WorshipSkull7' : 'Luciferian Skull',
                'WorshipSkull9' : 'Dreadnaught Skull',

                'Blank' : 'Blank',
                'None' : 'None'


}


max_level_tools = [
    'WorshipSkull9',
    'TrapBoxSet8',
    'EquipmentTools9',
    'CatchingNet10',
    'EquipmentToolsHatchet9',
    'FishingRod10'
]
tool_level_dict = {
                'EquipmentTools1' : 1,
                'EquipmentTools2' : 3,
                'EquipmentTools3' : 8,
                'EquipmentTools5' : 15,
                'EquipmentTools6' : 25,
                'EquipmentTools7' : 37,
                'EquipmentTools8' : 55,
                'EquipmentTools11' : 45,
                'EquipmentTools12' : 65,
                'EquipmentTools9' : 70,
                'EquipmentTools10' : 15,
                'EquipmentToolsHatchet3': 4,
                'EquipmentToolsHatchet1': 8,
                'EquipmentToolsHatchet4': 20,
                'EquipmentToolsHatchet2': 15,
                'EquipmentToolsHatchet5': 25,
                'EquipmentToolsHatchet7': 30,
                'EquipmentToolsHatchet6': 40,
                'EquipmentToolsHatchet8': 50,
                'EquipmentToolsHatchet9': 65,
                'FishingRod2' : 4,
                'FishingRod3': 9,
                'FishingRod4': 15,
                'FishingRod5': 25,
                'FishingRod6': 33,
                'FishingRod7': 40,
                'FishingRod8': 45,
                'FishingRod9': 50,
                'FishingRod10': 60,
                'CatchingNet2': 4,
                'CatchingNet3': 10,
                'CatchingNet4': 15,
                'CatchingNet5': 20,
                'CatchingNet6': 25,
                'CatchingNet7': 30,
                'CatchingNet8': 40,
                'CatchingNet9': 50,
                'CatchingNet10': 70,
                'TrapBoxSet1' : 1,
                'TrapBoxSet2': 5,
                'TrapBoxSet3': 15,
                'TrapBoxSet4': 25,
                'TrapBoxSet5': 35,
                'TrapBoxSet6': 40,
                'TrapBoxSet7': 48,
                'TrapBoxSet8': 60,
                'WorshipSkull1': 1,
                'WorshipSkull2': 10,
                'WorshipSkull3': 25,
                'WorshipSkull4': 35,
                'WorshipSkull5': 40,
                'WorshipSkull6': 50,
                'WorshipSkull7': 60,
                'WorshipSkull9': 70,

                'Blank' : 0,

                }

skills_equip_slot_translation_index = [
                            'mining',
                            'chopping',
                            'fishing',
                            'catching',
                            'trapping',
                            'worship']

skills_content_keys = { 'level' : 0,
                         'mining' : 1,
                         'smithing' : 2,
                         'chopping' : 3,
                         'fishing' : 4,
                         'alchemy' : 5,
                         'catching' : 6,
                         'trapping' : 7,
                         'construction' : 8,
                         'worship' : 9,
                         'unknown_1' : 10,
                         'breeding' : 11,
                         'research' : 12,
                         'sailing' : 13,
                         'divinity' : 14,
                         'gaming': 15
                         }


def mainroutine():
    equip_header_dict = []
    equip_content_dict = []
    skills_header_dict = []
    skills_content_dict = []

    for each_entry in data:
        if 'EquipOrder_' in each_entry:
            equip_header_dict.append(each_entry)
        if 'Lv0_' in each_entry:
            skills_header_dict.append(each_entry)

    # sort the headers so they are in order
    equip_header_dict.sort()
    skills_header_dict.sort()

    #print(equip_header_dict)

    # add contents to the equip contents dict
    for each_entry in data:
        if each_entry in equip_header_dict:
            equip_content_dict.append([each_entry, data[each_entry]])
    # re-sort
    equip_content_dict.sort()

    # add contents to the skills contents dict
    for each_entry in data:
        if each_entry in skills_header_dict:
            skills_content_dict.append([each_entry, data[each_entry]])
    # re-sort
    skills_content_dict.sort()

    # we want user0 => list # 1 (the second list) which is equipment

    output_dict = []
    for i in range(10): #iterate through all charcters
        #print(character_names_index[i])
        #print(equip_content_dict[i][1])
        user_equipment = equip_content_dict[i][1][1] # get the equipment json from
        #print(character_names_index[i], user_equipment, (skills_content_dict[i][1]))
        if use_names:
            print(character_names_index[i])
        else:
            print("Character #:", i)
        character_skill_array = (skills_content_dict[i][1])


        character_skill_type_level_array = []
        for skill_id in skills_equip_slot_translation_index:
            skill_id_ref_location = (skills_content_keys[skill_id])
            my_skill_level = character_skill_array[skill_id_ref_location]
            #print('skill type:', skill_id, '  skill level: ', my_skill_level)
            character_skill_type_level_array.append([skill_id,my_skill_level])
        # loop through the equipment slots
        # pull -> slot id, equip id, equip name, equip skill req, curr skill

        for j in range(6):
            current_slot = str(j)
            equipment_id = user_equipment[current_slot]
            equipment_name = tool_name_dict[equipment_id]
            equipment_skill_req = tool_level_dict[equipment_id]
            tool_skill_type = character_skill_type_level_array[j][0]
            tool_skill_level = character_skill_type_level_array[j][1]
            suggested_tool = get_next_best_tool(equipment_id, tool_skill_level, tool_skill_type)

            if suggested_tool == equipment_name or suggested_tool == 'BIS':
                character_string = 'Slot_{slot_id} : {equipment_name} [{skill_name}] || Skill: [{current_skill_level}] :: Best Current '.format(
                slot_id=j+1,
                equipment_name=equipment_name,
                skill_name=tool_skill_type,
                current_skill_level=tool_skill_level,
                suggested_tool=suggested_tool
                )
            elif suggested_tool == 'None':
                character_string = 'Slot_{slot_id} : {equipment_name} [{skill_name}] || Skill: [{current_skill_level}] :: Skill Too Low'.format(
                    slot_id=j+1,
                    equipment_name=equipment_name,
                    skill_name=tool_skill_type,
                    current_skill_level=tool_skill_level,
                    suggested_tool=suggested_tool
                )
            else:
                character_string = 'Slot_{slot_id} : {equipment_name} [{skill_name}] || Skill: [{current_skill_level}] :: Suggested > {suggested_tool}'.format(
                    slot_id=j+1,
                    equipment_name=equipment_name,
                    skill_name=tool_skill_type,
                    current_skill_level=tool_skill_level,
                    suggested_tool=suggested_tool)

            print(character_string)




        #character_mining_level = character_skill_array[skills_content_keys['mining']]

        print('    ')

    return


def get_next_best_tool(current_tool_id, current_skill_level, skill_type):

    if current_tool_id in max_level_tools:
        return 'BIS'
    elif 'chopping' in skill_type:
        return get_tool_list(current_skill_level, 'EquipmentToolsHatchet')
    elif 'fishing' in skill_type:
        return get_tool_list(current_skill_level, 'FishingRod')
    elif 'worship' in skill_type:
        return get_tool_list(current_skill_level, 'WorshipSkull')
    elif 'trapping' in skill_type:
        return get_tool_list(current_skill_level, 'TrapBoxSet')
    elif 'catching' in skill_type:
        return get_tool_list(current_skill_level, 'CatchingNet')
    elif 'mining' in skill_type:
        return get_tool_list(current_skill_level, 'EquipmentTools')
    else:
        return "ERROR"






    return "Error"


def get_tool_list(current_skill_level, tool_string):
    tool_array = []
    tool_array_1D = []
    for key, value in tool_level_dict.items():
        if tool_string in key and len(tool_string)-2 <= len(key) <= len(tool_string)+2 :
            tool_array.append([key, value])
            tool_array_1D.append(value)
        tool_array.sort(key = lambda x: x)
        tool_array_1D.sort(key=lambda x: x)
    #print(tool_array)
    best_tool = 'None'
    for each in range(len(tool_array)):
        if tool_array[each][1] <= current_skill_level:
            best_tool = tool_array[each][0]

    return tool_name_dict[best_tool]


if __name__ == '__main__':
    mainroutine()

class Player:
    def __init__(self, name: str, hp: int, mp: int):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = {}
        self.guild = 'Unaffiliated'

    def add_skill(self, skill_name, mana_cost):
        if skill_name not in self.skills.keys():
            self.skills[skill_name] = mana_cost
            return f'Skill {skill_name} added to the collection of the player {self.name}'
        return 'Skill already added'

    def player_info(self):
        print_result = f'Name: {self.name}\n'
        print_result += f'Guild: {self.guild}\n'
        print_result += f'HP: {self.hp}\n'
        print_result += f'MP: {self.mp}\n'

        for key, value in self.skills.items():
            print_result += f'==={key} - {value}\n'

        return print_result.strip()



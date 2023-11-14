from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):

    @staticmethod
    def get_team_data():
        expenses = 250000
        sponsors = {"Oracle":{1: 1500000, 2: 800000},
                    "Honda":{8: 20000, 10: 10000}}
        return expenses, sponsors

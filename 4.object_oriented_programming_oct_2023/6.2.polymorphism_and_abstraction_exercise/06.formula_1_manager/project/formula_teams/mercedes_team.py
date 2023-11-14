from project.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):

    @staticmethod
    def get_team_data():
        expenses = 200000
        sponsors = {"Petronas":{1: 1000000, 3: 500000},
                    "TeamViewer":{5: 100000, 7: 50000}}
        return expenses, sponsors

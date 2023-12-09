from project.divers.free_diver import FreeDiver
from project.divers.scuba_diver import ScubaDiver
from project.fish.deep_sea_fish import DeepSeaFish
from project.fish.predatory_fish import PredatoryFish


class NauticalCatchChallengeApp:
    def __init__(self):
        self.divers = []
        self.fish_list = []

    def dive_into_competition(self, diver_type: str, diver_name: str):
        if diver_type not in ["FreeDiver", "ScubaDiver"]:
            return f"{diver_type} is not allowed in our competition."
        if any(diver.name == diver_name for diver in self.divers):
            return f"{diver_name} is already a participant."
        diver = FreeDiver(diver_name) if diver_type == "FreeDiver" else ScubaDiver(diver_name)
        self.divers.append(diver)
        return f"{diver_name} is successfully registered for the competition as a {diver_type}."

    def swim_into_competition(self, fish_type: str, fish_name: str, points: float):
        if fish_type not in ["PredatoryFish", "DeepSeaFish"]:
            return f"{fish_type} is forbidden for chasing in our competition."
        if any(fish.name == fish_name for fish in self.fish_list):
            return f"{fish_name} is already permitted."
        fish = PredatoryFish(fish_name, points) if fish_type == "PredatoryFish" else DeepSeaFish(fish_name, points)
        self.fish_list.append(fish)
        return f"{fish_name} is allowed for chasing as a {fish_type}."

    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool):
        diver = next((d for d in self.divers if d.name == diver_name), None)
        if not diver:
            return f"{diver_name} is not registered for the competition."
        fish = next((f for f in self.fish_list if f.name == fish_name), None)
        if not fish:
            return f"The {fish_name} is not allowed to be caught in this competition."
        if diver.oxygen_level == 0:
            diver.has_health_issue = True
        if diver.has_health_issue:
            return f"{diver_name} will not be allowed to dive, due to health issues."

        if diver.oxygen_level < fish.time_to_catch:
            diver.miss(fish.time_to_catch)
            return f"{diver_name} missed a good {fish_name}."
        if diver.oxygen_level == fish.time_to_catch:
            if is_lucky:
                diver.hit(fish)
                return f"{diver_name} hits a {fish.points}pt. {fish_name}."
            else:
                diver.miss(fish.time_to_catch)
                return f"{diver_name} missed a good {fish_name}."
        if diver.oxygen_level > fish.time_to_catch:
            diver.hit(fish)
            return f"{diver_name} hits a {fish.points}pt. {fish_name}."

    def health_recovery(self):
        count = 0
        for diver in self.divers:
            if diver.has_health_issue:
                diver.has_health_issue = False
                diver.renew_oxy()
                count += 1
        return f"Divers recovered: {count}"

    def diver_catch_report(self, diver_name: str):
        diver = next((d for d in self.divers if d.name == diver_name), None)
        if not diver:
            return
        fish_details = "\n".join(fish.fish_details() for fish in diver.catch)
        return f"**{diver_name} Catch Report**\n{fish_details}"

    def competition_statistics(self):
        divers = sorted([diver for diver in self.divers if not diver.has_health_issue], key=lambda d: (-d.competition_points, -len(d.catch), d.name))
        diver_details = "\n".join(diver.__str__() for diver in divers)
        return f"**Nautical Catch Challenge Statistics**\n{diver_details}"

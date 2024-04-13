from src.scripts import file_exists
from src.scripts import read_json_file
from src.scripts import write_to_json_file
import asyncio


def create_player(
        name: str, full_name: str, position: str, number: list[str | int], country_id: str | int,
        appearances: str | int, goals: str | int):
    return {
        "name": name,
        "full_name": full_name,
        "country_id": country_id,
        "position": position,
        "number": number,
        "appearances": appearances,
        "goals": goals
    }


class SavePlayer:
    filepath = 'real_madrid.json'

    @classmethod
    def save_player(cls, player_info: dict):
        player_pos = player_info['position']

        # if the file doesn't exist
        if not file_exists(filepath=cls.filepath):
            file_content = {}
            asyncio.run(write_to_json_file(content=file_content, filepath=cls.filepath))
            # adding content to empty dict
            file_content[player_pos] = [player_info]

        # if the file exists
        else:
            file_content = asyncio.run(read_json_file(filepath=cls.filepath))

            try:  # trying to ping the data with position key
                file_content[player_pos]
            except KeyError:
                # if a player with a particular position hasn't been added yet
                file_content[player_pos] = [player_info]

            else:  # check if the player exists
                our_player_name = player_info["name"]
                players_on_that_pos: list = file_content[player_pos]

                for player_data in players_on_that_pos:  # player data is dict
                    if player_data["name"] == our_player_name:
                        return None  # aborting
                else:
                    # if the player is not in dict
                    file_content[player_pos].append(player_info)

        # saving changes to file
        asyncio.run(write_to_json_file(content=file_content, filepath=cls.filepath))


class PlayerFactory:
    @staticmethod
    def create_player(
            name: str, full_name: str, position: str, number: list[str | int], country_id: str | int,
            appearances: str | int, goals: str | int
    ):
        """
        Saves the player to db

        Example:
            :param (str) position: "GK"
            :param (str) name: "Iker Casillas"
            :param (str) full_name: "Iker Casillas Fernández"
            :param (list[str]) number: ['1']
            :param (str) country_id: "1"
            :return: None
        """
        return SavePlayer.save_player(
            player_info=create_player(

                position=position,
                name=name,
                full_name=full_name,
                number=number,
                country_id=country_id,
                appearances=appearances,
                goals=goals,

            ))

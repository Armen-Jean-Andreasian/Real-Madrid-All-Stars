from src.model import PlayerFactory

if False:
    player = PlayerFactory.create_player(
        full_name="Nicolas Sebastien Anelka",
        name="Nicolas Anelka",
        position="Forward",

        number=["19"],
        country_id=6,

        appearances=33,
        goals=7
    )


def cli_input():
    full_name = input("Full name: ")
    name = input("Name: ")

    pos = input("Position (GK, FW, DF, MF): ").strip().lower()
    match pos:
        case  "gk":
            position = "Goalkeeper"
        case "df":
            position = "Defender"
        case "mf":
            position = "Midfielder"
        case "fw":
            position = "Forward"
        case _:
            raise Exception("UnknownPosition")

    number = input("Number. Example: 11, 21 : ").split(', ')

    country_id = input("Country Id: ")
    appearances = input("Appearances: ")
    goals = input("Goals: ")

    PlayerFactory.create_player(
        full_name=full_name,
        name=name,
        position=position,

        number=number,
        country_id=country_id,

        appearances=appearances,
        goals=goals
    )

if __name__ == '__main__':
    cli_input()


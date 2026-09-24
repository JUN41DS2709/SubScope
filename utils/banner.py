import pyfiglet
import shutil


def show_banner():
    terminal_width = shutil.get_terminal_size().columns

    banner = pyfiglet.figlet_format(
        "SUBSCOPE",
        font="doom"
    )

    banner_lines = banner.splitlines()

    # Cyan banner
    for line in banner_lines:
        print("\033[96m" + line.center(terminal_width) + "\033[0m")

    # Description
    description = "All in One Passive Subdomain Enumeration Tool"
    print("\033[96m" + description.center(terminal_width) + "\033[0m")

    # Author - positioned toward the right of the centered description
    author = "~ JUN41D"
    description_width = len(description)

    author_position = (
        (terminal_width - description_width) // 2
        + description_width
        - len(author)
    )

    print("\033[92m" + " " * author_position + author + "\033[0m")



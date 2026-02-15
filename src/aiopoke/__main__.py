from aiopoke import version_info


def main():
    print(f"""
\033[1;32m
 .d8b.  d888888b  .d88b.  d8888b.  .d88b.  db   dD d88888b
d8' `8b   `88'   .8P  Y8. 88  `8D .8P  Y8. 88 ,8P' 88'
88ooo88    88    88    88 88oodD' 88    88 88,8P   88ooooo
88~~~88    88    88    88 88~~~   88    88 88`8b   88~~~~~
88   88   .88.   `8b  d8' 88      `8b  d8' 88 `88. 88.
YP   YP Y888888P  `Y88P'  88       `Y88P'  YP   YD Y88888P\033[0m\t\033[1;34mVersion: {version_info}\033[0m
""")


if __name__ == "__main__":
    main()

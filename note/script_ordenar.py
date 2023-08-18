from pathlib import Path as _Path

FILE_PATH = _Path(__file__).parent / 'libs.txt'


def get_libs(file_path: _Path) -> list[str] | None:
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            libs: list[str] = []
            for lib in file.readlines():
                lib = lib.strip()
                libs.append(lib)

        return libs
    except Exception:
        return None


def write_libs(file_path: _Path, libs: list[str] | None) -> bool:
    try:
        if libs is not None:
            with open(file_path, 'w', encoding='utf-8') as file:
                libs = sorted(set(libs))

                for lib in libs:
                    line = f'{lib} \n'
                    file.write(line)
        else:
            raise Exception
        return True
    except Exception:
        return False


list_libs: list[str] | None = get_libs(FILE_PATH)

if write_libs(FILE_PATH, list_libs):
    print('SUCCESS')
else:
    print('ERROR')

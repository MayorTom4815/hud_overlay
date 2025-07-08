import sqlite3 as db
from enum import Enum
import config


class TABLES(Enum):
    CONTROLLER = "Controller"
    BINDING = "Binding"


class SaverManager:
    def __init__(self, file_path: str) -> None:
        self.conx: db.Connection = db.connect(file_path)
        self.cursor: db.Cursor = self.conx.cursor()

        try:
            self.cursor.execute(
                f"CREATE TABLE {TABLES.CONTROLLER.value}(input_type TEXT NOT NULL, button_format INTEGER NOT NULL)"
            )
            self.cursor.execute(
                f"CREATE TABLE {TABLES.BINDING.value}(input_type TEXT NOT NULL, button_format INTEGER NOT NULL, button TEXT NOT NULL, key INTEGER NOT NULL)"
            )

        except Exception as err:
            print(err)

    def write_controller(self) -> None:
        try:
            self.cursor.execute(
                f"INSERT INTO {TABLES.CONTROLLER.value} VALUES (?, ?)",
                (config.input_type.value, config.button_format),
            )

        except Exception as err:
            print(err)

    def write_bindings(self, bindings: list[tuple]) -> None:
        for i in bindings:
            self.cursor.execute(
                f"INSERT INTO {TABLES.BINDING.value} VALUES (?, ?, ? ,?)", i
            )
            self.conx.commit()

    def read_controller(self) -> bool:
        control: list[tuple] = self.cursor.execute(
            f"SELECT input_type FROM {TABLES.CONTROLLER.value} WHERE input_type=? AND button_format=?",
            (config.input_type.value, config.button_format),
        ).fetchall()

        return True if control != [] else False

    def read_bindings(self) -> list[tuple]:
        control: list[tuple] = self.cursor.execute(
            f"SELECT * FROM {TABLES.CONTROLLER.value} WHERE input_type=? AND button_format=?",
            (config.input_type.value, config.button_format),
        ).fetchall()

        try:
            temp = self.cursor.execute(
                f"SELECT * FROM {TABLES.BINDING.value} WHERE input_type=? and button_format=?",
                control[0],
            ).fetchall()

            return temp

        except Exception:
            print("[Error] No hay alguna configuracion para ese control")
            return []

    def delete_all(self):
        self.cursor.execute(f"DELETE FROM {TABLES.CONTROLLER.value}")
        self.cursor.execute(f"DELETE FROM {TABLES.BINDING.value}")

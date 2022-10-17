import csv
from decimal import Decimal
from io import BytesIO
from typing import Generator, Iterable

from dateutil.parser import parse

from schemas.data import TransactionSchema, Statuses


def iter_rows(csv_content: BytesIO) -> Generator[tuple, None, tuple]:
    """
    encoding="cp1251", HEADERS:
    'Дата операции', 'Дата платежа', 'Номер карты',
    'Статус', 'Сумма операции', 'Валюта операции',
    'Сумма платежа', 'Валюта платежа', 'Кэшбэк',
    'Категория', 'MCC', 'Описание',
    'Бонусы (включая кэшбэк)', 'Округление на инвесткопилку', 'Сумма операции с округлением'
    """
    reader = csv.reader(csv_content, delimiter=";")
    next(reader)  # skip headers
    yield from reader


def from_csv_row(row: Iterable) -> TransactionSchema | None:
    if (status := row[3]) == Statuses.OK.value:
        return TransactionSchema(
            datetime=parse(row[0]),
            card=row[2],
            payment=Decimal(row[4].replace(",", ".")).quantize(Decimal("1.00")),
            category=row[9],
            mcc=int(row[10]) if row[10] else None,
            description=row[11]
        )


def serialize_csv(csv_content: BytesIO) -> tuple[TransactionSchema, ...]:
    return tuple(filter(bool, map(from_csv_row, iter_rows(csv_content))))

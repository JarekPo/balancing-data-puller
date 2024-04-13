from api_requests.api_requests import get_api_data
from database.database import get_db_data, insert_data_to_db


def handle_received_data(date: str) -> None:
    api_data = get_api_data(date)
    db_data = get_db_data(date)

    if db_data:
        for entry in api_data.get("data"):
            api_values = list(entry.values())
            api_settlement_period = entry.get("settlementPeriod")
            is_entry_in_db = False

            for row in db_data:
                db_settlement_period = row[2]
                if api_settlement_period == db_settlement_period and api_values[
                    2:
                ] == list(row[3:]):
                    is_entry_in_db = True
                    break

            if not is_entry_in_db:
                insert_data_to_db(api_values)
    else:
        for entry in api_data.get("data"):
            insert_data_to_db(list(entry.values()))

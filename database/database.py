import datetime
from typing import Any
import psycopg

from api_requests.api_requests import get_API_data
from config import (
    DATABASE_HOST,
    DATABASE_PORT,
    DATABASE_PASSWORD,
    DATABASE_USER,
    DATABASE_NAME,
)

DATABASE_URL = f"postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}"
current_date = datetime.datetime.today().strftime("%Y-%m-%d")


def get_new_data(date: str) -> Any:
    requested_data = get_API_data(date)
    return requested_data


def create_brms_table() -> Any:
    with psycopg.connect(
        dbname=DATABASE_NAME,
        user=DATABASE_USER,
        password=DATABASE_PASSWORD,
        host=DATABASE_HOST,
        port=DATABASE_PORT,
    ) as conn:
        with conn.cursor() as cur:

            cur.execute(
                """
                CREATE TABLE IF NOT EXISTS brms_data (
                    id serial PRIMARY KEY,
                    settlementDate date,
                    settlementPeriod integer,
                    startTime timestamp,
                    createdDateTime timestamp,
                    systemSellPrice float,
                    systemBuyPrice float,
                    bsadDefaulted boolean,
                    priceDerivationCode varchar(5),
                    reserveScarcityPrice float,
                    netImbalanceVolume float,
                    sellPriceAdjustment float,
                    buyPriceAdjustment float,
                    replacementPrice float,
                    replacementPriceReferenceVolume float,
                    totalAcceptedOfferVolume float,
                    totalAcceptedBidVolume float,
                    totalAdjustmentSellVolume integer,
                    totalAdjustmentBuyVolume integer,
                    totalSystemTaggedAcceptedOfferVolume float,
                    totalSystemTaggedAcceptedBidVolume float,
                    totalSystemTaggedAdjustmentSellVolume integer,
                    totalSystemTaggedAdjustmentBuyVolume integer
                    )
                """
            )
            conn.commit()


def compare_requested_data_withdatabase_entries(data: Any) -> Any:
    new_data = get_API_data(current_date)
    pass


def insert_data_to_db(data: Any) -> Any:

    with psycopg.connect(
        dbname=DATABASE_NAME,
        user=DATABASE_USER,
        password=DATABASE_PASSWORD,
        host=DATABASE_HOST,
        port=DATABASE_PORT,
    ) as conn:
        with conn.cursor() as cur:
            for element in data.get("data"):

                insert_query = """
                    INSERT INTO brms_data (
                        settlementDate,
                        settlementPeriod,
                        startTime, 
                        createdDateTime, 
                        systemSellPrice,
                        systemBuyPrice, 
                        bsadDefaulted, 
                        priceDerivationCode, 
                        reserveScarcityPrice, 
                        netImbalanceVolume, 
                        sellPriceAdjustment, 
                        buyPriceAdjustment, 
                        replacementPrice,
                        replacementPriceReferenceVolume, 
                        totalAcceptedOfferVolume, 
                        totalAcceptedBidVolume,
                        totalAdjustmentSellVolume, 
                        totalAdjustmentBuyVolume, 
                        totalSystemTaggedAcceptedOfferVolume,
                        totalSystemTaggedAcceptedBidVolume, 
                        totalSystemTaggedAdjustmentSellVolume, 
                        totalSystemTaggedAdjustmentBuyVolume 
                    ) VALUES (
                        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
                    );
                """

                cur.execute(insert_query, tuple(element.values()))
                conn.commit()

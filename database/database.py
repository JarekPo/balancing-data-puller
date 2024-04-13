from typing import Any, List
import psycopg

from config import (
    DATABASE_HOST,
    DATABASE_PORT,
    DATABASE_PASSWORD,
    DATABASE_USER,
    DATABASE_NAME,
)


def create_brms_table() -> None:
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
                    settlementDate varchar(12),
                    settlementPeriod integer,
                    startTime varchar(30),
                    createdDateTime varchar(30),
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
                    totalAdjustmentSellVolume float,
                    totalAdjustmentBuyVolume float,
                    totalSystemTaggedAcceptedOfferVolume float,
                    totalSystemTaggedAcceptedBidVolume float,
                    totalSystemTaggedAdjustmentSellVolume float,
                    totalSystemTaggedAdjustmentBuyVolume float
                    )
                """
            )
            conn.commit()


def insert_data_to_db(data: List[Any]) -> None:

    with psycopg.connect(
        dbname=DATABASE_NAME,
        user=DATABASE_USER,
        password=DATABASE_PASSWORD,
        host=DATABASE_HOST,
        port=DATABASE_PORT,
    ) as conn:
        with conn.cursor() as cur:

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

            cur.execute(insert_query, data)
            conn.commit()


def get_db_data(date: str) -> List[Any]:
    query = "SELECT * FROM brms_data WHERE settlementDate = %s"

    with psycopg.connect(
        dbname=DATABASE_NAME,
        user=DATABASE_USER,
        password=DATABASE_PASSWORD,
        host=DATABASE_HOST,
        port=DATABASE_PORT,
    ) as conn:
        with conn.cursor() as cur:
            cur.execute(query, (date,))
            data: List[Any] = cur.fetchall()
            return data

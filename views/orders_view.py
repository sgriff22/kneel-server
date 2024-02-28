import sqlite3
import json


def get_all_orders():
    # Open a connection to the database
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # SQL query for all the orders
        db_cursor.execute(
            """
        SELECT 
            o.id,
            o.metal_id,
            o.size_id,
            o.style_id
        FROM Orders o
        """
        )
        query_results = db_cursor.fetchall()

        # Initialize an empty list to store each dictionary made from the iteration below
        orders = []

        for row in query_results:
            orders.append(dict(row))

        # Serialize Python list to JSON encoded string
        serialized_orders = json.dumps(orders)

    return serialized_orders


def get_single_order(pk):
    # Open a connection to the database
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # SQL query for all the orders
        db_cursor.execute(
            """
        SELECT 
            o.id,
            o.metal_id,
            o.size_id,
            o.style_id
        FROM Orders o
        WHERE o.id = ?
        """,
            (pk,),
        )
        query_results = db_cursor.fetchone()

        # Serialize Python list to JSON encoded string
        serialized_orders = json.dumps(dict(query_results))

    return serialized_orders

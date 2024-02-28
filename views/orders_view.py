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


def create_order(order_data):
    # Open a connection to the database
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor = conn.cursor()

        # SQL query for all the orders
        db_cursor.execute(
            """
        INSERT INTO Orders (metal_id, size_id, style_id)
        VALUES (?, ?, ?)
        """,
            (order_data["metal_id"], order_data["size_id"], order_data["style_id"]),
        )

        new_order_id = db_cursor.lastrowid

    return new_order_id if new_order_id is not None else None


def delete_order(pk):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query for the order delete
        db_cursor.execute(
            """
        DELETE FROM Orders WHERE id = ?
        """,
            (pk,),
        )
        number_of_rows_deleted = db_cursor.rowcount

    return True if number_of_rows_deleted > 0 else False

import json
import sqlite3


def dict_factory(cursor, row):
    fields = [column[0] for column in cursor.description]
    return {key: value for key, value in zip(fields, row)}


def format_response(code, data):
    return {
        "statusCode": code,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(data, ensure_ascii=False),
    }


def get_data_from_db(query, params):
    with sqlite3.connect("./cc_functions/chinook.db") as con:
        cur = con.cursor()
        data = list(cur.execute(query, params).fetchall())
        cur.close()
    return data


def handle_customers(event):
    query = "SELECT * FROM customers WHERE CustomerId = ?"
    customer_id = event["pathParamters"]["customer_id"]

    data = get_data_from_db(query, [customer_id])
    return format_response(200, data)


def handle_albums(event):
    query = """
        SELECT
            a.*
            , a2.Name as ArtistName
            , t.Name as TrackName
        FROM albums a
        JOIN tracks t
            ON a.AlbumId = t.AlbumId
        JOIN artists a2
            on a.ArtistId = a2.ArtistId
        WHERE a.AlbumId = ?
    """
    album_id = event["pathParameters"]["album_id"]

    data = get_data_from_db(query, [album_id])
    first_row = data[0]
    response_body = {
        "AlbumId": first_row["AlbumId"],
        "Title": first_row["Title"],
        "Artist": first_row["ArtistName"],
        "Tracks": [row["TrackName"] for row in data],
    }
    return format_response(200, response_body)


def lambda_handler(event, _context):
    # create two endpoints, customers and albums.
    if event["httpMethod"] != "GET":
        return format_response(400, "Unsupported method")

    resource = event["resource"]
    if "customers" in resource and event["pathParameters"]:
        return handle_customers(event)

    if "albums" in resource and event["pathParameters"]:
        return handle_albums(event)

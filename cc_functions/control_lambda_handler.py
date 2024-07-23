import json
import sqlite3


def dict_factory(cursor, row):
    fields = [column[0] for column in cursor.description]
    return {key: value for key, value in zip(fields, row)}


def lambda_handler(event, _context):
    # create two endpoints, customers and albums.
    if event['httpMethod'] != "GET":
        return {
            "statusCode": 400,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps("Unsupported Method", ensure_ascii=False),
        }

    resource = event['resource']
    if 'customers' in resource and event['pathParameters']:
        query = """
            SELECT
            c.*
            , t.Name
            FROM customers c
            JOIN invoices i
                ON  c.CustomerId = i.CustomerId
            JOIN invoice_items ii
                on i.InvoiceId = ii.InvoiceId
			JOIN tracks t
				ON ii.TrackId = t.TrackId
            WHERE c.CustomerId = ?
        """
        customer_id = event["pathParameters"]["customer_id"]

        with sqlite3.connect('./cc_functions/chinook.db') as con:
            con.row_factory = dict_factory
            cur = con.cursor()
            data = list(cur.execute(query, [customer_id]).fetchall())

            response_body = {
                "CustomerId": data[0][0],
                "Name": f"{data[0][2]}, {data[0][1]}",
                "Address": data[0][4],
                "City": data[0][5],
                "State": data[0][6],
                "Country": data[0][7],
                "PostalCode": data[0][8],
                "OwnedTracks": [row[13] for row in data],
            }
            cur.close()
            return {
                "statusCode": 200,
                "headers": {"Content-Type": "application/json"},
                "body": json.dumps(response_body, ensure_ascii=False),
            }

    if 'albums' in resource and event['pathParameters']:
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
        customer_id = event["pathParameters"]["album_id"]

        with sqlite3.connect("./cc_functions/chinook.db") as con:
            con.row_factory = dict_factory
            cur = con.cursor()
            data = list(cur.execute(query, [customer_id]).fetchall())
            cur.close()
            first_row = data[0]
            response_body = {
                "AlbumId": first_row[0],
                "Title": first_row[1],
                "Artist": first_row[2],
                "Tracks": [row[3] for row in data],
            }
            return {
                "statusCode": 200,
                "headers": {"Content-Type": "application/json"},
                "body": json.dumps(response_body, ensure_ascii=False),
            }


if __name__ == '__main__':
    e = {
        "resource": "/customers",
        "httpMethod": "GET",
        "pathParameters": {"customer_id": 52, "album_id": 23}  # randint(1, NUM_CUSTOMERS)},
    }
    lambda_handler(e, {})

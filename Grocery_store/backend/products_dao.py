from sql_connection import get_sql_connection 
def get_all_products(connection): #Over here, value of connection is cnx. That cnx is only returned if __cnx has global value of None meaning no initial connection exists. 

    cursor = connection.cursor()

    query = "SELECT p.product_id, p.Name, p.uom_id, p.price_per_unit, u.uom_name FROM products as p INNER JOIN uom as u ON p.uom_id = u.uom_id"

    cursor.execute(query)

    response = []
    
    for (product_id, Name, uom_id, price_per_unit, uom_name) in cursor:
        response.append(
        {
            'product_id': product_id,
            'name':Name,
            'uom_id': uom_id,
            'price_per_unit': price_per_unit,
            'uom_name': uom_name
        }
    )
    if not response:
        print("No products found in the database.")
    return response
    
    

def insert_new_product(connection, product):
    cursor = connection.cursor()
    query = ("INSERT INTO products(Name, uom_id, price_per_unit)VALUES (%s, %s, %s)")
    data = (product['product_name'], product['uom_id'], product['price_per_unit'])
    cursor.execute(query, data)
    connection.commit()
    lastrowID = cursor.lastrowid

    return lastrowID

def delete_product(connection, product_id):
    cursor = connection.cursor()
    query = ("DELETE FROM products WHERE product_id=" + str(product_id))
    cursor.execute(query)
    connection.commit()

    
if __name__ == '__main__':
    connection = get_sql_connection()
    print(get_all_products(connection))
    #print(connection)

    # print(insert_new_product(connection, {
    #     'product_name': 'cabbage',
    #     'uom_id':'1',
    #     'price_per_unit': '10'
    # }))

    ##print(delete_product(connection, 13))

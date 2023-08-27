from sql_connection import get_sql_connection

def get_all_products(connection):

    cursor=connection.cursor()

    query="SELECT product_table.product_id, product_table.name, product_table.uom_id, product_table.price_per_unit, uom_table.uom_name FROM grocerystore.product_table inner join uom_table on product_table.uom_id=uom_table.uom_id"

    cursor.execute(query)

    response=[]

    for (product_id, name, uom_id,price_per_unit,uom_name ) in cursor:

        response.append({
            'product_id': product_id,
            'customer_name': name,
            'uom_id' : uom_id,
            'total': price_per_unit,
            'uom_name': uom_name
        })

        #print(product_id,name, uom_id,price_per_unit, uom_name)
    connection.close()

    return response


def insert_new_product(connection,product):
    cursor=connection.cursor()
    query=("INSERT INTO product_table"
           "(name, uom_id, price_per_unit)"
            "VALUES (%s, %s,%s)")

    data=(product['product_name'],product['uom_id'],product['price_per_unit'])
    cursor.execute(query,data)
    connection.commit()
    return cursor.lastrowid

def delete_product(connection, product_id):
    cursor = connection.cursor()
    query=("DELETE FROM product_table where product_id="+str(product_id))
    cursor.execute(query)
    connection.commit()

if __name__=='__main__':
    connection = get_sql_connection()
    print(delete_product(connection,6))
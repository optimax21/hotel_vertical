import frappe
from frappe.utils import nowdate

@frappe.whitelist()
def create_kot_history(so_name):
    print(":::::::::::::call kot history::::1::::::::", so_name)

    sale_order_doc = frappe.get_doc("Sales Order", so_name)
    print("\n sale_order_doc :::::::::::::::", sale_order_doc) 
    
    # Create a new KOT History document
    kot = frappe.get_doc({
        "doctype": "Kitchen Order Tickets",
        "order_number": sale_order_doc.name,
        "reservation_number": sale_order_doc.custom_table_order_id,
        "customer_name": sale_order_doc.customer_name,
        "date": nowdate(),
        "waiter_name": sale_order_doc.custom_waiter_name,
    })

    # Fetch existing KOTs for this Sales Order
    existing_kots = frappe.get_all("Kitchen Order Tickets", filters={
        "order_number": sale_order_doc.name
    }, fields=["name"])

    existing_kot_names = [kot['name'] for kot in existing_kots]
    print("\n Existing KOTs Names :::::111::::::::::", existing_kot_names)
    
    # Iterate through each item in the Sales Order
    for item in sale_order_doc.items:
        # Check if the item already exists in any KOT for the same Sales Order
        print("\n Processing item :::::::::::", item.item_code, item.name)
        
        existing_qty = 0
        if existing_kot_names:  # Ensure the list is not empty before executing the query
            existing_item_qty = frappe.db.sql("""
                SELECT
                    SUM(qty) AS total_qty
                FROM
                    `tabSales Order Item`
                WHERE
                    item_code = %s AND parent IN %s AND parentfield = %s AND parenttype = %s
                GROUP BY
                    item_code
            """, (item.item_code, tuple(existing_kot_names), 'order_list', 'Kitchen Order Tickets'), as_dict=True)

            existing_qty = existing_item_qty[0].get('total_qty', 0) if existing_item_qty else 0
        print("\n Existing Qty for item ::::::::::::::", existing_qty)
        
        # If the current qty is greater than the existing qty in KOTs, add the difference to the new KOT
        if item.qty > existing_qty:
            qty_to_add = item.qty - existing_qty
            kot.append("order_list", {
                "item_code": item.item_code,
                "item_name": item.item_name,
                "delivery_date": item.delivery_date,
                "qty": qty_to_add,
                "rate": item.rate,
                "uom": 'Nos',
                "conversion_factor": 1
            })
            print(f"\n Adding item {item.item_code} with qty {qty_to_add} to new KOT")

    # Add table_list from the Sales Order to the KOT History
    for table_item in sale_order_doc.custom_table_booking_child:
        kot.append("table_list", {
            "table_number": table_item.table_number,
            "capacity": table_item.capacity,
            "floor": table_item.floor,
        })
    
    # Insert the KOT History document if there are new items or updated quantities to add
    if kot.get("order_list"):
        kot.insert(ignore_permissions=True)
        frappe.db.commit()
        print("\n New KOT Created:", kot.name)
    else:
        print("No new items or updated quantities to add to Kitchen Order Tickets.")

// Copyright (c) 2024, Ketan Patel and contributors
// For license information, please see license.txt

frappe.ui.form.on('Table Booking Child', {
    table_number: function(frm, cdt, cdn) {
        let child = locals[cdt][cdn];
        console.log(":::::::::::::::::", child)
        if (child.table_number) {
            // Fetch the capacity from the Tables doctype based on the selected table_number
            frappe.db.get_value('Tables', child.table_number, 'capacity')
            .then(r => {
                if (r.message) {
                    frappe.model.set_value(cdt, cdn, 'capacity', r.message.capacity);
                }
            });
        } else {
            // Clear capacity if no table_number is selected
            frappe.model.set_value(cdt, cdn, 'capacity', null);
        }
    }
});

frappe.ui.form.on('Table Booking', {
    refresh: function(frm) {
        // Check if the workflow state is 'Done'
        if (frm.doc.workflow_state === 'Done') {
            frm.add_custom_button(__('Create Order'), function() {
                // Trigger function to create a Sales Order
                create_sales_order(frm);
            }, __('Actions')); // Optional: Group under 'Actions' dropdown if needed
        }
    }
});

// Function to create a Sales Order
function create_sales_order(frm) {
    frappe.model.with_doctype('Sales Order', function() {
        var so = frappe.model.get_new_doc('Sales Order');
        
        // Set the customer name from Table Booking
        so.customer = frm.doc.customer_name;
        so.custom_table_order_id = frm.doc.name;

        // Loop through each item in the Table Booking Child table
        frm.doc.table_booking_child.forEach(function(row) {
            var so_table = frappe.model.add_child(so, 'custom_table_booking_child');
            so_table.capacity = row.capacity;           // Assuming you have capacity field in the child table
            so_table.table_number = row.table_number;   // Adding custom field for table_number if required
            so_table.floor = row.floor;  
        });

        // Open the new Sales Order in a new form view
        frappe.set_route('Form', 'Sales Order', so.name);
    });
}

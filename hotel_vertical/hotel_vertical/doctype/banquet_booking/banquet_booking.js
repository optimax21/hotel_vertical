// Copyright (c) 2024, Ketan Patel and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Banquet Booking", {
// 	refresh(frm) {

// 	},
// });


// frappe.ui.form.on('Banquet Booking', {
//     refresh: function(frm) {
//         if (frm.doc.workflow_state === 'Done')
//         	{
//         		frm.add_custom_button(__('Create Order'), function() {
// 	            // Trigger function to create a Sales Order
// 	            create_sales_order(frm);
// 	        }, __('Actions')); // Optional: Group under 'Actions' dropdown if needed	
//         }
        
//     }
// });

// // Function to create a Sales Order
// function create_sales_order(frm) {
//     frappe.model.with_doctype('Sales Order', function() {
//         var so = frappe.model.get_new_doc('Sales Order');
        
//         // Set the customer name from Table Booking
//         so.custom_banquet_id = frm.doc.name;
//         so.customer = frm.doc.customer_name;
//         so.custom_banquet_type = frm.doc.banquet_type;
//         so.custom_event_name = frm.doc.event_name;
//         so.transaction_date = frm.doc.start_date;

        
//      	// Add the test product "BANQUET HALL" to the Sales Order items table
//         var item = frappe.model.add_child(so, 'items');
//         item.item_code = 'BANQUET HALL'; // Assuming the item code for the test product is "BANQUET HALL"
//         item.qty = 1;
//         item.rate = 1000;
//         item.amount = 1000;
        
//         // Save the Sales Order automatically
//         frappe.db.insert(so).then(function(doc) {
//             frappe.msgprint(__('Sales Order {0} created successfully.', [doc.name]));
//         }).catch(function(err) {
//             frappe.msgprint(__('Failed to create Sales Order: {0}', [err.message]));
//         });
//     });
// }


frappe.ui.form.on('Banquet Booking', {
    refresh: function(frm) {
        if (frm.doc.workflow_state === 'Done') {
            frm.add_custom_button(__('Create Order'), function() {
                // Check if the item exists, and create it if not, then create the Sales Order
                create_item_and_sales_order(frm);
            }, __('Actions')); // Optional: Group under 'Actions' dropdown if needed
        }
    }
});

// Function to check and create the item, then create and save the Sales Order
function create_item_and_sales_order(frm) {
    const item_code = 'BANQUET HALL';
    
    // Check if the item exists
    frappe.db.exists('Item', item_code).then(exists => {
        if (!exists) {
            // Create the item if it doesn't exist
            frappe.db.insert({
                doctype: 'Item',
                item_code: item_code,
                item_name: 'Banquet Hall',
                item_group: 'All Item Groups',  // Change this to your desired item group
                stock_uom: 'Nos',  // Change this to your desired UOM
                standard_rate: 1000
            }).then(() => {
                // After creating the item, create the Sales Order
                create_and_save_sales_order(frm, item_code);
            }).catch(err => {
                frappe.msgprint(__('Failed to create item: {0}', [err.message]));
            });
        } else {
            // If the item exists, proceed to create the Sales Order
            create_and_save_sales_order(frm, item_code);
        }
    });
}

// Function to create and save the Sales Order with the test product
function create_and_save_sales_order(frm, item_code) {
    frappe.model.with_doctype('Sales Order', function() {
        var so = frappe.model.get_new_doc('Sales Order');
        
        // Set the customer details from Banquet Booking
        so.custom_banquet_id = frm.doc.name;
        so.customer = frm.doc.customer_name;
        so.custom_banquet_type = frm.doc.banquet_type;
        so.custom_event_name = frm.doc.event_name;
        so.transaction_date = frm.doc.start_date;
        so.set_warehouse = 'Stores - SD'

        // Add the product "BANQUET HALL" to the Sales Order items table
        var item = frappe.model.add_child(so, 'items');
        item.item_code = item_code;
        item.qty = 1;
        item.rate = 1000;
        item.delivery_date = frm.doc.start_date;
        item.amount = 1000;
        
        // Save the Sales Order automatically
        frappe.db.insert(so).then(function(doc) {
            frappe.msgprint(__('Banquet Order {0} created successfully.', [doc.name]));
        }).catch(function(err) {
            frappe.msgprint(__('Failed to create Sales Order: {0}', [err.message]));
        });
    });
}

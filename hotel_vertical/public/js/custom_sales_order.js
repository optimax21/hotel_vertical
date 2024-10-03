frappe.ui.form.on('Sales Order', {
    refresh: function(frm) {
        frm.add_custom_button(__('KOT History'), function() {
            // Call the Python method to create KOT History
            frappe.call({
                method: "hotel_vertical.public.py.custom_sales_order.create_kot_history",
                args: {
                    so_name: frm.doc.name
                },
                callback: function(r) {
                    if (!r.exc) {
                        frappe.msgprint(__('KOT History created successfully.'));
                    }
                }
            });
        }, __('GENERATE KOT')); // Group under 'GENERATE KOT' dropdown if needed
    }
});


frappe.ui.form.on('Sales Order', {
    refresh: function(frm) {
        frm.fields_dict['items'].grid.get_field('item_code').get_query = function(doc, cdt, cdn) {
            // Only include items where custom_is_food_item is checked
            return {
                filters: {
                    'custom_is_food_item': 1
                }
            };
        };
    }
});

frappe.ui.form.on('Sales Order', {
    item_code: function(frm) {
        frm.fields_dict['items'].grid.get_field('item_code').get_query = function(doc, cdt, cdn) {
            // Only include items where custom_is_food_item is checked
            return {
                filters: {
                    'custom_is_food_item': 1
                }
            };
        };
    }
});

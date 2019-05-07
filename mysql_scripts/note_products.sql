select note_products.employee_id,customer_histories.date,note_products.sale_price from customer_histories,note_products where customer_histories.id = note_products.customer_history_id and note_products.user_id=102 and note_products.employee_id IN (49,74,55,110);


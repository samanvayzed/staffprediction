select note_services.employee_id,customer_histories.date,note_services.service_price from customer_histories,note_services where customer_histories.id = note_services.customer_history_id and customer_histories.user_id=102 and note_services.employee_id IN (49,74,55,110);


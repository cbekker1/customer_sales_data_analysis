select category_group_no	
		,category_group_desc
		,sum(sales) as sales_value
	from cust_sales
	group by category_group_no	
		,category_group_desc
	order by sales_value desc
	limit 10 
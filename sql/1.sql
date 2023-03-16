select count(distinct member_id) as customers
	,count(distinct article_code) as articles
	,count(distinct category_group_no) as article_groups
	,sum(sales) as sales
	
from cust_sales
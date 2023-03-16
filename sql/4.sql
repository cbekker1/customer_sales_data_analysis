with cust as (
select member_id
	, count(distinct period) no_periods
	
	from cust_sales
	group by member_id
	having count(distinct period) >1
	
)

select count (distinct member_id) as "no of members that appear in both groups"
from cust


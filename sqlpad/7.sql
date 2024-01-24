SELECT EXTRACT(YEAR from rental_ts) as year,
			 EXTRACT(MONTH from rental_ts )  as mon,
			 count(distinct customer_id) as uu_cnt
			 
FROM rental
group by year,mon;
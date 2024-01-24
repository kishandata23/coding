SELECT EXTRACT(YEAR FROM payment_ts) as year,
EXTRACT(MONTH FROM payment_ts) as mon,
sum(amount) as rev
FROM payment
group by year,mon;
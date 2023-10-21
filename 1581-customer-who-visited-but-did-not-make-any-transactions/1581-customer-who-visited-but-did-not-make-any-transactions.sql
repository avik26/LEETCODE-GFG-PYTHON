WITH CustomerVisits AS (
  SELECT v.customer_id, v.visit_id
  FROM Visits v
  LEFT JOIN Transactions t ON v.visit_id = t.visit_id
  WHERE t.visit_id IS NULL
)

SELECT customer_id, COUNT(visit_id) AS count_no_trans
FROM CustomerVisits
GROUP BY customer_id;

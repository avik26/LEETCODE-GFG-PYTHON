# Write your MySQL query statement below
WITH ContestCounts AS (
    SELECT
        r.contest_id,
        COUNT(DISTINCT r.user_id) AS registered_count
    FROM Register r
    GROUP BY r.contest_id
),
TotalUsers AS (
    SELECT COUNT(DISTINCT user_id) AS total_users
    FROM Users
)
SELECT
    c.contest_id,
    ROUND((c.registered_count / t.total_users) * 100, 2) AS percentage
FROM ContestCounts c
JOIN TotalUsers t
ON 1=1
ORDER BY percentage DESC, contest_id;

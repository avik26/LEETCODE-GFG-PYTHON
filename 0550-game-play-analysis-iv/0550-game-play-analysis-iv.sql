WITH FirstLogin AS (
    SELECT player_id, MIN(event_date) AS first_login_date
    FROM Activity
    GROUP BY player_id
)

SELECT 
    ROUND(
        COUNT(CASE WHEN DATEDIFF(A.event_date, FL.first_login_date) = 1 THEN 1 ELSE NULL END) 
        / COUNT(DISTINCT A.player_id), 2
    ) AS fraction
FROM Activity A
JOIN FirstLogin FL ON A.player_id = FL.player_id;

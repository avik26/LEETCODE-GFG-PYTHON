SELECT c1.name
FROM Customer c1
LEFT JOIN Customer c2 ON c1.referee_id = c2.id
WHERE c2.id IS NULL OR c2.id != 2;

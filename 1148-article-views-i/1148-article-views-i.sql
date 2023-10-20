SELECT DISTINCT author_id AS id
FROM Views
WHERE author_id = viewer_id AND author_id IN (SELECT DISTINCT author_id FROM Views WHERE author_id IS NOT NULL)
ORDER BY id;

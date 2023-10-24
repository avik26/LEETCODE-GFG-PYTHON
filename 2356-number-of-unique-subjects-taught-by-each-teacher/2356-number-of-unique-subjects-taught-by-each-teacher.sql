SELECT teacher_id, COUNT(subject_id) AS cnt
FROM (
    SELECT DISTINCT teacher_id, subject_id
    FROM Teacher
) AS distinct_subjects
GROUP BY teacher_id;

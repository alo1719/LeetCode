-- Notice that one SQL statement can only be one sentence, not like programming languages.
-- So need to substitude all middle results with subqueries.
-- Recommend to have subqueries first, then plug them into the main query.
WITH seniors AS (SELECT * FROM candidates WHERE position = 'senior'),
     juniors AS (SELECT * FROM candidates WHERE position = 'junior')
SELECT COUNT(1),
       (SELECT COUNT(1)
        FROM (SELECT *, (SELECT SUM(salary) FROM seniors seniors_tmp WHERE seniors_tmp.id <= seniors.id) AS sum
              FROM seniors
              WHERE sum <= 50000))
FROM (SELECT *,
             (SELECT SUM(salary) FROM juniors juniors_tmp WHERE juniors_tmp.id <= juniors.id) AS sum
      FROM juniors
      WHERE sum <= 50000 - (SELECT COALESCE(MAX(sum), 0)
                            FROM (SELECT *,
                                         (SELECT SUM(salary)
                                          FROM seniors seniors_tmp
                                          WHERE seniors_tmp.id <= seniors.id) AS sum
                                  FROM seniors
                                  WHERE sum <= 50000)));
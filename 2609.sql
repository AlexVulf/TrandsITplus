SELECT c.name, SUM(p.amount) AS sum
FROM categories c
JOIN products p ON c.id = p.id_categories
GROUP BY c.name
ORDER BY c.name;

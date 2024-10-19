-- Ranks country origins of bands --
-- Ordered by number of fans(non-unique --
SELECT origin,
       SUM(nb_fans) as total_fans
FROM
	metal_bands
GROUP BY
	origin
ORDER BY
	total_fans DESC;


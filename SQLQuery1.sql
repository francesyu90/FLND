--SELECT *
--FROM DBO.Quality;


--SELECT *
--FROM DBO.RealValue RV
--WHERE RV.tag_id = '361';

-- 354, 348, 350, 361, 303

SELECT * 
FROM DBO.RealValue RV 
WHERE CAST(RV.time AS date) BETWEEN '2/10/2017' and '2/17/2017'
AND RV.tag_id = '361';


-- 
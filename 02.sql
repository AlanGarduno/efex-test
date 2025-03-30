
WITH CustomerData AS (
    SELECT 
        C.id,
        CONCAT(C.first_name, ' ', C.last_name) AS full_name,
        LENGTH(CONCAT(C.first_name, C.last_name)) AS name_length
    FROM CUSTOMER C
)
SELECT 
    id,
    full_name
FROM 
    CustomerData
WHERE 
    name_length < 12
ORDER BY 
    name_length,
    LOWER(full_name),
    id;
            SELECT column_name             SELECT column_name 
            FROM information_schema.table_constraints tc            FROM information_schema.table_constraints tc
            JOIN information_schema.constraint_column_usage ccu             JOIN information_schema.constraint_column_usage ccu 
                ON tc.constraint_name = ccu.constraint_name                ON tc.constraint_name = ccu.constraint_name
            WHERE tc.table_name = 'students'             WHERE tc.table_name = 'students' 
                AND tc.constraint_type IN ('UNIQUE')                AND tc.constraint_type IN ('UNIQUE')
        ) THEN 'YES'        ) THEN 'YES'
        ELSE 'NO'        ELSE 'NO'
    END AS is_unique    END AS is_unique
FROM FROM 
    information_schema.columns    information_schema.columns
WHERE WHERE 
    table_name = 'students';    table_name = 'students';

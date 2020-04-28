SELECT  name, expiredate, price FROM food
WHERE AVG(price) = (SELECT MIN(price) FROM food f
                        WHERE f.placeid = placeid
                    )
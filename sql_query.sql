/*1. Write a query that will display the results below (Note: some columns might be renamed 
but use the column names above). It should only show 2020 data and order by driver points. */

SELECT 
  circuit_location AS loc,
  grid,
  position,
  fastest_lap,
  points,
  driver_name,
  race_name,
  time,
  year,
  team_name,
  date
FROM races
WHERE year = 2020
ORDER BY points DESC;
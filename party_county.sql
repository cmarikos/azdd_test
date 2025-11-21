CREATE OR REPLACE VIEW `valued-lambda-478823-h0.azdd_test.party_county` AS(
SELECT 
c.LABEL AS County
, p.active_dem/p.active_total AS dem_margin
, p.active_rep/p.active_total AS rep_margin
, (p.active_dem / p.active_total) - (p.active_rep / p.active_total) AS net_partisan_margin
, ST_GEOGFROMTEXT(c.WKT) AS GEOMETRY
FROM `valued-lambda-478823-h0.azdd_test.party_status_clean` AS p

LEFT JOIN `valued-lambda-478823-h0.azdd_test.colorado_counties` AS c
  ON p.county = c.LABEL

-- there are 64 counties in CO, I'm getting a null value on row 65
WHERE c.LABEL IS NOT NULL

)
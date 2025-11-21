CREATE OR REPLACE VIEW `valued-lambda-478823-h0.azdd_test.age_buckets` AS(
SELECT  
g.county

-- dem buckets
, SUM(g.dem_lt18) AS dem_lt18
, SUM(g.dem_18_24) AS dem_18_24
, SUM(g.dem_25_34) AS dem_25_34
, SUM(g.dem_35_44) AS dem_35_44
, SUM(g.dem_45_54) AS dem_45_54
, SUM(g.dem_55_64) AS dem_55_64
, SUM(g.dem_65_74) AS dem_65_74
, SUM(g.dem_75) AS dem_75

-- rep buckets
, SUM(g.rep_lt18) AS rep_lt18
, SUM(g.rep_18_24) AS rep_18_24
, SUM(g.rep_25_34) AS rep_25_34
, SUM(g.rep_35_44) AS rep_35_44
, SUM(g.rep_45_54) AS rep_45_54
, SUM(g.rep_55_64) AS rep_55_64
, SUM(g.rep_65_74) AS rep_65_74
, SUM(g.rep_75) AS rep_75

-- third party buckets
, SUM(g.grn_lt18 + g.lbr_lt18 + g.uni_lt18 + g.acn_lt18 + g.apv_lt18 + g.uaf_lt18) AS third_lt18
, SUM(g.grn_18_24 + g.lbr_18_24 + g.uni_18_24 + g.acn_18_24 + g.apv_18_24 + g.uaf_18_24) AS third_18_24
, SUM(g.grn_25_34 + g.lbr_25_34 + g.uni_25_34 + g.acn_25_34 + g.apv_25_34 + g.uaf_25_34) AS third_25_34
, SUM(g.grn_35_44 + g.lbr_35_44 + g.uni_35_44 + g.acn_35_44 + g.apv_35_44 + g.uaf_35_44) AS third_35_44 
, SUM(g.grn_45_54 + g.lbr_45_54 + g.uni_45_54 + g.acn_45_54 + g.apv_45_54 + g.uaf_45_54) AS third_45_54
, SUM(g.grn_55_64 + g.lbr_55_64 + g.uni_55_64 + g.acn_55_64 + g.apv_55_64 + g.uaf_55_64) AS third_55_64
, SUM(g.grn_65_74 + g.lbr_65_74 + g.uni_65_74 + g.acn_65_74 + g.apv_65_74 + g.uaf_65_74) AS third_65_74
, SUM(g.grn_75 + g.lbr_75 + g.uni_75 + g.acn_75 + g.apv_75 + g.uaf_75) AS third_75

FROM `valued-lambda-478823-h0.azdd_test.gender_party_age_clean` AS g

GROUP BY 1
)
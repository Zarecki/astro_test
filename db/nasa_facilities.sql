PRAGMA FOREIGN_KEYS = OFF;

DROP TABLE IF EXISTS facilities;

CREATE TABLE facilities (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    center VARCHAR,
    center_search_status VARCHAR,
    facility VARCHAR,
    occupied DATE,
    status VARCHAR,
    url VARCHAR,
    record_date DATE,
    last_update DATE,
    country VARCHAR,
    contact VARCHAR,
    phone VARCHAR,
    latitude FLOAT,
    longitude FLOAT,
    human_address VARCHAR,
    city VARCHAR,
    state VARCHAR,
    zipcode INTEGER,
    computed_region_bigw_e76g INTEGER,
    computed_region_cbhk_fwbd INTEGER,
    computed_region_nnqa_25f4 INTEGER
);
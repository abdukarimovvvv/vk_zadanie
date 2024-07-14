CREATE TABLE apps (
    uuid UUID PRIMARY KEY,
    kind VARCHAR(32) NOT NULL,
    name VARCHAR(128) NOT NULL,
    description TEXT,
    version VARCHAR(20) NOT NULL,
    state VARCHAR(20) DEFAULT 'NEW',
    json_data JSONB NOT NULL
);
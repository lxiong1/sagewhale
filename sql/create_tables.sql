CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE IF NOT EXISTS subscriber (
    id UUID DEFAULT uuid_generate_v4 () PRIMARY KEY,
    first_name VARCHAR(30),
    last_name VARCHAR(30),
    full_name VARCHAR(30)
);

CREATE TABLE IF NOT EXISTS demographics (
    id UUID DEFAULT uuid_generate_v4 () PRIMARY KEY,
    gender VARCHAR(10),
    age INT,
    race VARCHAR(30),
    marital_status VARCHAR(10),
    education VARCHAR(30),
    household_income VARCHAR(30),
    subscriber_id UUID NOT NULL,
    CONSTRAINT subscriber_fk
        FOREIGN KEY (subscriber_id)
            REFERENCES subscriber(id)
            ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS email_performance (
    id UUID DEFAULT uuid_generate_v4 () PRIMARY KEY,
    products JSONB NOT NULL DEFAULT '[]'::JSONB,
    subscriber_id UUID NOT NULL,
    CONSTRAINT subscriber_fk
        FOREIGN KEY (subscriber_id)
            REFERENCES subscriber(id)
            ON DELETE CASCADE
);

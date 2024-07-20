CREATE TABLE customers (
    customer_id VARCHAR(255) NOT NULL,
    customer_unique_id VARCHAR(255),
    customer_zip_code_prefix INT,
    customer_city VARCHAR(255),
    customer_state VARCHAR(255),
    PRIMARY KEY (customer_id)
);
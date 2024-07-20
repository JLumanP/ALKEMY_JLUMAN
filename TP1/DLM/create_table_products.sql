CREATE TABLE products (
    product_id VARCHAR(255) NOT NULL,
    product_category_name VARCHAR(255),
    product_name_length DECIMAL(5, 2),
    product_description_length DECIMAL(5, 2),
    product_photos_qty DECIMAL(5, 2),
    product_weight_g DECIMAL(10, 2),
    product_length_cm DECIMAL(10, 2),
    product_height_cm DECIMAL(10, 2),
    product_width_cm DECIMAL(10, 2),
    PRIMARY KEY (product_id)
);



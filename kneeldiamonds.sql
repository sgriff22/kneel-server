-- Run this block if you already have a database and need to re-create it
DELETE FROM Metals;
DELETE FROM Styles;
DELETE FROM Sizes;
DELETE FROM Orders;

DROP TABLE IF EXISTS Metals;
DROP TABLE IF EXISTS Styles;
DROP TABLE IF EXISTS Sizes;
DROP TABLE IF EXISTS Orders;
-- End block


-- Run this block to create the tables and seed them with some initial data
CREATE TABLE `Metals`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `metal` NVARCHAR(160) NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);

CREATE TABLE `Styles`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `style` NVARCHAR(160) NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);

CREATE TABLE `Sizes`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `carats` NUMERIC(3,2) NOT NULL,
    `price` NUMERIC(8,2) NOT NULL
);

CREATE TABLE `Orders`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `metal_id` INTEGER NOT NULL,
    `size_id` INTEGER NOT NULL,
    `style_id` INTEGER NOT NULL,
    FOREIGN KEY(`metal_id`) REFERENCES `Metals`(`id`),
    FOREIGN KEY(`size_id`) REFERENCES `Sizes`(`id`),
    FOREIGN KEY(`style_id`) REFERENCES `Styles`(`id`)
);

-- Insert statements for Styles
INSERT INTO `Styles` VALUES (NULL, 'Classic', 500);
INSERT INTO `Styles` VALUES (NULL, 'Modern', 710);
INSERT INTO `Styles` VALUES (NULL, 'Vintage', 965);

-- Insert statements for Sizes
INSERT INTO `Sizes` VALUES (NULL, 0.5, 405);
INSERT INTO `Sizes` VALUES (NULL, 0.75, 782);
INSERT INTO `Sizes` VALUES (NULL, 1, 1470);
INSERT INTO `Sizes` VALUES (NULL, 1.5, 1997);
INSERT INTO `Sizes` VALUES (NULL, 2, 3638);

-- Insert statements for Metals
INSERT INTO `Metals`  VALUES (NULL, 'Sterling Silver', 12.42);
INSERT INTO `Metals`  VALUES (NULL, '14K Gold', 736.4);
INSERT INTO `Metals`  VALUES (NULL, '24K Gold', 1258.9);
INSERT INTO `Metals`  VALUES (NULL, 'Platinum', 795.45);
INSERT INTO `Metals`  VALUES (NULL, 'Palladium', 1241);

-- Insert statements for Orders
INSERT INTO `Orders`  VALUES (NULL, 1, 2, 1);
INSERT INTO `Orders`  VALUES (NULL, 3, 5, 3);
INSERT INTO `Orders`  VALUES (NULL, 4, 1, 2);
INSERT INTO `Orders`  VALUES (NULL, 2, 3, 3);
INSERT INTO `Orders`  VALUES (NULL, 5, 4, 2);
-- End block

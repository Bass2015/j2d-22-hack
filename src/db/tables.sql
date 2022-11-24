CREATE TABLE "demanda"(
    "id" INTEGER NOT NULL,
    "week" INTEGER NOT NULL,
    "center_id" INTEGER NOT NULL,
    "meal_id" INTEGER NOT NULL,
    "checkout_price" DOUBLE PRECISION NOT NULL,
    "base_price" DOUBLE PRECISION NOT NULL,
    "emailer_for_promotion" BOOLEAN NOT NULL,
    "homepage_feat" BOOLEAN NOT NULL,
    "num_orders" INTEGER NOT NULL
);
ALTER TABLE
    "demanda" ADD PRIMARY KEY("id");
CREATE TABLE "center"(
    "center_id" INTEGER NOT NULL,
    "city_code" VARCHAR(255) NOT NULL,
    "region_code" VARCHAR(255) NOT NULL,
    "center_type" VARCHAR(255) NOT NULL,
    "op_area" DOUBLE PRECISION NOT NULL
);
ALTER TABLE
    "center" ADD PRIMARY KEY("center_id");
CREATE TABLE "product"(
    "meal_id" INTEGER NOT NULL,
    "category" VARCHAR(255) NOT NULL,
    "cuisine" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "product" ADD PRIMARY KEY("meal_id");
ALTER TABLE
    "demanda" ADD CONSTRAINT "demanda_center_id_foreign" FOREIGN KEY("center_id") REFERENCES "center"("center_id");
ALTER TABLE
    "demanda" ADD CONSTRAINT "demanda_meal_id_foreign" FOREIGN KEY("meal_id") REFERENCES "product"("meal_id");
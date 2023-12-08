08-Dec-2023 09:12 (UTC):
```sql
CREATE TABLE Master (id INTEGER PRIMARY KEY AUTOINCREMENT,symboling, normalized_losses, make, fuel_type, aspiration, num_of_doors, body_style, drive_wheels, engine_location, wheel_base, length, width, height, curb_weight, engine_type, num_of_cylinders, engine_size, fuel_system, bore, stroke, compression_ratio, horsepower, peak_rpm, city_mpg, highway_mpg, price)
```


08-Dec-2023 09:12 (UTC):
```sql
INSERT INTO Master(symboling, normalized_losses, make, fuel_type, aspiration, num_of_doors, body_style, drive_wheels, engine_location, wheel_base, length, width, height, curb_weight, engine_type, num_of_cylinders, engine_size, fuel_system, bore, stroke, compression_ratio, horsepower, peak_rpm, city_mpg, highway_mpg, price) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
```


08-Dec-2023 09:12 (UTC):
```sql
SELECT * FROM Master LIMIT 1
```


08-Dec-2023 09:12 (UTC):
```sql
UPDATE Master SET make = 'alfa_romero' WHERE make = 'alfa-romero'
```


08-Dec-2023 09:12 (UTC):
```sql
SELECT * FROM Master LIMIT 1
```


08-Dec-2023 09:12 (UTC):
```sql
DELETE FROM Master WHERE make = 'alfa_romero'
```


08-Dec-2023 09:12 (UTC):
```sql
SELECT * FROM Master
```


08-Dec-2023 09:12 (UTC):
```sql
CREATE TABLE Master (id INTEGER PRIMARY KEY AUTOINCREMENT,symboling, normalized_losses, make, fuel_type, aspiration, num_of_doors, body_style, drive_wheels, engine_location, wheel_base, length, width, height, curb_weight, engine_type, num_of_cylinders, engine_size, fuel_system, bore, stroke, compression_ratio, horsepower, peak_rpm, city_mpg, highway_mpg, price)
```


08-Dec-2023 09:12 (UTC):
```sql
INSERT INTO Master(symboling, normalized_losses, make, fuel_type, aspiration, num_of_doors, body_style, drive_wheels, engine_location, wheel_base, length, width, height, curb_weight, engine_type, num_of_cylinders, engine_size, fuel_system, bore, stroke, compression_ratio, horsepower, peak_rpm, city_mpg, highway_mpg, price) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
```


08-Dec-2023 09:12 (UTC):
```sql
SELECT * FROM Master LIMIT 5;
```


08-Dec-2023 09:12 (UTC):
```sql
UPDATE Master SET "normalized_losses" = 'Unknown'  
            WHERE "normalized_losses" IS "?";
```


08-Dec-2023 09:12 (UTC):
```sql
DELETE FROM Master WHERE "id" IS 1;
```


08-Dec-2023 09:12 (UTC):
```sql
SELECT * FROM Master LIMIT 1
```


-- 🔹 1. Zonas con más accidentes (por borough)
CREATE OR REPLACE VIEW kpi_accidents_by_borough AS
SELECT borough, COUNT(*) AS total_accidents
FROM accidents
WHERE borough IS NOT NULL AND borough <> ''
GROUP BY borough
ORDER BY total_accidents DESC;

-- 🔹 2. Horas con más accidentes (extrae hora de crash_time)
CREATE OR REPLACE VIEW kpi_accidents_by_hour AS
SELECT 
  SUBSTRING(crash_time FROM 1 FOR 2)::INT AS hour,
  COUNT(*) AS total_accidents
FROM accidents
WHERE crash_time ~ '^\d{2}:\d{2}'
GROUP BY hour
ORDER BY total_accidents DESC;

-- 🔹 3. Tipos de vehículo más involucrados
CREATE OR REPLACE VIEW kpi_vehicle_types AS
SELECT vehicle_type AS vehicle, COUNT(*) AS total_accidents
FROM (
  SELECT vehicle_type_code1 AS vehicle_type FROM accidents
  UNION ALL
  SELECT vehicle_type_code2 FROM accidents
) AS all_vehicles
WHERE vehicle_type IS NOT NULL AND vehicle_type <> ''
GROUP BY vehicle_type
ORDER BY total_accidents DESC;

-- 🔹 4. Total de accidentes por día
CREATE OR REPLACE VIEW kpi_accidents_daily AS
SELECT crash_date, COUNT(*) AS total_accidents
FROM accidents
WHERE crash_date IS NOT NULL
GROUP BY crash_date
ORDER BY crash_date;

-- 🔹 5. Comparativa de accidentes recientes (últimos 30 días vs anteriores)
CREATE OR REPLACE VIEW kpi_accidents_trend_comparison AS
WITH daily AS (
  SELECT crash_date, COUNT(*) AS total
  FROM accidents
  WHERE crash_date IS NOT NULL
  GROUP BY crash_date
),
recent AS (
  SELECT SUM(total) AS recent_accidents
  FROM daily
  WHERE crash_date >= CURRENT_DATE - INTERVAL '30 days'
),
previous AS (
  SELECT SUM(total) AS previous_accidents
  FROM daily
  WHERE crash_date < CURRENT_DATE - INTERVAL '30 days'
)
SELECT
  recent.recent_accidents,
  previous.previous_accidents,
  (recent.recent_accidents - previous.previous_accidents) AS difference
FROM recent, previous;

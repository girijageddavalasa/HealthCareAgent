CREATE TABLE IF NOT EXISTS public.health_measurements (
  type varchar NULL,
  unit varchar NULL,
  creation_date timestamptz NULL,
  start_date timestamptz NULL,
  end_date timestamptz NULL,
  value numeric NULL
);

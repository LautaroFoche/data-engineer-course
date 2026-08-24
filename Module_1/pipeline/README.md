uv run python ingest_data.py 
--pg-user=root   
--pg-pass=root   
--pg-host=localhost   
--pg-port=5432   
--pg-db=ny_taxi   --target-table=yellow_taxi_trips
--network=pg-network
--name pgdatabase
postgres:18


docker run -it --rm \
  --network=pipeline_default \
  taxi_ingest:v001 \
    --pg-user=root \
    --pg-pass=root \
    --pg-host=pgdatabase \
    --pg-port=5432 \
    --pg-db=ny_taxi \
    --target-table=yellow_taxi_trips
### prerequsite
1. docker
2. docker-compose
3. postgresql

### env file
- cam_duration - duration of recorded video in seconds(default `30`)
- live_views_time_schedule - duration of waiting until next record in seconds (default `60`)
- video_path - path to cameras with live views and timelapses. On first app start will create folder on this path (default `/video/`)
- timelapse_delay - duration of waiting until next timelapse builded in seconds (default 3600)
- timelapse_links - file where all timelapses are stored. Needed for building whole timelapse of all videos. Format - `$path/to/file.txt` (default `timelapse_day.txt`) 

### optional
- SECRETE_KEY - secrete key for postgresql db (`default supersecret`)
- POSTGRES_USER - postgres user (`default postgres`)
- POSTGRES_SERVER - database (`default postgres`)
- POSTGRES_PORT - database port (`default 5432`)
- POSTGRES_DB = type of database (`default postgres`)

### build and run
Go to the root directory
Open docker-compose.yml
For `liveviews` and `timelapse` change value of volumes to your absoulte path
Save file

Open terminal in root folder of project
run: `docker-compose build && docker-compose up`
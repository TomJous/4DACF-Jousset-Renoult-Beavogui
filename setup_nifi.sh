#!/bin/bash

CONTAINER_NAME="nifi_projet"

# --- Step 1: Stop and remove containers + volumes ---
echo "Stopping containers and removing volumes..."
docker compose down -v

# --- Step 2: Build and start containers ---
echo "Building and starting containers..."
docker compose up --build -d

# --- Step 3: Waiting that the app is started ---
echo "Step 3: Waiting for NiFi to fully start..."
# follow the logs to get the app started
docker logs -f $CONTAINER_NAME | while read LINE; do
    echo "$LINE"
    if [[ "$LINE" == *"org.apache.nifi.runtime.Application Started Application"* ]]; then
        echo "NiFi has fully started!"
        pkill -P $$ tail   # Stop the following
        break
    fi
done

# --- Step 4: Copy flow.json.gz into NiFi conf ---
FLOW_PATH="./nifi/mon_flow/flow.json.gz"
DEST_PATH="/opt/nifi/nifi-current/conf/flow.json.gz"

if [ ! -f "$FLOW_PATH" ]; then
  echo "ERROR: Flow file $FLOW_PATH not found!"
  exit 1
fi

echo "Copying flow.json.gz into container..."
docker cp "$FLOW_PATH" $CONTAINER_NAME:$DEST_PATH

# --- Step 5: Set permissions for NiFi user inside container ---
echo "Setting ownership and permissions..."
docker exec -u root $CONTAINER_NAME bash -c "chown -R nifi:nifi /opt/nifi/nifi-current/conf/"

# --- Step 6: Restart NiFi container to load the flow ---
echo "Restarting NiFi container..."
docker restart $CONTAINER_NAME

echo "✅ NiFi container is up with flow.json.gz loaded!"
#!/usr/bin/env bash
# wait-for-it.sh: wait for a host and TCP port to become available
set -e

HOST="$1"
PORT="$2"
shift 2

until nc -z "$HOST" "$PORT"; do
	echo "Waiting for $HOST:$PORT..."
	sleep 1

done

echo "$HOST:$PORT is available"
exec "$@"
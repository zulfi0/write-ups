#!/bin/bash
until ./petshop; do
    echo "Server 'petshop' crashed with exit code $?.  Respawning.." >&2
    sleep 1
done


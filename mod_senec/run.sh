#!/usr/bin/with-contenv bashio
set -e


bashio::log.info "Starting..."
SENEC_HOST=$(bashio::config 'SENEC_HOST')
export SENEC_HOST=$(bashio::config 'SENEC_HOST')
bashio::log.info "SENEC_HOST: ${SENEC_HOST}"
bashio::log.info "SENEC_HOST2: ${senec_host}"
bashio::log.info "Starting Python Trigger Script..."
python3 /app/trigger_senec.py

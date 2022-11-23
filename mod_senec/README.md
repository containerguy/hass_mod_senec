![Pipeline](https://github.com/containerguy/mod_senec/actions/workflows/docker-publish.yml/badge.svg)

# hass_mod_senec

Getting data from your senec pv is quite easy, but what about changing things like trigger the safety loading?
This container based tool is using selenium for triggering the safety load button.

# Signing
This repo uses cosign for signing the container image, which is part of the build / publish pipeline

# Usage
* Add Repo to Home Assistant AddOn Store
* Install AddOn through AddOn store
  * Configure IP in Config Tab

# ToDos
* Check if safety loading is activated
* More dynamic scripting, remove sleep() which is for now necessary because the senec appliance takes to long for selenium

![Pipeline](https://github.com/containerguy/mod_senec/actions/workflows/docker-publish.yml/badge.svg)

# mod_senec

Getting data from your senec pv is quite easy, but what about changing things like trigger the safety loading?
This container based tool is using selenium for triggering the safety load button.

# Signing
This repo uses cosign for signing the container image, which is part of the build / publish pipeline

# Usage
```bash
docker run --rm -e SENEC_HOST=192.168.100.100 ghcr.io/containerguy/mod_senec:sha256-c8326d3427d773af0cf86840c07fb3888e0ac9631b8b1ac5f3b865f95509a6f2.sig
```
# ToDos
* Check if safety loading is activated
* More dynamic scripting, remove sleep() which is for now necessary because the senec appliance takes to long for selenium

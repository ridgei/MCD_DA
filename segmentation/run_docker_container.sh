#!/bin/sh
docker run \
  --gpus all \
  -dit \
  --name mcd_da_latest \
  --rm \
  -v ~/small_amount_data/mcd_da:/workspace \
  -v $(readlink -f ./eepa_data/):$(readlink -f ./eepa_data/) \
  -v $(readlink -f ./garbage_data/):$(readlink -f ./garbage_data/) \
  mcd_da zsh
  #-p 6006:6006 \

#!/bin/sh
docker run -it --rm  -v ~/mcd_da:/workspace --gpus all --name mcd_da mcd_da bash

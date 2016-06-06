#!/usr/bin/env sh
# Compute the mean image from the imagenet training lmdb
# N.B. this is available in data/ilsvrc12

EXAMPLE=examples/imagenet
DATA=data/check
TOOLS=build/tools

$TOOLS/compute_image_mean $EXAMPLE/ava_train_lmdb \
  $DATA/imagenet_mean.binaryproto

echo "Done."

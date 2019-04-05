# MisGAN

## loading the data
Data should exist in "/data"
MisGAN will be compatible with all three datasets
python misgan.py --preprocess

## Training
For training misgan 
python misgan.py <fname> --train --misgan

For training misgan imputer
python misgan.py <fname> --train --imputer

Fmputer is trained after misgan finishes training, for simplicity hyper parameter for training are predefined

## Testing
For testing misgan 
python misgan.py <model_name> <fname> --test --misgan

For testing misgan imputer
python misgan.py <model_name> <fname> --test --imputer

## Evaluation
Evaluation of MisGAN uses RMSE score
python misgan.py <model_name> <fname>
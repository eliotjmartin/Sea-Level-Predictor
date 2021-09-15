# This entrypoint file to be used in development
import sea_level_predictor
from unittest import main

# Test function by calling it here
sea_level_predictor.draw_plot()

# Run unit tests automatically
main(module='test_module', exit=False)
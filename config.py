import os

# Find project root
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

# Data paths
RAW_DATA = os.path.join(PROJECT_ROOT, "data", "raw")
REFERENCE_DATA = os.path.join(PROJECT_ROOT, "data", "reference")
PROCESSED_DATA = os.path.join(PROJECT_ROOT, "data", "processed")
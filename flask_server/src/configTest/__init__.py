# """ Configure Flask environment variables separately from the application itself, based on actual environment(prod, dev, testing, etc.) """

# import os

# if os.environ.get("ENV") is not None:
#     if os.environ.get("ENV") == "dev":
#         import src.configTest.dev
#     elif os.environ.get("ENV") == "prod":
#         import src.configTest.prod
#     elif os.environ.get("ENV") == "test":
#         import src.configTest.testing

class ClassifierService:
    def __init__(self, sqs_provider, s3_provider, mongodb_repository):
        self.sqs_provider = sqs_provider
        self.s3_provider = s3_provider
        self.mongodb_repository = mongodb_repository

    def execute(message):
        print(message)

import os
from aws_cdk import (
    Duration,
    Stack,
    aws_lambda as _lambda,
    CfnOutput, 
    aws_iam as iam,
    SecretValue
)
from constructs import Construct
from aws_cdk.aws_cloudwatch import ComparisonOperator
from aws_cdk.aws_sns import Topic

from aws_cdk.aws_cloudwatch_actions import SnsAction


class IacStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.project_name = os.environ.get("PROJECT_NAME")
        self.aws_account_id = os.environ.get("AWS_ACCOUNT_ID")

        self.algorithms = ['astar', 'heuristic']

        for algorithm in self.algorithms:
            lambda_fn = _lambda.Function(
                self,
                f"BattleSnakeLambda{algorithm}",
                runtime=_lambda.Runtime.PYTHON_3_9,
                code=_lambda.Code.from_asset("../src"),
                handler=f"app.main_{algorithm}.handler",
                timeout=Duration.seconds(15),
            )

            lambda_url = lambda_fn.add_function_url(
                auth_type=_lambda.FunctionUrlAuthType.NONE,
            )

            CfnOutput(self, f"{self.project_name}{algorithm}Url",
                      value=lambda_url.url,
                      export_name=f"{self.project_name}{algorithm}UrlValue")    
            
            CfnOutput(self, f"{self.project_name}{algorithm}LambdaConsole",
                        value="https://" + self.region + ".console.aws.amazon.com/lambda/home?region=" + self.region + "#/functions/" + lambda_fn.function_name + "?tab=code",
                        export_name=f"{self.project_name}{algorithm}LambdaConsoleValue"
                        )

       
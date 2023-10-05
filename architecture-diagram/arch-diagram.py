# diagram.py
from diagrams import Diagram
from diagrams.aws.compute import Lambda
from diagrams.programming.language import Python


with Diagram("Lambda Fucntion with a Layer", show=False):
    Python("Lambda Layer") >> Lambda("Demo Lambda")
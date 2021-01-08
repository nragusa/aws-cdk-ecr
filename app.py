#!/usr/bin/env python3

from aws_cdk import core

from cdk_ecr.cdk_ecr_stack import CdkEcrStack


app = core.App()
CdkEcrStack(app, "cdk-ecr")

app.synth()
